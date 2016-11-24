
## About
* This assignment performs equal-width and equal-frequency dicreatization  
* The experiments are run with 5 fold cross validation
* The results are produced by Scott-Knot Analysis

## Instruction to run
* download the zip
* go to code 7 folder in the terminal
* run command **python main.py**

## Result
```
iris.csv --------------------------------------

recall for :  iris.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,         freq ,    0.33  ,  0.89 (----------*    |              ), 0.00,  0.33,  0.89
   1 ,        width ,    0.44  ,  0.40 (        ------*|              ), 0.25,  0.44,  0.65
   1 ,           nb ,    0.56  ,  0.46 (        -------|--*           ), 0.25,  0.56,  0.71

false alarm for :  iris.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,         freq ,    0.59  ,  0.45 (           ----*              ), 0.50,  0.59,  0.95
   1 ,           nb ,    0.68  ,  0.22 (            ---|--*           ), 0.53,  0.68,  0.75
   1 ,        width ,    0.71  ,  0.24 (              -|----*         ), 0.56,  0.71,  0.80

Runtime
nb :  0.00396733283997  sec
freq :  0.00394268035889  sec
width :  0.00685381889343  sec
```
