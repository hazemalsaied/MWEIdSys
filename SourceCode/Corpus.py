import os

import nltk
from nltk import WordNetLemmatizer
from nltk.tokenize import WordPunctTokenizer


class Corpus:
    """
        a class used to encapsulate all the information of the corpus
    """

    def __init__(self, path, printReport=False, format='conllu'):
        """
            an initializer of the corpus, responsible of creating a structure of objects encapsulating all the information
            of the corpus, its sentences, tokens and MWEs.

            This function iterate over the lines of corpus document to create the precedent ontology
        :param path: the physical path of the corpus document
        """
        self.sentNum = 0
        self.mweNum = 0
        conlluFile = None
        if os.path.isfile(os.path.join(path, 'train.conllu')):
            conlluFile = os.path.join(path, 'train.conllu')
        mweFile = os.path.join(path, 'train.parsemetsv')
        self.sentences = []
        if conlluFile is not None:

            with open(conlluFile) as corpusFile:
                # Read the corpus file
                lines = corpusFile.readlines()
                sent = None
                senIdx = 1
                for line in lines:
                    if len(line) > 0 and line.endswith('\n'):
                        line = line[:-1]
                    if line.startswith('# sentid:'):
                        sentId = line.split('# sentid:')[1].strip()
                        sent = Sentence(senIdx, sentid=sentId)
                        senIdx += 1
                        self.sentences.append(sent)

                    elif line.startswith('# sentence-text:'):
                        sentText = ''
                        if len(line.split(':')) > 1:
                            sent.text = line.split('# sentence-text:')[1]

                    else:
                        lineParts = line.split('\t')

                        if len(lineParts) != 10 or '-' in lineParts[0]:
                            continue
                        morpho = ''
                        if lineParts[5] != '_':
                            morpho = lineParts[5].split('|')
                        token = Token(lineParts[0], lineParts[1], lemma=lineParts[2], posTag=lineParts[4],
                                      abstractPosTag=lineParts[3], morphologicalInfo=morpho,
                                      dependencyParent=int(lineParts[6]),
                                      dependencyLabel=lineParts[7])

                        # Associate the token with the sentence
                        sent.tokens.append(token)

            with open(mweFile) as corpusFile:
                # Read the corpus file
                lines = corpusFile.readlines()
                noSentToAssign = False
                for line in lines:
                    if line == '\n' or line.startswith('# sentence-text:') or (
                                not line.startswith('# sentid:') and noSentToAssign):
                        continue
                    if len(line) > 0 and line.endswith('\n'):
                        line = line[:-1]
                    if line.startswith('# sentid:'):
                        sentId = line.split('# sentid:')[1].strip()
                        sents = [s for s in self.sentences if s.sentid == sentId]
                        if sents is not None and len(sents) > 0:
                            sent = sents[0]
                        if sent is None:
                            noSentToAssign = True
                        else:
                            noSentToAssign = False
                    else:
                        lineParts = line.split('\t')

                        if lineParts is not None and len(lineParts) == 4 and lineParts[3] != '_':
                            tokens = [t for t in sent.tokens if t.position == int(lineParts[0])]
                            if tokens is not None and len(tokens) > 0:
                                token = tokens[0]
                            if token == None:
                                print 'Error: '
                                print sent.text
                            vMWEids = lineParts[3].split(';')
                            for vMWEid in vMWEids:
                                id = int(vMWEid.split(':')[0])
                                # New MWE captured
                                if id not in sent.getWMWEIds():
                                    type = str(vMWEid.split(':')[1])
                                    vMWE = VMWE(id, token, type)
                                    self.mweNum += 1
                                    sent.vMWEs.append(vMWE)
                                # Another token of an under-processing MWE
                                else:
                                    vMWE = sent.getVMWE(id)
                                    if vMWE is not None:
                                        vMWE.addToken(token)
                                # associate the token with the MWE
                                token.setParent(vMWE)
            self.sentNum = len(self.sentences)
            for sent in self.sentences:
                sent.recognizeEmbededVMWEs()
                sent.recognizeInterleavingVMWEs()
        else:
            with open(mweFile) as corpusFile:
                # Read the corpus file
                lines = corpusFile.readlines()
                sent = None
                senIdx = 1
                for line in lines:
                    if len(line) > 0 and line.endswith('\n'):
                        line = line[:-1]
                    if line.startswith('1\t'):
                        # sentId = line.split('# sentid:')[1]
                        if sent is not None:
                            # Represent the sentence as a sequece of tokens and POS tags
                            sent.setTextandPOS()
                            sent.recognizeEmbededVMWEs()
                            sent.recognizeInterleavingVMWEs()
                        sent = Sentence(senIdx)
                        senIdx += 1
                        self.sentences.append(sent)

                    elif line.startswith('# sentence-text:'):
                        sentText = ''
                        if len(line.split(':')) > 1:
                            sent.text = line.split('# sentence-text:')[1]

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
                                self.mweNum += 1
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
                self.sentNum = len(self.sentences)


