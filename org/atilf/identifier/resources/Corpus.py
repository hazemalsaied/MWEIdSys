import nltk
from nltk.stem import WordNetLemmatizer


class Corpus:
    """
        a class used to encapsulate all the information of the corpus
    """

    def __init__(self, path, printReport=False):
        """
            an initializer of the corpus, responsible of creating a structure of objects encapsulating all the information
            of the corpus, its sentences, tokens and MWEs.

            This function iterate over the lines of corpus document to create the precedent ontology
        :param path: the physical path of the corpus document
        """
        self.sentences = []
        with open(path) as corpusFile:
            # Read the corpus file
            lines = corpusFile.readlines()
            sent = None
            senIdx = 1
            for line in lines:
                if len(line) > 0 and line.endswith('\n'):
                    line = line[:-1]
                if line.startswith('1\t'):
                    if sent is not None:
                        sent.setTextandPOS()
                    sent = Sentence(senIdx)
                    senIdx += 1
                    self.sentences.append(sent)
                lineParts = line.split('\t')
                # Empty line or lines of the form: "8-9	can't	_	_"
                if len(lineParts) != 4 or '-' in lineParts[0]:
                    continue
                token = Token(lineParts[0], lineParts[1])
                # Trait the MWE
                if lineParts[3] != '_':
                    vMWEids = lineParts[3].split(';')
                    for vMWEid in vMWEids:
                        id = int(vMWEid.split(':')[0])
                        # New MWE captured
                        if id not in sent.getWMWEIds():
                            type = str(vMWEid.split(':')[1])
                            vMWE = VMWE(id, token, type)
                            sent.vMWEs.append(vMWE)
                        # Another token of an under-processing MWE
                        else:
                            vMWE = sent.getVMWE(id)
                            if vMWE is not None:
                                vMWE.addToken(token)
                        # associate the token with the MWE
                        token.setParent(vMWE)
                # Associate the token with the sentence
                sent.tokens.append(token)
            # Represent the sentence as a sequece of tokens and POS tags
            sent.setTextandPOS()
            sent.recognizeEmbededVMWEs()
            sent.recognizeInterleavingVMWEs()
        # Generate a console in the format of .md file to summarize the corpus antology creation.
        if printReport:
            for sent in self.sentences:
                print sent


class Sentence:
    """
       a class used to encapsulate all the information of a sentence
    """

    def __init__(self, id):
        self.id = id
        self.tokens = []
        self.vMWEs = []
        self.text = ''

    def getWMWEs(self):
        return self.vMWEs

    def getWMWEIds(self):
        result = []
        for vMWE in self.vMWEs:
            result.append(vMWE.getId())
        return result

    def getVMWE(self, id):

        for vMWE in self.vMWEs:
            if vMWE.getId() == int(id):
                return vMWE
        return None

    def setTextandPOS(self):

        tokensTextList = []
        for token in self.tokens:
            self.text += token.text + ' '
            tokensTextList.append(token.text)
        self.text = self.text.strip()
        posTags = nltk.pos_tag(tokensTextList)
        idx = 0
        for token in self.tokens:
            token.addPosTag(posTags[idx][1])
            idx += 1

    def recognizeEmbededVMWEs(self):
        if len(self.vMWEs) <= 1:
            return
        traitedPairs = []
        for vMwe1 in self.vMWEs:
            for vMwe2 in self.vMWEs:
                if vMwe1 is not vMwe2:
                    isTraited = False
                    for pair in traitedPairs:
                        if vMwe1 in pair and vMwe2 in pair:
                            isTraited = True
                    if not isTraited:
                        traitedPairs.append([vMwe1, vMwe2])
                        # Get The longer VMWE
                        masterVmwe = vMwe1
                        slaveVmwe = vMwe2
                        if len(vMwe2.tokens) > len(vMwe2.tokens):
                            masterVmwe = vMwe2
                            slaveVmwe = vMwe1
                        slaveVmwe.isEmbeded = True
                        for token in slaveVmwe.tokens:
                            if masterVmwe not in token.parents:
                                slaveVmwe.isEmbeded = False

    def recognizeInterleavingVMWEs(self):
        if len(self.vMWEs) <= 1:
            return
        for vmwe in self.vMWEs:
            if vmwe.isEmbeded or vmwe.isInterleaving:
                continue
            for token in vmwe.tokens:
                if len(token.parents) > 1:
                    for parent in token.parents:
                        if parent is not vmwe:
                            if parent.isEmbeded:
                                continue
                            parents = sorted(token.parents,key=lambda VMWE:VMWE.id)
                            if parent != parents[0]:
                                parent.isInterleaving = True

    def __str__(self):

        posText = ''
        for token in self.tokens:
            posText += token.posTag + ' '
        posText = posText.strip()
        vMWEText = ''
        for vMWE in self.vMWEs:
            vMWEText += str(vMWE) + '\n'
        return '##Sentence No. ' + str(
            self.id) + '\n**Text:** ' + self.text + '\n**POS Tagging:** ' + posText + '\n###The Verbal MWEs: \n' + vMWEText


class Token:
    """
        a class used to encapsulate all the information of a sentence tokens
    """
    wordNetLemmatiser = WordNetLemmatizer()

    def __init__(self, pos, txt):
        self.position = int(pos)
        self.text = txt
        self.posTag = ''
        self.lemma = Token.wordNetLemmatiser.lemmatize(txt)
        self.parents = []

    def setParent(self, vMWE):
        self.parents.append(vMWE)

    def addPosTag(self, posTag):
        self.posTag = posTag

    def __str__(self):
        parentTxt = ''
        if len(self.parents) != 0:
            for parent in self.parents:
                parentTxt += str(parent) + '\n'

        return str(self.position) + ' : ' + self.text + ' : ' + self.posTag + '\n' + 'parent VMWEs\n' + parentTxt


class VMWE:
    """
        A class used to encapsulate the information of a verbal multi-word expression
    """

    def __init__(self, id, token, type, isEmbeded=False, isInterleaving=False):
        self.id = int(id)
        self.tokens = []
        self.tokens.append(token)
        self.type = type
        self.isEmbeded = isEmbeded
        self.isInterleaving = isInterleaving

    def getId(self):
        return self.id

    def addToken(self, token):
        self.tokens.append(token)

    def __str__(self):
        tokensStr = ''
        for token in self.tokens:
            tokensStr += token.text + ' '
        tokensStr = tokensStr.strip()
        return '**MWE No.:** ' + str(self.id) + '\n**Text:** ' + tokensStr + '\n' + '**Type:** ' + self.type + '\n\n'
