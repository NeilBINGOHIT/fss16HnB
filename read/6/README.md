###Paper 
[Learning to Rank Relevant Files for Bug Reports using Domain Knowledge] (http://dl.acm.org/citation.cfm?id=2635874), by Xin Ye, Razvan Bunescu and Chang Liu, proceedings of the 22nd ACM SIGSOFT International Symposium on Foundation of Software Engineering, 2014

###Summary
This paper introduces an adaptive ranking approach that leverages domain knowledge through functional decompositions of source code files into methods, API descriptions of library components used in the code, the bug-fixing history, and the code change history. Given a bug report, the ranking source of each file is computed as a weighted combination of an array of features encoding domain knowledge, where the weights are trained automatically on previously solved bug reports using a learning-to-rank technique. 

###Keywords
1.	Mean Average Precision  
It is a standard metric that is widely used in information retrieval. It is defined as the mean of the Average Precision (AvgP) values obtained for all the evaluation queries.

2.	Bug/defect  
A software bug or defect is a coding mistake that may cause unintended and unexpected behaviors of the software components.

3.	Vector Space Model ([VSM] (https://en.wikipedia.org/wiki/Vector_space_model))  
It is an algebraic model for representing text documents as vectors of identifiers such as index terms. It is used in information filtering, information retrieval, indexing and relevancy rankings. 

4.	Term Frequency (tf) – Inverse Document Frequency (idf)  
Term frequency factor tf(t,d) represents the number of occurrences of term *t* in document *d*. Document Frequency factor df(t) represents the number of documents in the repository that contain the term *t*. Inverse Document Frequency idf(t) is computed using a logarithm in order to dampen the effect of document frequency factor in the overall term weight. 

###Features
1.	Motivational Statement  
When a new bug report is received, developers usually need to reproduce the bug and perform code reviews to find the cause a process that can be tedious and time consuming. A large number of bug reports could be opened during a development lifecycle. For example, 3389 bug reports were created for the Eclipse Platform product in 2013 alone. A tool that helps the developer narrow down the search and lead to the source file containing the cause of the bug would lead to a substantial increase in productivity.

2.	Commentary   
A ranking model is defined to compute a matching score for any bug report *r* and source code file *s* combination. The scoring function *f(r, s)* is defined as a weighted sum of *k* features (k = 6) , where each feature *sigma(r, s)* measures a specific relationship between the source file *s* and the received bug report *r*

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/6/Figure%201.jpg" width="400">

   The user is presented with a ranked list of files, with the expectation that files appearing higher in the list are more likely to be relevant for the bug report. The model parameters *w* are trained on previously solved bug reports using a learning to rank technique. 

   The following are the 6 features
   * Surface lexical similarity (**equation 3 and 4**) – the input documents is tokenized using standard IR techniques (remove whitespaces, remove stop words, stem words using Porter stemmer). Since the source file is large, AST parser is used to segment the source code into methods in order to compute per-method similarities with the bug report.
   * API enriched Lexical similarity (**equation 5**) – This bridges the gap between the bug report (usually expressed in natural language) and source code file (written in programming language). This is achieved by the following: for each method, the authors extract a set of classes and interfaces names and using project API specification they obtain textual descriptions.
   *	Collaborative filtering score (**equation 6**) – This accounts for the following observation: a file that has been fixed before may be responsible for similar bugs.
   *	Class name Similarity (**equation 7**) – This accounts for the following: a bug report may directly mention a class name in the summary, which provides a useful signal that the corresponding source file implementing that class may be relevant for the bug report.
   *	Bug fixing recency (**equation 8**) – This feature is based on the fact that change history of the source code provides information that can help predict fault-prone files.
   *	Bug fixing frequency (**equation 9**) – This feature is based on the fact that a source file that has been frequently fixed may be a fault prone file. 
  *	Feature Scaling (**equation 10**) – This helps bring all the features to the same scale so that they become comparable with each other.

3.	Data  
The training /benchmark datasets were taken from 6 open-source projects: [AspectJ] (http://eclipse.org/aspectj/), [Birt] (https://www.eclipse.org/birt/), [Eclipse Platform UI] (http://projects.eclipse.org/projects/eclipse.platform.ui), [JDT] (http://www.eclipse.org/jdt/), [SWT] (http://www.eclipse.org/swt/), [Tomcat] (http://tomcat.apache.org). All these project use BugZilla as their issues tracking system and GIT as a version control system. The dataset is publicly available on this [site] (http://dx.doi.org/10.6084/m9.figshare.951967)

4.	Informative Visualization  
The authors **learning-to-rank (LR)** approach was compared against 2 state-of-the-art systems: BugLocator and BugScout. The following figures are **Accuracy@k** (this measures the percentage of bug reports for which the authors make at least one correct recommendation in the top k ranked files) results for the 4 implemented methods, with *k* ranging from 1-20.  The LR approach achieves better results than the other three methods on all the 6 projects.  

   <img src="https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/6/Figure%202.jpg" width="1200">

###Improvements
1.	The training set may be prone to sampling bias. The authors trained only on those data sets that had fixed files associated. This implies that the learner is not trained on certain bugs. The authors should develop a technique for predicting source files for such bug reports.

2.	The authors could have added a section listing points that pose a threat to their validity. Adding such **certification envelope** may help other researchers and practitioners provide usage guidelines. 

3.	The authors could have mentioned techniques to further enhance the Accuracy@k metric. Current standards imply that a developer has 70% chance of locating the bug in 10 source files predicted by LR. This could still be time-consuming in certain situations – threatening the initial goal of better productivity.   

###Connection to [Paper 1] (https://github.com/NeilBINGOHIT/fss16gNS/tree/master/read/1)
The authors of this paper have concentrated on using bug reports to narrow down the source files containing the source. A bug report is an important artifact in the software development lifecycle. In the survey, conducted by authors Buse and Zimmermann in paper 1, it is evident that bug reports are extensively used by both managers and developers in their daily development process. Thus the authors have extended this result and tried to make the process of locating the bug efficient.  

###Results
1.	The new method makes correct recommendations within the top 10 source files for over 70% of the bug reports in the Eclipse Platform and Tomcat projects. 
2.	It performs better than BugScout because LR uses features that capture domain knowledge relationships between bug reports and source files. Also LR is trained directly to optimize ranking results. But BugScout is trained for classification into multiple topics. 
3.	The system requires a max of 3643 sec (of the 6 projects) in indexing, max of 3.56 sec in training and a max of 1.59 in testing – making it suitable for practical purposes.
