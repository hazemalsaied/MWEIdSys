import datetime

import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OutputCodeClassifier, OneVsRestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

from corpus import SPMLRCorpus
from evaluate import Evaluation
from parser import Parser


class Train:
    @staticmethod
    def train(corpusName, binary=False, printReport=False):
        time = datetime.datetime.now()
        corpus = SPMLRCorpus(corpusName, printReport=printReport)
        # corpus = Corpus(os.path.join(os.path.dirname(__file__), corpusName),printReport=printReport)

        sentenceNum = int(len(corpus.sentences) * 0.8)
        trainingSents = corpus.sentences[0:sentenceNum]
        testingSents = corpus.sentences[sentenceNum + 1:]

        cls = Train.classify(trainingSents, printReport=printReport, binary=binary)

        for sent in testingSents:
            Parser.parse(cls[0], cls[1], sent)
            print sent
        Evaluation.evaluate(testingSents, printReport=True)

    @staticmethod
    def classify(sents, printReport=False, binary=False):
        trainingData = []
        trainDataLabel = []
        time = datetime.datetime.now()
        for sent in sents:
            # Parse the sentence
            trainingInfo = Parser.staticParse(sent, printReport=printReport, binary=binary)
            trainDataLabel.extend(trainingInfo[0])
            trainingData.extend(trainingInfo[1])
        print 'Static parsing duration: ' + str(datetime.datetime.now() - time)
        vec = DictVectorizer()
        X = vec.fit_transform(trainingData)
        Y = np.asarray(trainDataLabel)
        # F = vec.get_feature_names()
        time = datetime.datetime.now()

        clf = MultinomialNB()
        # #clf = OutputCodeClassifier(LinearSVC(random_state=0), code_size=2, random_state=0)
        #clf = OneVsOneClassifier(LinearSVC(random_state=0))
        #clf = OneVsRestClassifier(LinearSVC(random_state=0))
        clf.fit(X, Y)
        # svc.fit(X_train, Y_train)
        # svc.fit(X, Y)
        print 'Training classifier duration: ' + str(datetime.datetime.now() - time)
        return [clf, vec]

    @staticmethod
    def evaluateClassifiers(corpusName, printReport=True):

        corpus = SPMLRCorpus(corpusName, printReport=printReport)
        vectors = Train.vectorizeSents(corpus.sentences, printReport=printReport)
        X = vectors[0]
        Y = vectors[1]
        Train.evaluateOneVsRest(X, Y, printReport=printReport)
        Train.evaluateOutputCode(X, Y, printReport=printReport)
        Train.evaluateOneVsOne(X, Y, printReport=printReport)
        # Train.evaluateSVMOVR(X, Y, printReport=printReport)
        Train.evaluateGaussianNaiveBayes(X, Y, printReport=printReport)

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

    # @staticmethod
    # def evaluateSVMOVR(X, Y, printReport=False):
    #     time = datetime.datetime.now()
    #     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    #     clf = svm.SVC(decision_function_shape='ovr')
    #     clf.fit(X_train, Y_train)
    #     if printReport:
    #         print 'Training time:' + str(datetime.datetime.now() - time)
    #         print 'Evaluation result: SVM-OVR: ' + str(clf.score(X_test, Y_test))
    #     Y_test = clf.predict(X_test)
    #     if printReport:
    #         print '0: ' + str((Y_test == 0).sum())
    #         print '1: ' + str((Y_test == 1).sum())
    #         print '2: ' + str((Y_test == 2).sum())

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

    @staticmethod
    def vectorizeSents(sents, printReport=False):

        trainingData = []
        trainingDataLebels = []
        for sent in sents:
            trainingInfo = Parser.staticParse(sent, printReport=printReport)
            trainingDataLebels.extend(trainingInfo[0])
            trainingData.extend(trainingInfo[1])
        vec = DictVectorizer()
        X = vec.fit_transform(trainingData)
        Y = np.asarray(trainingDataLebels)
        F = vec.get_feature_names()
        if printReport:
            print 'The dimensions of vectors matrix:' + str(X.shape)
        return [X, Y]


# corpusName = '/Users/hazemalsaied/Parseme/MWEIdSys/Corpora/corpus.txt'

corpusName = '/Users/hazemalsaied/Parseme/MWEIdSys/Corpora/fr_SPMRL/pred/conll/train/train.French.pred.conll'

# Train.evaluateClassifiers(corpusName)
Train.train(corpusName,printReport=False)