class SPMLRCorpus:
    def __init__(self, path, verbalEx=True, printReport=True):

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
                        # Represent the sentence as a sequece of tokens and POS tags
                        self.recognizeMWE(sent)
                        sent.text = ''
                        for token in sent.tokens:
                            sent.text += token.text + ' '
                        sent.text = sent.text.strip()
                    sent = Sentence(senIdx)
                    senIdx += 1
                    self.sentences.append(sent)
                lineParts = line.split('\t')
                # Empty line or lines of the form: "8-9	can't	_	_"
                if len(lineParts) != 10 or '-' in lineParts[0]:
                    continue
                morpho = ''
                if lineParts[5] != '_':
                    morpho = lineParts[5].split('|')
                token = Token(lineParts[0], lineParts[1], lemma=lineParts[2], posTag=lineParts[4],
                              abstractPosTag=lineParts[3], morphologicalInfo=morpho,
                              dependencyParent=int(lineParts[6]),
                              dependencyLabel=lineParts[7])

                # Associate the token with the sentence
                sent.tokens.append(token)

        if verbalEx:
            for sent in self.sentences:
                for mwe in sent.vMWEs:
                    mwe.isVerbal = VMWE.isVerbalMwe(mwe)
                sent.vMWEs = [x for x in sent.vMWEs if x.isVerbal]

        self.sentences = [x for x in self.sentences if (len(x.vMWEs) > 0)]

        # Generate a console in the format of .md file to summarize the corpus antology creation.
        # if printReport:
        #     for sent in self.sentences:
        #         print sent

    def recognizeMWE(self, sent):
        mwe = None
        for token in sent.tokens:
            if token.dependencyLabel == 'dep_cpd':
                tokenIndex = sent.tokens.index(token)
                previousToken = sent.tokens[tokenIndex - 1]
                if previousToken.dependencyLabel != 'dep_cpd':
                    mwe = VMWE(len(sent.vMWEs))
                    sent.vMWEs.append(mwe)
                    mwe.tokens.append(previousToken)
                    previousToken.parentMWEs.append(mwe)
                mwe.tokens.append(token)
                token.parentMWEs.append(mwe)


class Sentence:
    """
       a class used to encapsulate all the information of a sentence
    """

    def __init__(self, id, sentid=''):

        self.sentid = sentid
        self.id = id
        self.tokens = []
        self.vMWEs = []
        self.identifiedVMWEs = []
        self.text = ''
        self.initialTransition = None
        self.featuresInfo = []

    @staticmethod
    def fromTextToSent(text):

        tokenizer = WordPunctTokenizer()
        wordNetLemmatiser = WordNetLemmatizer()
        sent = Sentence(0)
        sent.text = text
        tokenList = tokenizer.tokenize(text)
        posTags = nltk.pos_tag(tokenList)
        for token in tokenList:
            tokenLemma = wordNetLemmatiser.lemmatize(token)
            tokenPos = posTags[tokenList.index(token)][1]
            tokenObj = Token(tokenList.index(token), token, lemma=tokenLemma, posTag=tokenPos)
            sent.tokens.append(tokenObj)
        return sent

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
        # posTags = nltk.pos_tag(tokensTextList)
        # idx = 0
        # for token in self.tokens:
        #     token.addPosTag(posTags[idx][1])
        #     idx += 1

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
                            if masterVmwe not in token.parentMWEs:
                                slaveVmwe.isEmbeded = False

    def recognizeInterleavingVMWEs(self):
        if len(self.vMWEs) <= 1:
            return
        for vmwe in self.vMWEs:
            if vmwe.isEmbeded or vmwe.isInterleaving:
                continue
            for token in vmwe.tokens:
                if len(token.parentMWEs) > 1:
                    for parent in token.parentMWEs:
                        if parent is not vmwe:
                            if parent.isEmbeded:
                                continue
                            parents = sorted(token.parentMWEs, key=lambda VMWE: VMWE.id)
                            if parent != parents[0]:
                                parent.isInterleaving = True

    def getCorpusText(self, gold=True):
        if gold:
            mwes = self.vMWEs
        else:
            mwes = self.identifiedVMWEs
        lines = ''
        idx = 1
        for token in self.tokens:
            line = str(idx) + '\t' + token.text + '\t_\t'
            idx += 1
            for mwe in mwes:
                if token in mwe.tokens:
                    if line.endswith('\t'):
                        line += str(mwe.id)
                    else:
                        line += ';' + str(mwe.id)
            if line.endswith('\t'):
                line += '_'
            lines += line + '\n'
        return lines

    def printSummary(self):
        vMWEText = ''
        for vMWE in self.vMWEs:
            vMWEText += str(vMWE) + '\n'
        if len(self.identifiedVMWEs) > 0:
            identifiedMWE = '###Identified MWEs: \n'
            for mwe in self.identifiedVMWEs:
                identifiedMWE += str(mwe) + '\n'
        else:
            identifiedMWE = ''

        return '##Sentence No. ' + str(self.id) + ' - ' + self.sentid + '\n' + self.text + \
               '\n###Existing MWEs: \n' + vMWEText + identifiedMWE

    def __str__(self):

        vMWEText = ''
        for vMWE in self.vMWEs:
            vMWEText += str(vMWE) + '\n'
        if len(self.identifiedVMWEs) > 0:
            identifiedMWE = '###Identified MWEs: \n'
            for mwe in self.identifiedVMWEs:
                identifiedMWE += str(mwe) + '\n'
        else:
            identifiedMWE = ''
        featuresInfo = ''
        if len(self.featuresInfo) == 2:
            labels = self.featuresInfo[0]
            features = self.featuresInfo[1]
            for x in xrange(0, len(labels)):
                featuresInfo += str(x) + '- ' + str(labels[x]) + ' : ' + str(features[x]) + '\n'
        return '##Sentence No. ' + str(self.id) + ' - ' + self.sentid + '\n' + self.text + \
               '\n###Existing MWEs: \n' + vMWEText + identifiedMWE \
               + '\n' + str(self.initialTransition) + '\n###Features: \n' + featuresInfo


