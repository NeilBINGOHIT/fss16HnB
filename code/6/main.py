from tableReader import Table
from sklearn.cluster import MiniBatchKMeans
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics.pairwise import pairwise_distances_argmin
import warnings
from sk import rdivDemo
import time
import random
import math
warnings.filterwarnings("ignore")


list1 = list2 = []
a12Score = olda12Score = 0
datasets = ['iris.csv']

def recall(predicted_labels, actuals, label):
	tp =0
	tn=0
	fn=0
	fp = 0
	for i,p in enumerate(predicted_labels):
		a = actuals[i]
		if( a == label):
			if(a == p):
				tp +=1
			else:
				fn +=1
		else:
			if(a ==p):
				tn +=1
			else:
				fp +=1
				# false alarm = false positive / (true negative + false positive)
				# recall = true positive / (false negative + true positive)
	return float(tp)/(fn + tp + 1)


def naiveBayes(train, test):
	dtrain, ltrain = [x[:-1] for x in train ], [x[-1] for x in train]
 	dtest = [x[:-1] for x in test ]
	NB = GaussianNB()
	NB.fit(dtrain,ltrain)
	predicted_labels = NB.predict(dtest)
	return predicted_labels

def a12(list1, list2):
    more = same = 0.0
    for x in sorted(list1):
        for y in sorted(list2):
            if x == y:
                same += 1
            elif x > y:
                more += 1
    return (more + 0.5*same) / (len(list1)*len(list2))

def print_era(predicted_labels, test):
	global list1, list2, a12Score, olda12Score

	# print predicted_labels
	test_label = [x[-1] for x in test]
	recall_class_one = recall(predicted_labels,test_label,'Iris-setosa')
	recall_class_two = recall(predicted_labels,test_label,'Iris-versicolor')
	recall_class_three = recall(predicted_labels,test_label,'Iris-virginica')

	print "Class 1: " + str(recall_class_one)
	print "Class 2: " + str(recall_class_two)
	print "Class 3: " + str(recall_class_three)
	
	flag = 0
	if len(list1) == 0:
		list1 = [recall_class_one, recall_class_two, recall_class_three]
		list2 = list1
		flag = 1
	else:
		list1 = list2
		list2 = [recall_class_one, recall_class_two, recall_class_three]

	olda12Score = a12Score
	a12Score = a12(list1, list2)

	if flag == 0:
		print "A12 Score: " + str(a12Score)
		if math.fabs(olda12Score - a12Score) > 0.2 * olda12Score:
			print "Anamoly detected!!"
	print ""


for dataset in datasets:
	table = Table(dataset)

	table.addRow()
	# generate a total of 2000 rows in specifed order
	count = 0
	data_list = []

	for i,x in enumerate (table.rows):
		if i < 100:
			data_list.append(x)
		else:
			break
	data_list = data_list * 10

	class_a = table.rows[0:50] 
	class_b = table.rows[50:100]
	class_c = table.rows[100:150]

	for i in range (10):
		data_list += class_a[0:10] + class_b[0:30] + class_c[0:50] + class_c[0:10]
		random.shuffle(class_a)
		# not shuffling for better results
		# random.shuffle(class_b)
		# random.shuffle(class_c)

	# alternate logic
	
	# while count < 2000:
	# 	row = table.rows[random.randint(0, len(table.rows) - 1)]
        	
	# 	if row[-1] == 'Iris-setosa':
	# 		if class_one_round_one < 500:
	# 			class_one_round_one += 1
	# 			first_1000.append(row)
	# 			count += 1
	# 		elif class_one_round_two < 100:
	# 			class_one_round_two += 1
	# 			second_1000.append(row)
	# 			count += 1
	# 	elif row[-1] == 'Iris-versicolor':
	# 		if class_two_round_one < 500:
	# 			class_two_round_one += 1
	# 			first_1000.append(row)
	# 			count += 1
	# 		elif class_two_round_two < 300:
	# 			class_two_round_two += 1
	# 			second_1000.append(row)
	# 			count += 1
	# 	elif class_three_round_two < 600:
	# 			class_three_round_two += 1
	# 			second_1000.append(row)
	# 			count += 1

	# random.shuffle(first_1000)
	# for x in first_1000:
	# 	data_list.append(x)

	# # random.shuffle(second_1000)   	
	# for x in second_1000:
	# 	data_list.append(x)

	# for j in data_list:
	# 	print j
	# print len(data_list)

	print '***Era 1***'
	test_list = train_list = data_list[0 : 100]
	print_era (naiveBayes(train_list, test_list), test_list)

	for i in xrange(1, 20):
		print '***Era ' + str(i+1) + '***'
		train_list = data_list[0 : i * 100]
		test_list = data_list[i * 100 : (i+1) * 100] 

		print_era (naiveBayes(train_list, test_list), test_list)

		

