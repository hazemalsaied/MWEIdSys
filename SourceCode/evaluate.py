from __future__ import division

class Evaluation:

    @staticmethod
    def evaluate(sents, printReport=False):
        nubCorrectExpectedAnn = 0
        nubFoundAnn = 0
        nubCorrectFoundAnn = 0

        for sent in sents:

            nubCorrectExpectedAnn += len(sent.vMWEs)
            nubFoundAnn += len(sent.identifiedVMWEs)
            mwesStrings = []
            for m in sent.vMWEs:
                mwesStrings.append(m.getString())
            for m in sent.identifiedVMWEs:
                if m.getString() in mwesStrings:
                    nubCorrectFoundAnn += 1
        recall = nubCorrectFoundAnn / nubCorrectExpectedAnn
        precision = nubCorrectFoundAnn / nubFoundAnn
        fScore = 2 * (recall * precision) / (recall + precision)
        if printReport:
            print 'Recall: ' + str(recall)
            print 'Precision: ' + str(precision)
            print 'F-Score: ' + str(fScore)
