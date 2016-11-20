## About
* This assignment compares the recal, false alarm and runtime of naive bayes with other learners 
* The experiments are run with 5 fold cross validation
* The results are produced by Scott-Knot Analysis

## Instruction to run
* download the zip
* go to code 5 folder in the terminal
* run command **python main.py**

## Result
```
diabetes.csv --------------------------------------

recall for :  diabetes.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,       kdTree ,    0.75  ,  0.03 (         --*   |              ), 0.73,  0.75,  0.76
   1 ,    minibatch ,    0.76  ,  0.05 (        ----*  |              ), 0.73,  0.76,  0.78
   2 ,           nb ,    0.82  ,  0.05 (               |  --*         ), 0.81,  0.82,  0.85

false alarm for :  diabetes.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,           nb ,    0.39  ,  0.10 (        -----* |              ), 0.34,  0.39,  0.44
   2 ,       kdTree ,    0.46  ,  0.04 (               |---*          ), 0.43,  0.46,  0.47
   2 ,    minibatch ,    0.47  ,  0.07 (               |---*          ), 0.43,  0.47,  0.50

Runtime
nb :  0.00969080924988  sec
minibatch :  0.418505382538  sec
kdTree :  0.0179957866669  sec

camel-1.0.csv --------------------------------------

recall for :  camel-1.0.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,           nb ,    0.91  ,  0.04 (            ---*              ), 0.90,  0.91,  0.94
   2 ,    minibatch ,    0.96  ,  0.02 (               |       -*     ), 0.95,  0.96,  0.97
   2 ,       kdTree ,    0.96  ,  0.04 (               |     ---*     ), 0.94,  0.96,  0.98

false alarm for :  camel-1.0.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,           nb ,    0.50  ,  0.42 (        -------|-*            ), 0.25,  0.50,  0.67
   2 ,    minibatch ,    0.67  ,  0.25 (               | ------*      ), 0.50,  0.67,  0.75
   2 ,       kdTree ,    0.67  ,  0.25 (               | ------*      ), 0.50,  0.67,  0.75

Runtime
nb :  0.0107860565186  sec
minibatch :  0.293381500244  sec
kdTree :  0.014032793045  sec
```
The above timings shows that naive bayes is faster than other learners
