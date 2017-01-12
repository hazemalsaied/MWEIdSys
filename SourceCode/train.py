import codecs
import datetime
import os
import pickle
import sys
from random import randint

import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OutputCodeClassifier, OneVsRestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

from corpus import Corpus
from evaluate import Evaluation
from parser import Parser


class Train:
    @staticmethod
    def train(corpusName, binary=True, verbalEx=False, printReport=False, enableSerialization=False):

        languageName = corpusName.split('/')[-1]
        if languageName.strip() == '':
            languageName = corpusName.split('/')[-2]
        dumpingFolder = '/Users/hazemalsaied/Parseme/MWEIdSys/Serialization/'
        if not os.path.exists(dumpingFolder):
            os.makedirs(dumpingFolder)

        if enableSerialization:
            # Reading the corpus
            corpus = Corpus(corpusName, printReport=printReport)
            # corpus = SPMLRCorpus(corpusName, verbalEx=verbalEx, printReport=printReport)
            with open(os.path.join(dumpingFolder, languageName + '.pickle'), 'wb') as f:
                pickle.dump(corpus, f)
        else:
            with open(os.path.join(dumpingFolder, languageName + '.pickle'), 'rb') as f:
                corpus = pickle.load(f)

        # creating an initial report
        if printReport:
            languageName = corpusName.split('/')[-1]
            if len(languageName) > 0:
                Evaluation.resultsPath = os.path.join(Evaluation.resultsPath, languageName)
            else:
                Evaluation.resultsPath = os.path.join(Evaluation.resultsPath, corpusName.split('/')[-2])
            if not os.path.exists(Evaluation.resultsPath):
                os.makedirs(Evaluation.resultsPath)

            printingPath = os.path.join(Evaluation.resultsPath, 'Readme.md')
            staticParsingFile = open(printingPath, 'w')
            result = '##Number of Sentences: ' + str(corpus.sentNum) + '\n##Number of MWEs: ' + str(corpus.mweNum)
            staticParsingFile.write(result)

        # Spliting the data in train and testing
        sentenceNum = int(len(corpus.sentences) * 0.8)
        trainingSents = corpus.sentences[0:sentenceNum]
        testingSents = corpus.sentences[sentenceNum + 1:]

        # Training classifier
        cls = Train.classify(trainingSents, printReport=printReport, binary=binary)

        # Parsing the test phrases
        for sent in testingSents:
            Parser.parse(cls[0], cls[1], sent, binary=binary)

        # creating a parsing report
        if printReport:
            Train.createParsingReport(testingSents)

        goldCorpus = ''
        for sent in testingSents:
            goldCorpus += sent.getCorpusText() + '\n'
        goldtestingCorpusPath = os.path.join(os.path.join('/Users/hazemalsaied/Parseme/MWEIdSys/Results/',languageName),
                                             languageName + '.gold')
        goldtestingCorpusFile = open(goldtestingCorpusPath, 'w')
        goldtestingCorpusFile.write(goldCorpus)

        predCorpus = ''
        for sent in testingSents:
            predCorpus += sent.getCorpusText(gold=False) + '\n'
        goldtestingCorpusPath = os.path.join(os.path.join('/Users/hazemalsaied/Parseme/MWEIdSys/Results/',languageName),
                                             languageName + '.pred')
        goldtestingCorpusFile = open(goldtestingCorpusPath, 'w')
        goldtestingCorpusFile.write(predCorpus)

        # Evaluation
        Evaluation.evaluate(testingSents, printReport=True)

        # Enjoying testing
        testingCorpusPath = '/Users/hazemalsaied/Parseme/MWEIdSys/Corpora/testing/'
        while True:
            sentId = raw_input('again? ')
            sents = [s for s in corpus.sentences if s.sentid == sentId]
            if sents is None or sents == []:
                testingCorpus = Corpus(testingCorpusPath, printReport=printReport)
                for sent in testingCorpus.sentences:
                    Parser.parse(cls[0], cls[1], sent, binary=binary)
                    print sent
            else:
                sent = sents[0]
                print sent
                Parser.parse(cls[0], cls[1], sent, binary=binary)
                print sent

    @staticmethod
    def classify(sents, printReport=False, binary=True):

        staticParsingData = Train.getStaticParseData(sents, printReport=printReport, binary=binary)
        if printReport:
            Train.createStaticParsingReports(sents)

        vec = DictVectorizer()
        X = vec.fit_transform(staticParsingData[1])
        Y = np.asarray(staticParsingData[0])
        F = vec.get_feature_names()
        report = '## The number of features used: ' + str(len(F))
        time = datetime.datetime.now()
        report += '\n## Transition classification evaluation: \n'
        score = []
        clfs = []
        oneVsRest = Train.evaluateOneVsRest(X, Y)
        report += '### 1- SVM One Vs Rest: \n' + 'Score: ' + str(oneVsRest[0]) + ', Number of merge operation: ' + str(
            oneVsRest[1]) + '\n'
        score.append(oneVsRest[1])
        clfs.append(oneVsRest[2])
        outputCode = Train.evaluateOutputCode(X, Y)
        report += '### 2- SVM Output Code: \n' + 'Score: ' + str(outputCode[0]) + ', Number of merge operation: ' + str(
            outputCode[1]) + '\n'
        score.append(outputCode[1])
        clfs.append(outputCode[2])
        oneVsOne = Train.evaluateOneVsOne(X, Y)
        report += '### 3- SVM One Vs One : \n' + 'Score: ' + str(oneVsOne[0]) + ', Number of merge operation: ' + str(
            oneVsOne[1]) + '\n'
        score.append(oneVsOne[1])
        clfs.append(oneVsOne[2])
        gaussianNaiveBayes = Train.evaluateGaussianNaiveBayes(X, Y)
        report += '### 4- Gaussian Naive Bayes : \n' + 'Score: ' + str(
            gaussianNaiveBayes[0]) + ', Number of merge operation: ' + str(
            gaussianNaiveBayes[1]) + '\n'
        score.append(gaussianNaiveBayes[1])
        clfs.append(gaussianNaiveBayes[2])
        idx = score.index(max(score))
        report += '### The Selected Classifier is: ' + str(idx) + '\n'
        clf = clfs[idx]

        if printReport:
            printingPath = os.path.join(Evaluation.resultsPath, 'Readme.md')
            staticParsingFile = open(printingPath, 'a')
            staticParsingFile.write(report)

        clf.fit(X, Y)
        print 'Training classifier duration: ' + str(datetime.datetime.now() - time)
        return [clf, vec]

    @staticmethod
    def getStaticParseData(sents, printReport=False, binary=True):
        trainingData = []
        trainDataLabel = []
        time = datetime.datetime.now()
        for sent in sents:
            # Parse the sentence
            trainingInfo = Parser.staticParse(sent, printReport=printReport, binary=binary)
            if trainingInfo is not None:
                trainDataLabel.extend(trainingInfo[0])
                trainingData.extend(trainingInfo[1])
        return  [trainDataLabel,trainingData]

    @staticmethod
    def evaluateGaussianNaiveBayes(X, Y, printReport=False):
        time = datetime.datetime.now()
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        clf = MultinomialNB()
        clf.fit(X_train, Y_train)
        if printReport:
            print 'Training time:' + str(datetime.datetime.now() - time)
            print 'Evaluation result: GaussianNaiveBayes: ' + str(clf.score(X_test, Y_test))
        Y_test = clf.predict(X_test)
        if printReport:
            print '0: ' + str((Y_test == 0).sum())
            print '1: ' + str((Y_test == 1).sum())
            print '2: ' + str((Y_test == 2).sum())
        return [clf.score(X_test, Y_test), (Y_test == 1).sum(), clf]

    @staticmethod
    def evaluateOneVsRest(X, Y, printReport=False):
        time = datetime.datetime.now()
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        clf = OneVsRestClassifier(LinearSVC(random_state=0))
        clf.fit(X_train, Y_train)
        if printReport:
            print 'Training time:' + str(datetime.datetime.now() - time)
            print 'Evaluation result: OneVsRest: ' + str(clf.score(X_test, Y_test))
        Y_test = clf.predict(X_test)
        if printReport:
            print '0: ' + str((Y_test == 0).sum())
            print '1: ' + str((Y_test == 1).sum())
            print '2: ' + str((Y_test == 2).sum())
        return [clf.score(X_test, Y_test), (Y_test == 1).sum(), clf]

    @staticmethod
    def evaluateOutputCode(X, Y, printReport=False):
        time = datetime.datetime.now()
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        clf = OutputCodeClassifier(LinearSVC(random_state=0), code_size=2, random_state=0)
        clf.fit(X_train, Y_train)
        if printReport:
            print 'Training time:' + str(datetime.datetime.now() - time)
            print 'Evaluation result: OneVsOne: ' + str(clf.score(X_test, Y_test))
        Y_test = clf.predict(X_test)
        if printReport:
            print '0: ' + str((Y_test == 0).sum())
            print '1: ' + str((Y_test == 1).sum())
            print '2: ' + str((Y_test == 2).sum())
        return [clf.score(X_test, Y_test), (Y_test == 1).sum(), clf]

    @staticmethod
    def evaluateOneVsOne(X, Y, printReport=False):
        time = datetime.datetime.now()
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        clf = OneVsOneClassifier(LinearSVC(random_state=0))
        clf.fit(X_train, Y_train)
        if printReport:
            print 'Training time:' + str(datetime.datetime.now() - time)
            print 'Evaluation result: OutputCode: ' + str(clf.score(X_test, Y_test))
        Y_test = clf.predict(X_test)
        if printReport:
            print '0: ' + str((Y_test == 0).sum())
            print '1: ' + str((Y_test == 1).sum())
            print '2: ' + str((Y_test == 2).sum())
        return [clf.score(X_test, Y_test), (Y_test == 1).sum(), clf]

    @staticmethod
    def createParsingReport(testingSents):
        sentsForPrinting = [s for s in testingSents if len(s.vMWEs) >= 1]
        sentsForPrinting = sorted(sentsForPrinting, key=lambda Sentence: len(Sentence.vMWEs), reverse=True)
        if len(sentsForPrinting) - 30 > 0:
            random = randint(1, len(sentsForPrinting) - 30)
        else:
            random = 0
        printingPath = os.path.join(Evaluation.resultsPath, 'Parsing.md')
        staticParsingFile = codecs.open(printingPath, 'w', "utf-8")
        result = ''
        for sent in sentsForPrinting[random:random + 5]:
            result += str(sent)
        staticParsingFile.write(result)

        # Producing a long report
        printingPath = os.path.join(Evaluation.resultsPath, 'Parsing-long.md')
        staticParsingFile = codecs.open(printingPath, 'w', "utf-8")
        result = ''
        for sent in sentsForPrinting: #[random:random + 30]:
            result += sent.printSummary()
        staticParsingFile.write(result)

    @staticmethod
    def createStaticParsingReports(sents):
        sentsForPrinting = [s for s in sents if len(s.vMWEs) >= 2]
        sentsForPrinting = sorted(sentsForPrinting, key=lambda Sentence: len(Sentence.vMWEs), reverse=True)
        if len(sentsForPrinting) - 30 > 0:
            random = randint(1, len(sentsForPrinting) - 30)
        else:
            random = 0
        sentsForPrinting = sentsForPrinting[random:random + 5]
        printingPath = os.path.join(Evaluation.resultsPath, 'StaticParsing.md')
        staticParsingFile = codecs.open(printingPath, 'w', "utf-8")
        result = ''
        for sent in sentsForPrinting:
            result += str(sent)
        staticParsingFile.write(result)

reload(sys)
sys.setdefaultencoding('utf8')

# FTB = '/Users/hazemalsaied/Parseme/MWEIdSys/Corpora/fr_SPMRL/pred/conll/train/train.French.pred.conll'
corpusName = '/Users/hazemalsaied/Parseme/MWEIdSys/Corpora/sharedtask/FR'

Train.train(corpusName, binary=True, printReport=True)
