###Paper
[Fair and Balanced? Bias in Bug-Fix Datasets] (http://dl.acm.org/citation.cfm?id=1595716), by Christian Bird, Adrian Bachmann, Eric Aune, John Duffy, Abraham Bernstein, Vladimir Filkov, Premkumar Devanbu, proceedings of the 7th meeting of European Software Engineering Conference and the ACM SIGSOFT symposium on the Foundations of Software Engineering 2009.

###Summary
Software engineers have long been interested in where and why bugs occur in code and in predicting where they might turn up next. Researchers have used bug tracking systems and code version histories as source of bug data to test their hypothesis and build statistical bug prediction models. But the authors have questioned the integrity of the bug fixes records/datasets and asked are they fair representation of the full population of bug fixes?
 
###Keywords
1.	Sampling Bias  
When the data gathered does not represent the full population the sampling bias is said to be introduced. Sampling bias makes truly random sample impossible.

2.	Hypothesis Testing  
Hypothesis testing is a method in which data is gathered relative to a proposed hypothesis and statistical methods are used to confirm or refute the hypothesis with a given degree of confidence.

3.	Commit Feature Bias
4.	Bug Feature Bias
5.	False negative and false positives
6.	P-values

###Features

1.	Motivational Statement  
Processes and humans are imperfect. Historical datasets are used to test hypothesis concerning processes of bug introduction and also to build statistical bug prediction models. The claim is that only a fraction of bugs are actually labelled in those data set and the same goes for code commits. And prediction made from samples can be wrong if the samples are not representative of the population. This threatens the validity and effectiveness of the derived hypothesis and models.

2.	Related Work  
Related work shows that bias is big consideration in hypothesis testing. Data quality also differs from project to project. Different projects have different methods of defect handling. 

3.	Data  
The authors have used [Eclipse](http://www.st.cs.uni-saarland.de/softevo/bug-data/eclipse) and [AspectJ](http://www.st.cs.uni-saarland.de/ibugs) bug data set from the University of Saarland. Apart from this, they gathered data for five projects: Eclipse, NetBeans, the Apache Webserver, OpenOffice and GNOME. They also mined bud databases: Bugzilla and Issuezilla.

4.	Patterns  
The authors have described patterns for data retrieval and preprocessing. They extracted change histories from source code management system (SCM) commit logs. Information included commit date, committer identity, lines changes and log messages. In addition to this information, they also collected information on rework like new commit changes. This required origin analysis which involved converting CVS and SVN repositories into git. Regarding bugs, they extracted information related to opening, closing, reopening, assignment, severity, comments, time and initiator of every event.

The authors also adopted Fisher et al.’s technique of finding links between commit and bug report. The technique involves searching the commit log messages for valid bug report references. But the authors made several changes to decrease the number of false negative links. (see steps mentioned on page 5)

To validate the data retrieved, the authors manually scanned a random sample for false positives and false negatives.

###Improvements

1.	What if the authors did hypothesis testing on the wrong data set
