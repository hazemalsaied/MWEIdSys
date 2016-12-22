from configuration import Configuration
from trannsition import Transition
from trannsition import TransitionType
from corpus import Token
from corpus import VMWE


class Parser:
    IMPOSSIBLE_SHIFT_TRANSITION = "ERROR: It's impossible to apply a SHIFT transition, the BUFFER is empty!"
    IMPOSSIBLE_MERGE_TRANSITION = "ERROR: It's impossible to apply a MERGE transition, the STACK doesn't contain two elements!"
    IMPOSSIBLE_COMPLETE_TRANSITION = "ERROR: It's impossible to apply a COMPLETE transition, the head of the STACK doesn't contain any element!"
    NO_TRANSITION_TYPE = "ERROR: No transition has been predicted by the classifier"

    @staticmethod
    def parse(classifier, dictVectorizer, sent):

        initialTransition = Transition.createInitialTransition(sent)
        transition = initialTransition
        while not transition.isTerminal():
            featDic = Parser.getConfigurationFeatures(transition.configuration, sent)
            try:
                transType = classifier.predict(dictVectorizer.transform(featDic))
                if transType == 0:
                    transition = Parser.applyShift(transition)
                elif transType == 1:
                    transition = Parser.applyMerge(transition)
                elif transType == 2:
                    transition = Parser.applyComplete(transition)
                else:
                    raise
            except ValueError as e:
                print(Parser.NO_TRANSITION_TYPE)

    @staticmethod
    def staticParse(sent, printReport=True, binary=False):
        sent = Parser.generateTransitions(sent, printReport=printReport, binary=binary)
        return Parser.extractFeatures(sent)

    @staticmethod
    def extractFeatures(sent):

        transition = sent.initialTransition
        transDicList = []
        transLebelsList = []
        while True:
            if transition.next is None:
                break
            transLebelsList.append(transition.next.type.value)
            configuration = transition.configuration
            stackToken = Configuration.getToken(configuration.stack)
            transDic = Parser.getConfigurationFeatures(configuration, sent)
            transDicList.append(transDic)
            transition = transition.next
        return [transLebelsList, transDicList]

    @staticmethod
    def getConfigurationFeatures(configuration, sent):
        transDic = {}
        stackToken = Configuration.getToken(configuration.stack)
        for elem in stackToken:
            elemIdx = len(stackToken) - int(stackToken.index(elem))
            elemTitle = 'S' + str(elemIdx)
            transDic[elemTitle + 'Token'] = elem.text
            transDic[elemTitle + 'POS'] = elem.posTag
            transDic[elemTitle + 'Lemma'] = elem.lemma
        # Features of first element of buffer
        if len(configuration.buffer) > 0:
            bufferElem = configuration.buffer[0]
            transDic['BToken'] = bufferElem.text
            transDic['BPOS'] = bufferElem.posTag
            transDic['BLemma'] = bufferElem.lemma
            # The distance between the first element of the stack and the buffer
            if len(stackToken) > 0:
                transDic['distance'] = str(
                    sent.tokens.index(configuration.buffer[0]) - sent.tokens.index(stackToken[-1]))
        return transDic

    @staticmethod
    def generateTransitions(sent, printReport=True, binary=False):
        initialTransition = Transition.createInitialTransition(sent)
        transition = initialTransition
        while not transition.isTerminal():
            transition = Parser.getNextTransition(transition, binary)
        sent.initialTransition = initialTransition
        if printReport:
            print initialTransition
        return sent

    @staticmethod
    def getNextTransition(transition, binary=False):

        config = transition.configuration
        if config.isInitial:
            return Parser.applyShift(transition)

        # Check for VMWE complete
        newTransition = Parser.checkForComplete(config, transition, binary)
        if newTransition is not None:
            return newTransition

        newTransition = Parser.checkForMerge(config, transition, binary)
        if newTransition is not None:
            return newTransition

        # Check again for one word COMPLETE
        if len(config.stack) > 0 and config.stack[-1] is not None and not isinstance(config.stack[-1], list):
            if (len(config.stack[-1].parentMWEs) == 0):
                return Parser.applyComplete(transition, binary)

            complete = True
            for parent in config.stack[-1].parentMWEs:
                if not parent.isEmbeded and not parent.isInterleaving:
                    complete = False
            if complete:
                return Parser.applyComplete(transition, binary)

        # Apply the default transition: SHIFT
        return Parser.applyShift(transition)

    @staticmethod
    def checkForComplete(config, transition, binary=False):
        # Check up for a possible COMPLETE of MWE after a MERGE transition
        if transition.type == TransitionType.MERGE:
            if len(config.stack) == 1 and isinstance(config.stack[0], list):
                vMWE = None
                parents = []
                tokens = Parser.getToken(config.stack[0])
                for token in tokens:
                    if len(token.parentMWEs) == 1:
                        vMWE = token.parentMWEs[0]
                        break
                    for parent in token.parentMWEs:
                        if parent not in parents:
                            parents.append(parent)
                if vMWE is None:
                    for parent in parents:
                        for token in tokens:
                            if parent not in token.parentMWEs:
                                parents.remove(parent)
                    if len(parents) > 1:
                        print config
                        print 'unexpected Scenario: two VMWE with the same lenght and the same components!'
                        raise
                    vMWE = parents[0]
                if vMWE is not None and len(vMWE.tokens) == len(tokens):
                    return Parser.applyComplete(transition, vMWE.id, vMWE.type, binary=binary)
        return None

    @staticmethod
    def checkForMerge(config, transition, binary=False):
        # Check up of a possible MERGE
        if len(config.stack) > 1:
            hasParent = True

            tokens = []
            for elem in config.stack:
                tokens.extend(Parser.getToken(elem))

            for token in tokens:
                if len(token.parentMWEs) == 0:
                    hasParent = False
                    break
            if hasParent:
                parents = []
                for token in tokens:
                    for parent in token.parentMWEs:
                        if parent not in parents:
                            parents.append(parent)
                selectedParents = parents
                for parent in list(parents):
                    if len(parent.tokens) != len(tokens):
                        selectedParents.remove(parent)
                        continue
                    for token in tokens:
                        if parent not in token.parentMWEs:
                            selectedParents.remove(parent)
                if len(selectedParents) == 1 and not selectedParents[0].isEmbeded and not selectedParents[
                    0].isInterleaving and len(selectedParents[0].tokens) == len(tokens):
                    selectedParent = selectedParents[0]
                    return Parser.applyMerge(transition, binary)
        return None

    @staticmethod
    def applyShift(transition):
        try:
            config = transition.configuration
            if len(config.buffer) > 0:

                lastToken = config.buffer[0]
                newBuffer = list(config.buffer)
                newBuffer = newBuffer[1:]
                newTokens = list(config.tokens)
                newStack = list(config.stack)
                newStack.append(lastToken)

                newConfig = Configuration(buffer=newBuffer, stack=newStack, tokens=newTokens)

                newTransition = Transition(TransitionType.SHIFT, newConfig, previous=transition)
                transition.next = newTransition
                return newTransition

            else:
                raise Exception(Parser.IMPOSSIBLE_SHIFT_TRANSITION)
        except ValueError as e:
            print(Parser.IMPOSSIBLE_SHIFT_TRANSITION)

    @staticmethod
    def applyMerge(transition, binary=False):
        try:
            config = transition.configuration
            if len(config.stack) > 1:
                newBuffer = list(config.buffer)
                if binary:
                    newStack = list(config.stack)[:-2]
                    newStack.append([config.stack[-2], config.stack[-1]])
                else:
                    newStack = [list(config.stack)]
                newTokens = list(config.tokens)
                newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens)
                newTransition = Transition(TransitionType.MERGE, newConfig, previous=transition)
                transition.next = newTransition
                return newTransition
            else:
                raise
        except ValueError as e:
            print(Parser.IMPOSSIBLE_MERGE_TRANSITION)

    @staticmethod
    def applyComplete(transition, vMWEId=None, vMWEType=None, binary=False):
        try:
            config = transition.configuration
            if len(config.stack) > 0:

                newBuffer = list(config.buffer)
                newStack = list(config.stack)
                vMWETokens = Parser.getToken(newStack[0])
                newStack = newStack[:-1]
                newTokens = list(config.tokens)
                if len(vMWETokens) > 1:
                    vMWE = VMWE(vMWEId, vMWETokens[0], vMWEType)
                    vMWE.tokens = vMWETokens
                    newTokens.append(vMWE)
                else:
                    newTokens.append(vMWETokens[0])
                newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens)

                newTransition = Transition(TransitionType.COMPLETE, newConfig, previous=transition)
                transition.next = newTransition
                return newTransition

            else:
                raise
        except ValueError as e:
            print(Parser.IMPOSSIBLE_COMPLETE_TRANSITION)

    @staticmethod
    def getToken(elemlist):

        if isinstance(elemlist, Token):
            return [elemlist]
        result = []
        for elem in elemlist:
            if isinstance(elem, Token):
                result.append(elem)
            elif isinstance(elem, list):
                result.extend(Parser.getToken(elem))
        return result
