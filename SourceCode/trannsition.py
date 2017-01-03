from enum import Enum

from configuration import Configuration


class Transition:
    def __init__(self, type, config, previous=None, next=None):
        self.type = type
        self.configuration = config
        self.previous = previous
        self.next = next

    @staticmethod
    def createInitialTransition(sent):

        initialConfig = Configuration(buffer=sent.tokens, isInitial=True)
        initialTransition = Transition(None, config=initialConfig)

        return initialTransition

    def isInitial(self):
        if self.configuration is not None:
            return self.configuration.isInitial
        return False

    def isTerminal(self):
        if self.configuration is not None:
            return self.configuration.isTerminalConf()
        return False

    def __str__(self):
        result = 'Trans   \t>\t\tConfiguration\n'
        transition = self
        while True:
            type = ''
            configuration = ''
            if transition.type is not None:
                type = transition.type.name
            else:
                type = '        '
            configuration = str(transition.configuration)
            if len(type) == 5:
                type = type + '   '
            result += type + '\t>\t\t' + configuration + '\n'
            if transition.next is None:
                break
            transition = transition.next
        return result


class TransitionType(Enum):
    SHIFT = 0
    MERGE = 1
    COMPLETE = 2
