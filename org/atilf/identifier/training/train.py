import os
from org.atilf.identifier.resources.Corpus import Corpus
from org.atilf.identifier.oracle.StaticOracle import StaticOracle

class Train:

    @staticmethod
    def train(corpusName):
        corpus = Corpus(os.path.join(os.path.dirname(__file__),corpusName ))
        for sent in corpus.sentences:
            # Parse the sentence
            StaticOracle.parse(sent)
            # Generate the vector

Train.train('corpus.txt')