from tableReader import Table
from sklearn.cluster import MiniBatchKMeans
import numpy as np
from sklearn.neighbors import KDTree
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics.pairwise import pairwise_distances_argmin
import warnings
from sk import rdivDemo
import time
from random import shuffle
warnings.filterwarnings("ignore")

def train_test(data, folds=5, index=0):
    l = len(data)
    test = []
    train = []
    
    for i in range(0, folds):
        if i == index:
            test = [data[x] for x in range(int(i * l / folds),int((i + 1) * l / folds))]
        else:
            for x in range(int(i * l / folds),int((i + 1) * l / folds)):
            	train.append(data[x])
    train_label = [x[-1] for x in train]
    test_label = [x[-1] for x in test]

    return train,test, train_label, test_label

def recall(predicted_labels, actuals, label):
	tp =0
	tn=0
	fn=0
	fp = 0
	for i,p in enumerate(predicted_labels):
		a = actuals[i]
		if( a== label):
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
	return float(tp)/(fn + tp+1)

def falseAlarm(predicted_labels, actuals, label):
	tp =0
	tn=0
	fn=0
	fp = 0
	for i,p in enumerate(predicted_labels):
		a = actuals[i]
		if( a== label):
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
	return float(fp)/(tn + fp +1)

def  MiniBatch(train,test):
	mb = MiniBatchKMeans(init='random',n_clusters=20, n_init=20,batch_size=20,compute_labels=True)
 	dtrain = [x[:-1] for x in train ]
 	dtest = [x[:-1] for x in test ]
 	mb.fit(dtrain)
	k_means_cluster_centers = np.sort(mb.cluster_centers_, axis=0)
	k_means_labels = mb.labels_ #pairwise_distances_argmin(dtrain, k_means_cluster_centers)
	predicted_clusters = mb.predict(dtest)

	labels ={}
	
	for i,value in enumerate(k_means_labels):
		if value in labels:
			indexes = labels[value]
			indexes.append(i)
			labels[value] = indexes
		else:
			labels[value] =[i]
	predicted_labels=[]
	for i,p in enumerate(predicted_clusters):
		train_elements_in_clusters = [dtrain[x] for x in labels[p]]
		predicted_row = pairwise_distances_argmin(dtest[i], train_elements_in_clusters ).tolist()
		predicted_labels.append(train[dtrain.index(train_elements_in_clusters[predicted_row[0]])][-1])

	return predicted_labels

def kdTree(train, test):
	dtrain = [x[:-1] for x in train ]
 	dtest = [x[:-1] for x in test ]
	t = KDTree(dtrain, leaf_size=2)
	distance, ind=t.query(dtest,k=1)
	predicted_labels=[train[index][-1] for x in ind for index in x]
	return predicted_labels

def naiveBayes(train, test, train_label, test_label):
	dtrain = [x[:-1] for x in train ]
 	dtest = [x[:-1] for x in test ]
	NB = GaussianNB()
	NB.fit(dtrain,train_label)
	predicted_labels = NB.predict(dtest)
	return predicted_labels

datasets = ['diabetes.csv','camel-1.0.csv']
for dataset in datasets:
	table = Table(dataset)
	# table.printFormat()

	table.addRow()
	# table.printFormat()
	recall_for_diff_algos={}
	recall_for_diff_algos['nb'] =['nb']
	recall_for_diff_algos['kdTree'] =['kdTree']
	recall_for_diff_algos['minibatch'] =['minibatch']
	fAlarm_for_diff_algos={}
	fAlarm_for_diff_algos['nb'] =['nb']
	fAlarm_for_diff_algos['kdTree'] =['kdTree']
	fAlarm_for_diff_algos['minibatch'] =['minibatch']
	
	nb_time = 0;
	minibatch_time = 0;
	kdTree_time = 0;

	for index in range(0,25):	
		#print table.rows
		if(index%5 ==0):
			shuffle(table.rows)
		

		train,test,train_label, test_label = train_test(table.rows,5, index%5)
		# print  "length of test ", len(test)
		# print  "length of train ", len(train)
		# print  "length of test ", len(test_label)
		# print  "length of test ", len(train_label)
		# print "length of rows",len(table.rows)

		start_time = time.time()
		predicted_labels = MiniBatch(train,test)
		minibatch_time += (time.time() - start_time)
		recall_for_diff_algos['minibatch'].append(recall(predicted_labels,test_label,0))
		fAlarm_for_diff_algos['minibatch'].append(falseAlarm(predicted_labels,test_label, 0))
		
		start_time = time.time()
		predicted_labels = kdTree(train,test)
		# print(predicted_labels)
		# print(test_label)
		kdTree_time += (time.time() - start_time)
		recall_for_diff_algos['kdTree'].append(recall(predicted_labels,test_label,0))
		fAlarm_for_diff_algos['kdTree'].append(falseAlarm(predicted_labels,test_label, 0))

		start_time = time.time()
		predicted_labels = naiveBayes(train,test, train_label, test_label)
		nb_time += (time.time() - start_time)
		recall_for_diff_algos['nb'].append(recall(predicted_labels,test_label,0))
		fAlarm_for_diff_algos['nb'].append(falseAlarm(predicted_labels,test_label, 0))
		

	print dataset,"--------------------------------------"
	print  ""
	print "recall for : ", dataset
	print (rdivDemo(recall_for_diff_algos.values()))
	print "false alarm for : ", dataset
	print (rdivDemo(fAlarm_for_diff_algos.values()))
	print "Runtime"
	print "nb : ", nb_time/5, " sec";
	print "minibatch : ", minibatch_time/5, " sec";
	print "kdTree : ", kdTree_time/5, " sec";
	print  ""
	# print fAlarm_for_diff_algos
	# print recall_for_diff_algos
