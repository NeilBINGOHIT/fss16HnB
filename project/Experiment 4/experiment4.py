from tableReader import Table
from sk import rdivDemo
from random import shuffle
from time import time

import numpy as np
import entropy as en
import operator
from math import log
from sklearn.model_selection import StratifiedKFold

from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import neighbors

from imblearn.over_sampling import SMOTE
import copy

import warnings
warnings.filterwarnings("ignore")

# calculates recall of class variable from predicted list and actual list
def recall(predicted_labels, actuals, class_var):
	tp =0
	tn=0
	fn=0
	fp = 0
	for i,p in enumerate(predicted_labels):
		a = actuals[i]
		if( a == class_var):
			if(a == p):
				tp +=1
			else:
				fn +=1
		else:
			if(a == p):
				tn +=1
			else:
				fp +=1
				# recall = true positive / (false negative + true positive)
	return float(tp)/(fn + tp)

# calculates false alarm of class variable from predicted list and actual list
def falseAlarm(predicted_labels, actuals, class_var):
	tp =0
	tn=0
	fn=0
	fp = 0
	for i,p in enumerate(predicted_labels):
		a = actuals[i]
		if(a == class_var):
			if(a == p):
				tp +=1
			else:
				fn +=1
		else:
			if(a == p):
				tn +=1
			else:
				fp +=1
				# false alarm = false positive / (true negative + false positive)
	return float(fp)/(tn + fp)

# learners
def naiveBayes(train, train_label, test):
	model = GaussianNB()
	model.fit (train, train_label)
	# print model
	predicted = model.predict (test)
	return predicted

def supportVectorMachine(train, train_label, test):
	# model = SVC (kernel='linear')
	model = SVC()
	model.fit(train, train_label)
	# print model
	predicted = model.predict(test)
	return predicted

def randomForest(train, train_label, test):
	model = RandomForestClassifier(criterion='entropy')
	model.fit(train, train_label)
	# print model
	predicted = model.predict(test)
	return predicted

def classificationAndRegressionTrees(train, train_label, test):
	model = DecisionTreeClassifier(criterion='entropy')
	model.fit(train, train_label)
	# print model
	predicted = model.predict(test)
	return predicted

def linearRegression(train, train_label, test):
	model = LogisticRegression()
	model.fit(train, train_label)
	# print model
	predicted = model.predict(test)
	return predicted 

def kNearestNeighbour(train, train_label, test):
	model = neighbors.KNeighborsClassifier(n_neighbors=5)
	model.fit(train, train_label)
	predicted = model.predict(test)
	return predicted

def log_filtering(table):
	# transform only numberic
	min_val = 0.000001
	for i,row in enumerate(table.rows):
		for col in xrange(0, len(table.cols) - 1):
			if (row[col] <= min_val):
				row[col] = log(min_val)
			else:
				row[col] = log(row[col])

	return table

def overallEnt(a, totalRec):
	entropyOverall = 0.0
	for item in a:
		entroCur = item[0]
		fracOfRec = len(item[1])/float(totalRec)
		entropyOverall = entropyOverall + entroCur*fracOfRec
	return entropyOverall

def performSMOTE(train, train_label, algo):
	# using SMOTE to perform oversampling of minor class
	sm = SMOTE (kind = algo)
	train, train_label = sm.fit_sample([x for x in train], [y for y in train_label])
	train, train_label = train.tolist(), train_label.tolist()
	return train, train_label

with open("dataset.txt") as f:
	DATASETS = f.readlines()
DATASETS = [x.strip('\n') for x in DATASETS]
# DATASETS = ['pc1.csv']

M = 10
N = 10
LEARNERS = ['NB', 'KNN', 'SVM', 'RF', 'CART', 'LR']
METHODS = {'NB':naiveBayes, 'KNN':kNearestNeighbour, 'SVM':supportVectorMachine, 'RF':randomForest, 'CART':classificationAndRegressionTrees, 'LR':linearRegression}
BESTK = {'NB', 'KNN', 'SVM', 'RF', 'CART', 'LR'}

def main_code():
	
	for dataset in DATASETS:
		
		print ""
		print dataset

		table = Table (dataset)
		table.addRow()
		# TODO : convert arff to csv and 
		columns = table.headers[:-1]
		# table.printFormat()

		# sanity check on dataset
		# throw error if there is string value in the dataset after removing string columns and converting class variable to 1/0

		# LOG FILTERING
		table = log_filtering(table)
		
		# FEATURE SELECTION
		entropyDict = {}
		for i,col in enumerate(columns):
			lst = [(row[i], row[-1]) for row in table.rows]
			d = en.ediv(lst)
			entropyDict[col] = overallEnt(d, len(table.rows))


		top_ranked_attributes = dict(sorted(entropyDict.items(), key=operator.itemgetter(1))[:3])
		temp_required = [table.headers.index(col) for col in top_ranked_attributes.keys()]
		temp_required.append(len(table.cols)-1)

	  	# LIST OF COLUMN NUMBER TO BE REMOVED
		temp = range(len(table.cols))
		new_list = [col for col in temp if col not in temp_required]

		# REMOVE COLUMNS
		table.rows = np.array(table.rows)
		table.rows = np.delete(table.rows, tuple(new_list), 1)

		table.rows = table.rows.tolist()
		for row in table.rows:
			row[-1] = int(row[-1])
			
		# DATA INITIALIZATION
		RECALL = {'NB':['NB'], 'KNN':['KNN'], 'SVM':['SVM'], 'RF':['RF'], 'CART':['CART'], 'LR':['LR']}
		FALSE_ALARM = {'NB':['NB'], 'KNN':['KNN'], 'SVM':['SVM'], 'RF':['RF'], 'CART':['CART'], 'LR':['LR'] }
		TIME = {'NB':0, 'KNN':0, 'SVM':0, 'RF':0, 'CART':0, 'LR':0}


		for index in range(M):
			
			shuffle (table.rows)
			
			X = np.array([x[:-1] for x in table.rows])
			y = np.array([x[-1] for x in table.rows])
			skf = StratifiedKFold(n_splits=N, random_state=None, shuffle=True)
			
			for train_index, test_index in skf.split(X, y):
				train, test = X[train_index], X[test_index]
				train_label, test_label = y[train_index], y[test_index]

				# SMOTE TRAINING SET
				train, train_label = performSMOTE(train, train_label, "regular")

				for learner in LEARNERS:
					# RUN LEARNER
					start = time()
					predicted = METHODS[learner] (train, train_label, test)
					TIME[learner] += (time() - start)
					RECALL[learner].append (recall (predicted, test_label, 1))
					FALSE_ALARM[learner].append (falseAlarm (predicted, test_label, 1))


		print ""
		print "RECALL FOR : ", dataset
		print rdivDemo(RECALL.values())
		print ""
		print "FALSE ALARM : ", dataset
		print rdivDemo(FALSE_ALARM.values())
		print ""
		print "RUNTIME"
		print TIME
		print ""

if __name__ == '__main__':
	main_code()