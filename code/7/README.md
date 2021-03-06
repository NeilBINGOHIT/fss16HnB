
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

diabetes.csv --------------------------------------

recall for :  diabetes.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,        width ,    0.37  ,  0.11 (      --*      |              ), 0.34,  0.37,  0.45
   1 ,           nb ,    0.37  ,  0.11 (      --*      |              ), 0.34,  0.37,  0.45
   1 ,         freq ,    0.40  ,  0.09 (        ---*   |              ), 0.37,  0.40,  0.46
false alarm for :  diabetes.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,        width ,    0.13  ,  0.03 (     ---*      |              ), 0.11,  0.13,  0.15
   1 ,           nb ,    0.13  ,  0.03 (     ---*      |              ), 0.11,  0.13,  0.15
   1 ,         freq ,    0.14  ,  0.04 (       --*     |              ), 0.12,  0.14,  0.16

Runtime
nb :  0.0158552646637  sec
freq :  0.0137827396393  sec
width :  0.0150231361389  sec

camel-1.0.csv --------------------------------------

recall for :  camel-1.0.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,        width ,    0.91  ,  0.04 (               |          -*  ), 0.90,  0.91,  0.94
   1 ,           nb ,    0.91  ,  0.04 (               |          -*  ), 0.90,  0.91,  0.94
   1 ,         freq ,    0.91  ,  0.07 (               |         --*  ), 0.88,  0.91,  0.94

false alarm for :  camel-1.0.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,        width ,    0.50  ,  0.47 (       --------|--*           ), 0.20,  0.50,  0.67
   1 ,           nb ,    0.50  ,  0.47 (       --------|--*           ), 0.20,  0.50,  0.67
   1 ,         freq ,    0.50  ,  0.25 (         ------|--*           ), 0.25,  0.50,  0.50

Runtime
nb :  0.0085470199585  sec
freq :  0.0120255470276  sec
width :  0.0155718326569  sec

arc.csv --------------------------------------

recall for :  arc.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,           nb ,    0.23  ,  0.14 (    ----*      |              ), 0.13,  0.23,  0.27
   1 ,        width ,    0.23  ,  0.14 (    ----*      |              ), 0.13,  0.23,  0.27
   1 ,         freq ,    0.27  ,  0.23 (   -------*    |              ), 0.11,  0.27,  0.34

false alarm for :  arc.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,        width ,    0.55  ,  0.17 (               |--*           ), 0.50,  0.55,  0.67
   1 ,           nb ,    0.56  ,  0.29 (              -|--*           ), 0.43,  0.56,  0.71
   1 ,         freq ,    0.67  ,  0.25 (               |------*       ), 0.50,  0.67,  0.75

Runtime
nb :  0.0103500843048  sec
freq :  0.0197681427002  sec
width :  0.00893540382385  sec

ivy-2.0.csv --------------------------------------

recall for :  ivy-2.0.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,           nb ,    0.78  ,  0.13 (               |   ----*      ), 0.72,  0.78,  0.85
   1 ,         freq ,    0.80  ,  0.20 (               |-------*      ), 0.66,  0.80,  0.85
   1 ,        width ,    0.80  ,  0.13 (               |   ----*      ), 0.70,  0.80,  0.84

false alarm for :  ivy-2.0.csv

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,         freq ,    0.60  ,  0.28 (          -----*              ), 0.50,  0.60,  0.78
   1 ,        width ,    0.67  ,  0.12 (               |--*           ), 0.62,  0.67,  0.75
   1 ,           nb ,    0.67  ,  0.12 (             --|--*           ), 0.57,  0.67,  0.69

Runtime
nb :  0.0145550251007  sec
freq :  0.00977435112  sec
width :  0.0157612323761  sec

```
The above results show that discreatization rarely hurt NB (which is consistent with Doughery et al. result)
