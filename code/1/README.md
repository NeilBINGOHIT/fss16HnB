# HW1

---
###eg0
eg0 first prints the five attributes of the dataset. Then it prints the content which is formatted with proper spaces for a better view and which follows the alphabetical order of the attribute *outlook*. The most important work of eg0 is running a decision tree learner algorithm j48 with 10-fold cross validation on the data weather.arff. Therefore, a decision tree is given at last.

###eg1
eg1 simply does a part of eg0's work which is formatted with proper spaces for a better view and which follows the alphabetical order of the attribute *outlook*.

###eg2
eg2 gives all the process of j4810 which runs j48 decision tree learner on the dataset `data/weather.arff` with 10-fold cross validation. eg2 also gives the line number of the output. It gives information like the structure of J48 pruned tree, error on training data, detailed ccuracy by class, confusion matrix and stratified cross-validation, etc. 

###eg3
eg2 shows the result of calling a decision tree learner j48 with the same training and testing data. It prints out details on each test instance with the line numbers. We can notice that the all the predictions are right because of the same training and testing data.

###eg4
eg4 prints the actual and predicted values from each instance with the `wantgot()` function to give a formatted result.

###eg5
eg5 uses the results of eg4 and runs the python script abcd.py on them. {a, b, c, d} denotes the true negatives, false negatives, false positives, and true positives (reespectively) found by a binary detector. eg5 summerizes the results from eg4 inro precision and shows 100% accuracy on both *no* and *yes* classes because we use the same training and testing data(in eg3).

###eg6
eg6 runs `crossval` (cross-validation) that 1 time, divides the data into 3 bins, then trains on two of them and tests on the other third. The fild ends with a list of learners (here are `j48` and `jrip`) to try. It produces infomation like eg5 but with two groups for j48 and jrip. It is stratified cross-validation because each fold in the output contains roughly the same proportions of the two types of class labels.

###eg7
eg7 runs a 5*5 cross-validation with two learners, j48 and jrip, saves the result to `$out`. Then eg7 runs `gawk` to get the information in #2(learner), #10(pd) and #11(pf) column from the stored file to seperated .pd and .pf files.

###eg8
eg8 does similar work as eg7 but uses named columns which is a better way to indicate and locate the column than numbers, to print the result which is the same as eg7's result.

###eg9
eg9 runs `stats.py` script with the output of eg8 to show the distrubution of `j48`'s `pd` and its `pf` values. The advantage of separating the reporting of a data mining run is that this structure is much better in such senario like we run data mining in HPC or other high power servers and get the visualized data in our local machine. Data mining is time and resource consuming, such structure will help make the work more efficient and keep the result safe.  

###eg10
eg10 uses the dataset `data/jedit-4.1.arff` to run the learners `j48`, `nb`, `rbfnet` and `bnet` with 5*5 cross-validation and store the results of `pd` and `pf` to `$i.pd` and `$i.pf` files. Then report the distribution of the values in the two files, just like what we did previously.

 1. `j48` (class name: J48) is a class for generating a pruned or unpruned C4.5 decision tree.
 2. `jrip` (class name: JRip) is a propositional rule learner, Repeated Incremental Pruning to Produce Error Reduction (RIPPER), which was proposed by William W. Cohen as an optimized version of IREP.
 

