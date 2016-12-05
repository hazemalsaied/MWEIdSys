from org.atilf.identifier.parser.configuration import Configuration
from org.atilf.identifier.parser.trannsition import Transition
from org.atilf.identifier.parser.trannsition import TransitionType
from org.atilf.identifier.resources.Corpus import VMWE


class StaticOracle:
    IMPOSSIBLE_SHIFT_TRANSITION = "It's impossible to apply a SHIFT transition, the BUFFER is empty!"
    IMPOSSIBLE_MERGE_TRANSITION = "It's impossible to apply a MERGE transition, the STACK doesn't contain two elements!"
    IMPOSSIBLE_COMPLETE_TRANSITION = "It's impossible to apply a COMPLETE transition, the head of the STACK doesn't contain any element!"

    @staticmethod
    def parse(sent):
        initialTransition = Transition.createInitialTransition(sent)
        transition = initialTransition
        while not transition.isTerminal():
            transition = StaticOracle.getNextTransition(transition)
            print transition
        #print initialTransition

    @staticmethod
    def getNextTransition(transition):

        config = transition.configuration
        if config.isInitial:
            return StaticOracle.applyShift(transition)

        # Check for VMWE complete
        newTransition = StaticOracle.checkForComplete(config, transition)
        if newTransition is not None:
            return newTransition

        newTransition = StaticOracle.checkForMerge(config, transition)
        if newTransition is not None:
            return newTransition

        # Check again for one word COMPLETE
        if len(config.stack) > 0 and config.stack[-1] is not None and not isinstance(config.stack[-1], list):
            if (len(config.stack[-1].parents) == 0):
                return StaticOracle.applyComplete(transition)

            complete = True
            for parent in config.stack[-1].parents:
                if not parent.isEmbeded and not parent.isInterleaving:
                    complete = False
            if complete:
                return StaticOracle.applyComplete(transition)

        # Apply the default transition: SHIFT
        return StaticOracle.applyShift(transition)

    @staticmethod
    def checkForComplete(config, transition):
        # Check up for a possible COMPLETE of MWE after a MERGE transition
        if transition.type == TransitionType.MERGE:
            if len(config.stack) == 1 and isinstance(config.stack[0], list):
                vMWE = None
                parents = []
                for token in config.stack[0]:
                    if len(token.parents) == 1:
                        vMWE = token.parents[0]
                        break
                    for parent in token.parents:
                        if parent not in parents:
                            parents.append(parent)
                if vMWE is None:
                    for parent in parents:
                        for token in config.stack[0]:
                            if parent not in token.parents:
                                parents.remove(parent)
                    if len(parents) > 1:
                        print config
                        print 'unexpected Scenario: two VMWE with the same lenght and the same components!'
                        raise
                    vMWE = parents[0]
                if vMWE is not None and len(vMWE.tokens) == len(config.stack[0]):
                    return StaticOracle.applyComplete(transition, vMWE.id, vMWE.type)
        return None

    @staticmethod
    def checkForMerge(config, transition):
        # Check up of a possible MERGE
        if len(config.stack) > 1:
            hasParent = True
            for token in config.stack:
                if len(token.parents) == 0:
                    hasParent = False
                    break
            if hasParent:
                parents = []
                for token in config.stack:
                    for parent in token.parents:
                        if parent not in parents:
                            parents.append(parent)
                selectedParents = parents
                for parent in list(parents):
                    if len(parent.tokens) != len(config.stack):
                        selectedParents.remove(parent)
                        continue
                    for token in config.stack:
                        if parent not in token.parents:
                            selectedParents.remove(parent)
                if len(selectedParents) == 1 and not selectedParents[0].isEmbeded and not selectedParents[
                    0].isInterleaving and len(selectedParents[0].tokens) == len(config.stack):
                    selectedParent = selectedParents[0]
                    return StaticOracle.applyMerge(transition)
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
                raise
        except ValueError as e:
            print(StaticOracle.IMPOSSIBLE_SHIFT_TRANSITION)

    @staticmethod
    def applyMerge(transition):
        try:
            config = transition.configuration
            if len(config.stack) > 1:
                newBuffer = list(config.buffer)
                newStack = [list(config.stack)]
                newTokens = list(config.tokens)
                newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens)
                newTransition = Transition(TransitionType.MERGE, newConfig, previous=transition)
                transition.next = newTransition
                return newTransition
            else:
                raise
        except ValueError as e:
            print(StaticOracle.IMPOSSIBLE_MERGE_TRANSITION)

    @staticmethod
    def applyComplete(transition, vMWEId=None, vMWEType=None):
        try:
            config = transition.configuration
            if len(config.stack) > 0:

                newBuffer = list(config.buffer)
                newStack = list(config.stack)
                vMWETokens = newStack[0]
                newStack = newStack[:-1]
                newTokens = list(config.tokens)
                if vMWETokens is list:
                    vMWE = VMWE(vMWEId, vMWETokens, vMWEType)
                    newTokens.append(vMWE)
                else:
                    newTokens.append(vMWETokens)
                newConfig = Configuration(stack=newStack, buffer=newBuffer, tokens=newTokens)

                newTransition = Transition(TransitionType.COMPLETE, newConfig, previous=transition)
                transition.next = newTransition
                return newTransition

            else:
                raise
        except ValueError as e:
            print(StaticOracle.IMPOSSIBLE_COMPLETE_TRANSITION)
