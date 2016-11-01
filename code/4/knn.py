from __future__ import division
import sys
import math
import tableReader
import random
import operator

class KNN:
    def __init__(self, table, k):
        self.table = table
        self.k = k

    def knn(self, trainingSet, testInstance):
        dists = []
        for x in range(len(trainingSet)):
            dist = self.table.distance(testInstance, trainingSet[x])
            dists.append((trainingSet[x], dist))
        dists.sort(key = operator.itemgetter(1))
        neighbors = []
        for x in range(self.k):
            neighbors.append(dists[x][0])
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.iteritems(), key = operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]
        

trainData = tableReader.Table(sys.argv[2])
trainData.addRow()
testData = tableReader.Table(sys.argv[3])
testData.addRow()
knnLearner = KNN(trainData,1)
prediction = []
for row in testData.rows:
    prediction.append(knnLearner.knn(trainData.rows, row))
print prediction