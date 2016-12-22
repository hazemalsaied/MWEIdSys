import os

from sklearn import svm
from sklearn.feature_extraction import DictVectorizer

from corpus import Corpus
from parser import Parser


class Train:
    @staticmethod
    def train(corpusName):
        corpus = Corpus(os.path.join(os.path.dirname(__file__), corpusName))
        trainingData = []
        trainingDataLebels = []
        for sent in corpus.sentences:
            # Parse the sentence
            trainingInfo = Parser.staticParse(sent, binary=True)
            trainingDataLebels.extend(trainingInfo[0])
            trainingData.extend(trainingInfo[1])
        # trainingDataLebels = array(trainingDataLebels)
        svc = svm.SVC()
        vec = DictVectorizer()
        vec.transform(trainingData)
        # print len(svc.get_feature_names())
        # print vec.get_feature_names()
        svc.fit(trainingData, trainingDataLebels)


Train.train('/Users/hazemalsaied/Parseme/MWEIdSys/Corpora/corpus.txt')
