##Feature Selection

- All datasets are coming from Weka
- All classification is using Naive Bayes

##SubPart 1  - Feature selection using J48(M=2)

Steps
* Select the .arff file
* Go to classify - choose **NaiveBayes** and click on start
* Record the precision and recall values
* Go to select attributes tab  
   * Under **Attribute Evaluator** select **WrapperSubsetEval**
   * Edit the classifier as J48 with value of M = 2
* Mark the selected arrtributes; invert and remove the other attributes
* Go to classify - choose **NaiveBayes** and click on start
* Record the precision and recall values

| Datasets     | selected features / all features   | precision (selected/all) | recall (selected/all) |
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
|  credit-g.arff |  9 / 20 | 0.721 / 0.763 | 0.738 / 0.772 |
|  glass.arff | 5 / 9  | 0.550 / 0.564  | 0.547 / 0.556 |
|  iris.arff | 1 / 4 | 0.960 / 0.960 | 0.960 / 0.960 |
|  ionosphere.arff | 5 / 34  | 0.854 / 0.844  | 0.855 / 0.829 |
|  labor.arff | 6 / 16 | 0.912 / 0.983 | 0.912 / 0.982 |
|  vote.arff | 5 / 16 | 0.931 / 0.907 | 0.931 / 0.903 |

##SubPart 2 - Wrapper feature selection 
- classifier subset eval and classifier used is NB (selected features/all features)

| Datasets     | selected features / all features | precision (selected/all) | recall (selected/all) |
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
|  credit-g.arff |  5 / 8 | 0. / 0. | 0. / 0. |
|  glass.arff | 6 / 9  | 0. / 0.  | 0. / 0. |
|  iris.arff | 15 / 20 | 0. / 0. | 0. / 0. |
|  ionosphere.arff | 5 / 34  | 0. / 0.  | 0. / 0. |
|  labor.arff | 3 / 16 | 0. / 0. | 0. / 0. |
|  vote.arff | 3 / 4 | 0. / 0. | 0. / 0. |

##SubPart 3 - Filter feature selection 
- infogain  (selected features/all features)

| Datasets     | selected features / all features | precision (selected/all) | recall (selected/all) |
| ------------- |:-------------:|:-------------:|:-------------:|:-------------:|
|  credit-g.arff |  5 / 8 | 0. / 0. | 0. / 0. |
|  glass.arff | 6 / 9  | 0. / 0.  | 0. / 0. |
|  iris.arff | 15 / 20 | 0. / 0. | 0. / 0. |
|  ionosphere.arff | 5 / 34  | 0. / 0.  | 0. / 0. |
|  labor.arff | 3 / 16 | 0. / 0. | 0. / 0. |
|  vote.arff | 3 / 4 | 0. / 0. | 0. / 0. |
