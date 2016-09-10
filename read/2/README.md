###Paper
An Empirical Investigation into the Role of API-Level Refactorings during Software Evolution, by Miryung Kim, Dongxiang Cai and Sunghun Kim, presented in 33rd International Conference on Software Engineering (ICSE), 2011.

###Summary
Refactoring is the process of changing a programs’ design structure without modifying its external functional behavior in order to improve program readability, maintainability and extensibility. 

Relevant studies show different results between refactoring and following bug fixes. 

The goal of this paper is to systematically investigate the role of refactorings during the software evolution by examining the relationships between refactorings, bug fixes, the time to resolve bugs and release cycles using fine-grained version histories.

###Keywords
1. API – level Refactoring  
API-Level refactoring are rename refactorings at the level of packages/classes/methods, add/delete parameter refactorings, move refactoring at the level of packages/classes/methods and changes to the return type of a method.

2. Floss Refactoring  
There are two different occasions when programmers refactor. The first kind occurs interweaved with normal program development, arising whenever and wherever design problems arise. For example, if a programmer introduces (or is about to introduce) duplication when adding a feature, then the programmer removes that duplication. This kind of refactoring, done frequently to maintain healthy software, is called [floss refactoring](http://people.engr.ncsu.edu/ermurph3/papers/wrt07.pdf).

3. Change Distilling  
It is a tree differencing algorithm for fine-grained source code change extraction. It was published in [IEEE transactions to Software Engineering](http://dl.acm.org/citation.cfm?id=1314081). 

4. Hunks  
List of consecutive source code lines that were added or deleted. 

###Features
1.	Motivational Statement  
In theory, refactoring improves software quality and programmers’ productivity. However, in practice there are trends that show increase in bug reports after refactoring. This motivates the authors to dig deeper and systematically investigate the role of refactoring. The idea is to study and establish a relationship between refactorings, bug fixes, the time to resolve bugs and release cycles.

2.	Related Work  
Weissgerber and Diehl found that a high ratio of refactorings is sometimes followed by an increasing ratio of bug reports. In contradiction, Ratzinger et al. found that the number of defects decreases if the number of refactorings increases in the preceding time period. Dig et al. found that 80% of the changes that break client applications are API-level refactorings. Another study showed that large commits, which tend to include refactorings, have a higher chance of including bugs. Moreover, studies have also shown that there are many bugs in refactoring tools and these tools do a poor job of communicating errors. All these relate to the outcome of the empirical investigation of the authors.

3.	Hypotheses  
The authors focused their efforts to answer the following questions from the gathered data
 * Are there more bug fixes after API-level refactorings? 
 * Do API-level refactorings improve developer productivity? 
 * Do API-level refactoring facilitate bug fixes? 
 * Are there relatively fewer API-level refactorings before major releases? 

4.	Study Instruments and Commentary  
The author’s applied M. Kim et al.’s refactorings reconstruction technique to find revisions that underwent refactoring and S. Kim et al.’s bug history extraction technique to identify bug fix revisions. The refactorings are used for this study are from change logs of Eclipse JDT, jEdit and Columba.

5.	Results  
Results of relationship between refactorings and bug reports include in-depth knowledge regarding the following questions
 * Are there more bug fixes after API-level refactorings? Yes, there is a short-term increase in the number of bug fixes after refactorings.
 * Do API-level refactorings improve developer productivity? Yes, when it comes to fixing bugs introduced near the time of refactorings, the average fix time tends to decrease after refactorings.
 * Do API-level refactoring facilitate bug fixes? Yes, Fixes and refactoring often appear in the same revision. Furthermore, it is more likely for a refactoring revision to be followed by related bug fixes than for a non-refactoring revision.
 * Are there relatively fewer API-level refactorings before major releases? No, there are more refactorings and bug fixes prior to major version release.

###Improvements

1.	Generalization of results  
The authors have closely studied API-level refactorings but in their results they have generalized these to normal refactorings. To a reader perusing the results, it might mislead to believe that general refactorings have the same trend as API-level refactorings.

2.	Results and type of refactorings  
The results generated talk about API-level refactorings and its trends with bug-fixes and release cycles. It would have been more interesting to know what type of refactorings, manual or automatic, conform to these results.

3.	Excluding Software Life Cycle Activity  
The authors did not take into account the fact that their subject might practice the activity of refactoring the code before a major release. This fact might skew the last result. 
