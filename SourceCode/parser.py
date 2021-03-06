from configuration import Configuration
from corpus import Token
from corpus import VMWE
from trannsition import Transition
from trannsition import TransitionType


class Parser:
    IMPOSSIBLE_SHIFT_TRANSITION = "ERROR: It's impossible to apply a SHIFT transition, the BUFFER is empty!"
    IMPOSSIBLE_MERGE_TRANSITION = "ERROR: It's impossible to apply a MERGE transition, the STACK doesn't contain two elements!"
    IMPOSSIBLE_COMPLETE_TRANSITION = "ERROR: It's impossible to apply a COMPLETE transition, the head of the STACK doesn't contain any element!"
    NO_TRANSITION_TYPE = "ERROR: No transition has been predicted by the classifier"

    @staticmethod
    def parse(classifier, dictVectorizer, sent,  binary=True):

        initialTransition = Transition.createInitialTransition(sent)
        transition = initialTransition
        transDicList = []
        transLebelsList = []
        while not transition.configuration.isTerminalConf():
            featDic = Parser.getConfigurationFeatures(transition, sent)
            transDicList.append(featDic)
            transType = classifier.predict(dictVectorizer.transform(featDic))
            config = transition.configuration
            if len(config.stack) == 0 and len(config.buffer) > 0:
                transition = Parser.applyShift(transition)
                transLebelsList.append(0)
            elif len(config.buffer) == 0 and len(config.stack) == 1:
                transition = Parser.applyComplete(transition, sent, parse=True)
                transLebelsList.append(2)
            elif transType == 0:
                if len(config.buffer) > 0:
                    transition = Parser.applyShift(transition)
                    transLebelsList.append(0)
                else:
                    transition = Parser.applyComplete(transition, sent, parse=True)
                    transLebelsList.append(2)
            elif transType == 1:
                if len(transition.configuration.stack) > 1:
                    transition = Parser.applyMerge(transition)
                    transLebelsList.append(1)
                else:
                    transition = Parser.applyComplete(transition, sent, parse=True)
                    transLebelsList.append(2)
            elif transType == 2:
                transition = Parser.applyComplete(transition, sent, parse=True)
                transLebelsList.append(2)
            else:
                print(Parser.NO_TRANSITION_TYPE)

        sent.initialTransition = initialTransition
        sent.featuresInfo = [transLebelsList, transDicList]
        return sent

    @staticmethod
    def staticParse(sent, printReport=False,  binary=True):
        sent = Parser.generateTransitions(sent, printReport=printReport, binary=binary)
        if sent is not None:
            return Parser.extractFeatures(sent)
        return None

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
            transDic = Parser.getConfigurationFeatures(transition, sent)
            transDicList.append(transDic)
            transition = transition.next
        sent.featuresInfo = [transLebelsList, transDicList]
        return [transLebelsList, transDicList]

    @staticmethod
    def getConfigurationFeatures(transition, sent):
        transDic = {}
        elemIdx = 0
        configuration = transition.configuration
        if len(configuration.stack) >= 2:
            stackElements = [configuration.stack[-2], configuration.stack[-1]]
        else: stackElements = configuration.stack

        for elem in stackElements:
            elemTitle = 'S' + str(elemIdx)
            if isinstance(elem, Token):
                transDic[elemTitle + 'Token'] = elem.text
                transDic[elemTitle + 'POS'] = elem.posTag
                transDic[elemTitle + 'Lemma'] = elem.lemma
            elif isinstance(elem, list):
                transDic[elemTitle + 'Token'] = ''
                transDic[elemTitle + 'POS'] = ''
                transDic[elemTitle + 'Lemma'] = ''
                tokens = Configuration.getToken(elem)
                for token in tokens:
                    transDic[elemTitle + 'Token'] += token.text + '-'
                    transDic[elemTitle + 'POS'] += token.posTag + '-'
                    transDic[elemTitle + 'Lemma'] += token.lemma + '-'
                transDic[elemTitle + 'Token'] = transDic[elemTitle + 'Token'][:-1]
                transDic[elemTitle + 'POS'] = transDic[elemTitle + 'POS'][:-1]
                transDic[elemTitle + 'Lemma'] = transDic[elemTitle + 'Lemma'][:-1]
            elemIdx += 1

        if len(configuration.buffer) > 0:
            element = configuration.buffer[0]
            transDic['B0Token'] = element.text
            transDic['B0POS'] = element.posTag
            transDic['B0Lemma'] = element.lemma

            if len(configuration.buffer) > 1:
                element = configuration.buffer[1]
                transDic['B1Token'] = element.text
                transDic['B1POS'] = element.posTag
                transDic['B1Lemma'] = element.lemma

        if len(configuration.stack) > 0 and len(configuration.buffer) > 0:
            stackTokens = Configuration.getToken(configuration.stack[-1])
            transDic['distance'] = str(
                sent.tokens.index(configuration.buffer[0]) - sent.tokens.index(stackTokens[-1]))

        if transition.previous is not None:
            transDic['prevriousT'] = str(transition.previous.type)
            if transition.previous.previous is not None:
                transDic['antepenultimateT'] = str(transition.previous.previous.type)
            else: transDic['antepenultimateT'] = '_'
        else:
            transDic['prevriousT'] = '_'
            transDic['antepenultimateT'] = '_'

        return transDic

    @staticmethod
    def generateTransitions(sent, printReport=True,  binary=True):
        initialTransition = Transition.createInitialTransition(sent)
        transition = initialTransition
        while transition is not None and not transition.isTerminal():
            transition = Parser.getNextTransition(transition, sent, binary)
        if transition is not None:
            sent.initialTransition = initialTransition
            return sent
        return None

    @staticmethod
    def getNextTransition(transition, sent,  binary=True):

        config = transition.configuration
        if config.isInitial:
            return Parser.applyShift(transition)

        # Check for VMWE complete
        newTransition = Parser.checkForComplete(config, transition, sent)
        if newTransition is not None:
            return newTransition

        newTransition = Parser.checkForMerge(config, transition, binary)
        if newTransition is not None:
            return newTransition

        # Check again for one word COMPLETE
        if len(config.stack) > 0 and config.stack[-1] is not None and not isinstance(config.stack[-1], list):
            if (len(config.stack[-1].parentMWEs) == 0):
                return Parser.applyComplete(transition, sent, parse=False)

            complete = True
            for parent in config.stack[-1].parentMWEs:
                if not parent.isEmbeded and not parent.isInterleaving:
                    complete = False
            if complete:
                return Parser.applyComplete(transition, sent, parse=False)

        # Apply the default transition: SHIFT
        return Parser.applyShift(transition)

    @staticmethod
    def checkForComplete(config, transition, sent):
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
                        print sent
                        print config
                        print 'unexpected Scenario: two VMWE with the same lenght and the same components!'
                    vMWE = parents[0]
                if vMWE is not None and len(vMWE.tokens) == len(tokens):
                    return Parser.applyComplete(transition, sent, vMWE.id, vMWE.type)
        return None

    @staticmethod
    def checkForMerge(config, transition,  binary=True):
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
                        if parent in selectedParents:
                            selectedParents.remove(parent)
                        continue
                    for token in tokens:
                        if parent not in token.parentMWEs:
                            if parent in selectedParents:
                                selectedParents.remove(parent)
                if len(selectedParents) == 1 and not selectedParents[0].isEmbeded and not selectedParents[
                    0].isInterleaving and len(selectedParents[0].tokens) == len(tokens):
                    selectedParent = selectedParents[0]
                    return Parser.applyMerge(transition, binary)
        return None

    @staticmethod
    def applyShift(transition):
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
            print config
            print(Parser.IMPOSSIBLE_SHIFT_TRANSITION)
            return None
            # raise Exception(Parser.IMPOSSIBLE_SHIFT_TRANSITION)
            # except ValueError as e:
            #     print(Parser.IMPOSSIBLE_SHIFT_TRANSITION)
            #     pass

    @staticmethod
    def applyMerge(transition,  binary=True):
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
            print config
            print(Parser.IMPOSSIBLE_MERGE_TRANSITION)
            return None

    @staticmethod
    def applyComplete(transition, sent, vMWEId=None, vMWEType=None, parse=False):
        config = transition.configuration
        if len(config.stack) > 0:

            newBuffer = list(config.buffer)
            newStack = list(config.stack)
            vMWETokens = Parser.getToken(newStack[0])
            newStack = newStack[:-1]
            newTokens = list(config.tokens)
            Parser.getVMWENumber(newTokens)
            if len(vMWETokens) > 1:
                if vMWEId is None:
                    vMWEId = Parser.getVMWENumber(newTokens) + 1
                vMWE = VMWE(vMWEId, vMWETokens[0], vMWEType)
                if parse:
                    sent.identifiedVMWEs.append(vMWE)
                vMWE.tokens = vMWETokens
                newTokens.append(vMWE)
            else:
                newTokens.append(vMWETokens[0])
            newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens)

            newTransition = Transition(TransitionType.COMPLETE, newConfig, previous=transition)
            transition.next = newTransition
            return newTransition

        else:
            print sent
            print config
            print(Parser.IMPOSSIBLE_COMPLETE_TRANSITION)
            return None

    @staticmethod
    def getVMWENumber(tokens):
        result = 0
        for token in tokens:
            if isinstance(token, VMWE):
                result += 1
        return result

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