class Token:
    """
        a class used to encapsulate all the information of a sentence tokens
    """

    # wordNetLemmatiser = WordNetLemmatizer()

    def __init__(self, position, txt, lemma='', posTag='', abstractPosTag='', morphologicalInfo=[], dependencyParent=0,
                 dependencyLabel=''):
        self.position = int(position)
        self.text = txt
        # if lemma == '':
        #    self.lemma = Token.wordNetLemmatiser.lemmatize(txt)
        # else:
        self.lemma = lemma
        self.abstractPosTag = abstractPosTag
        self.posTag = posTag
        self.morphologicalInfo = morphologicalInfo
        self.dependencyParent = dependencyParent
        self.dependencyLabel = dependencyLabel
        self.parentMWEs = []

    def setParent(self, vMWE):
        self.parentMWEs.append(vMWE)

    def addPosTag(self, posTag):
        self.posTag = posTag

    def __str__(self):
        parentTxt = ''
        if len(self.parentMWEs) != 0:
            for parent in self.parentMWEs:
                parentTxt += str(parent) + '\n'

        return str(self.position) + ' : ' + self.text + ' : ' + self.posTag + '\n' + 'parent VMWEs\n' + parentTxt


class VMWE:
    """
        A class used to encapsulate the information of a verbal multi-word expression
    """

    def __init__(self, id, token=None, type=None, isEmbeded=False, isInterleaving=False):
        self.id = int(id)
        self.tokens = []
        if token is not None:
            self.tokens.append(token)
        self.type = ''
        if type is not None:
            self.type = type
        self.isEmbeded = isEmbeded
        self.isInterleaving = isInterleaving
        self.isVerbal = True

    def getId(self):
        return self.id

    def addToken(self, token):
        self.tokens.append(token)

    @staticmethod
    def isVerbalMwe(mwe):
        isVerbal = False
        for token in mwe.tokens:
            if token.posTag.startswith('V'):
                isVerbal = True
        return isVerbal

    def __str__(self):
        tokensStr = ''
        for token in self.tokens:
            tokensStr += token.text + ' '
        tokensStr = tokensStr.strip()
        isInterleaving = ''
        if self.isInterleaving:
            isInterleaving = ', Interleaving '
        isEmbedded = ''
        if self.isEmbeded:
            isEmbedded = ', Embedded'
        type = ''
        if self.type != '':
            type = self.type
        return str(self.id) + '- ' + '**' + tokensStr + '** (' + type + ')' + isEmbedded + isInterleaving

    def getString(self):
        result = ''
        for token in self.tokens:
            result += token.text + ' '
        return result[:-1]
