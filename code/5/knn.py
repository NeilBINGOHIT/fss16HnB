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
        


# Mini-Batch kmeans
class MBKmeans:
    # k = 20 centers
    # paras: k, mini-batch size b, iterations t, data set x
    def __init__(self, k, b, x):
        self.clusters = None 
        
    def kmeans(self, t):
        if self.cluster is None:
            self.clusters = tableReader.Table(dataFile)
            self.clusters = 

class KDTree:
    def __init__(self, k):
        self.k = k



table = tableReader.Table('weather.csv')
table.addRow()
testLearner = KNN(table,1)
prediction = []
for row in table.rows:
    prediction.append(testLearner.knn(table.rows, row))
print prediction