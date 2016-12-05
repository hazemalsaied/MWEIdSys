from org.atilf.identifier.parser.configuration import Configuration
from enum import Enum


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
            return self.configuration.isTerminal
        return False

    def __str__(self):
        result = 'Trans\t\t===>\t\tConfiguration\n'
        transition = self
        while True:
            type = ''
            configuration = ''
            if transition.type is not None:
                type = transition.type.name
            configuration = str(transition.configuration)
            result += type + '\t\t===>\t\t' + configuration + '\n'
            if transition.next is None:
                break
            transition = transition.next
        return result

class TransitionType(Enum):

    SHIFT = 1
    MERGE = 2
    COMPLETE = 3

