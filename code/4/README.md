## About
* This assignment compares the recal, false alarm and runtime of different learners (knn, minibatch k-means, and kdtrees)
* The experiments are run with 5 fold cross validation
* The results are produced by Scott-Knot Analysis

## Instruction to run
* download the zip
* go to code 4 folder in the terminal
* run command **python main.py**

## Results

```
diabetes.csv --------------------------------------

recall for :  diabetes.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    minibatch ,    0.51  ,  0.13 (       ----*   |              ), 0.47,  0.51,  0.59
   1 ,          knn ,    0.52  ,  0.06 (          --*  |              ), 0.49,  0.52,  0.56
   1 ,       kdTree ,    0.53  ,  0.12 (      -------* |              ), 0.45,  0.53,  0.57

false alarm for :  diabetes.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,          knn ,    0.20  ,  0.04 (       --*     |              ), 0.19,  0.20,  0.22
   2 ,       kdTree ,    0.24  ,  0.05 (           ----*              ), 0.21,  0.24,  0.26
   2 ,    minibatch ,    0.24  ,  0.05 (             --|*             ), 0.22,  0.24,  0.27

Runtime
knn :  8.37736868858 sec
minibatch :  0.463464355469 sec
kdTree :  0.0218190193176 sec

ivy-2.0.csv --------------------------------------

recall for :  ivy-2.0.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,    minibatch ,    0.11  ,  0.20 (-----*         |              ), 0.00,  0.11,  0.20
   1 ,       kdTree ,    0.11  ,  0.20 (-----*         |              ), 0.00,  0.11,  0.20
   1 ,          knn ,    0.17  ,  0.29 (--------*      |              ), 0.00,  0.17,  0.29


false alarm for :  ivy-2.0.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,          knn ,    0.11  ,  0.06 (     ----*     |              ), 0.08,  0.11,  0.14
   1 ,       kdTree ,    0.11  ,  0.04 (       ---*    |              ), 0.09,  0.11,  0.14
   1 ,    minibatch ,    0.12  ,  0.04 (       ----*   |              ), 0.10,  0.12,  0.14

Runtime
knn :  3.51418147087 sec
minibatch :  0.261498594284 sec
kdTree :  0.00960593223572 sec
```
