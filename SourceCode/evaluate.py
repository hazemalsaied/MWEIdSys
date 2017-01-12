from __future__ import division

import os


class Evaluation:
    resultsPath = '/Users/hazemalsaied/Parseme/MWEIdSys/Results/'

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
        if nubCorrectExpectedAnn == 0 or nubFoundAnn == 0:
            print 'Evaluation Failed: Zero values'
            return
        recall = nubCorrectFoundAnn / nubCorrectExpectedAnn
        precision = nubCorrectFoundAnn / nubFoundAnn
        fScore = 2 * (recall * precision) / (recall + precision)

        if printReport:
            report = '## Exact Identification Evaluation: ' + '\n'
            report += '####Recall: ' + str(recall) + '\n'
            report += '####Precision: ' + str(precision) + '\n'
            report += '####F-Score: ' + str(fScore) + '\n'
            printingPath = os.path.join(Evaluation.resultsPath, 'Readme.md')
            staticParsingFile = open(printingPath, 'a')
            staticParsingFile.write(report)

        print 'Recall: ' + str(recall)
        print 'Precision: ' + str(precision)
        print 'F-Score: ' + str(fScore)

