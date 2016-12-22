from corpus import Token
from corpus import VMWE


class Configuration:
    def __init__(self, buffer=[], stack=[], tokens=[], isInitial=False, isTerminal=False):

        self.buffer = buffer
        self.stack = stack
        self.tokens = tokens
        self.isInitial = isInitial
        self.isTerminal = self.isTerminal()

    def isTerminal(self):
        if len(self.buffer) == 0 and len(self.stack) == 0:
            return True
        return False

    def __str__(self):
        stackStr = Configuration.printStack(self.stack)

        # '[  '
        # for elem in self.stack:
        #     if isinstance(elem, Token):
        #         stackStr += str(elem.text) + ', '
        #     else:
        #         stackStr += '['
        #         for sumEl in elem:
        #             stackStr += str(sumEl.text) + ', '
        #         stackStr += ']  '
        # stackStr = stackStr[:-2] + ' ] '

        buffStr = '[  '
        for token in self.buffer:
            buffStr += str(token.text) + ', '
        buffStr = buffStr[:-2] + '] '

        tokensStr = '[  '
        for token in self.tokens:
            if isinstance(token, VMWE):
                tokenStr = '[  '
                for elem in token.tokens:
                    tokenStr += elem.text + ', '
                tokenStr += '] '
                tokensStr += tokenStr + ', '

        tokensStr = tokensStr[:-2] + '] '

        return ' stack = ' + stackStr + ' ; buffer = ' + buffStr + ' ; VMWEs = ' + tokensStr

    @staticmethod
    def printStack(elemlist):

        result = '[ '
        for elem in elemlist:
            if isinstance(elem, Token):
                result += elem.text + ', '
            elif isinstance(elem, list):

                result += Configuration.printStack(elem)
        return result[:-2] + ' ]  '

    @staticmethod
    def getToken(elemlist):

        if isinstance(elemlist, Token):
            return [elemlist]
        result = []
        for elem in elemlist:
            if isinstance(elem, Token):
                result.append(elem)
            elif isinstance(elem, list):
                result.extend(Configuration.getToken(elem))
        return result