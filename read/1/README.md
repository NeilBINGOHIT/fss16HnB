
###Paper
 "Information Needs for Software Development Analytics", by Raymond P.L. Buse and Thomas Zimmermann, presented in 34th International Conference on Software Engineering (ICSE), 2012.

###Keywords

1. Cluster Analysis  
Cluster analysis or clustering is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar (in some sense or another) to each other than to those in other groups (clusters).

2. Churn  
Your churn rate is the amount of customers or subscribers who cut ties with your service or company during a given time period. These customers have “churned”. Business people say an acceptable churn rate is in the 5 – 7% range annually, depending upon whether it measures customers or revenue.

3. Telemetry  
Software Project Telemetry is a project management technique that uses software sensors to collect metrics automatically and unobtrusively. It then employs a domain-specific language to represent telemetry trends in software product and process metrics. Project management and process improvement decisions are made by detecting changes in telemetry trends and comparing trends between different periods of the same project. 

4. GQM Paradigm  
GQM stands for "goal, question, metric". It is an approach to software metrics which consists of six-steps. The first three steps are about using business goals to drive the identification of the right metrics and the last three steps are about gathering the measurement data and making effective use of the measurement results to drive decision making and improvements. For details see [wiki](https://en.wikipedia.org/wiki/GQM).


###Features

1. Motivational Statement  
Software development involves making decisions based on metrics. The paper is motivated by the fact that software engineers do not have necessary tools and techniques to leverage metrics from the available information resources and use them to take concrete decisions. As a result, the authors have conducted a survey to present a spectrum of information needs and the corresponding insights gained from them. They also tried to comment on the design of the tools that should be made available to the community. 

2. Study Instruments and Commentary  
To carry out analysis, the authors have used Kitchenham and Pfleeger's guidelines for personal opinion surveys. The survey consisted of 28 questions taken via emails from a random, equal-sized set of engineers and lead-engineers (managers) at Microsoft. They recorded both the importance and difficulty of answering questions in each domain. Importance-related questions were rated on a 4-point scale of Not-important, Somewhat-important, Important, Very-Important.

3. Related Work  
Previous studies have identified information needs for managers for specific decision-making tasks. Jedlitschka identified information needs of managers and showed empirical data on how these needs have impact on cost, quality and schedule. Other people have proposed questions that managers should ask which would help them gather relevant data and make decision. Related work was also done in building an experience factory, where not only data but experiences from projects were collected and reused to make decisions.

4. Informative Visualizations  
The paper includes 6 visualizations. Some of the basic graphs include importance of factors to decision making, importance of types of artifacts and preference of indicators/metrics amongst developers and managers from the survey. The most important is the table that summarizes what information (type : exploration, analysis and experimentation) should tools present to managers for past, present and future scenarios.

![alt tag](https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/1/Results.jpg)

###Improvements

1. Small size of participants  
The underlying hypothesis is that engineers lack the necessary tools and techniques to leverage metrics from the information resources, yet the survey was done only on 110 developers and managers. This number is extremely small compared to the number of software developers and managers in the world. Moreover, we know that socio-technical factors could play an important role. Confining the study only to Microsoft company, which has a specific hierarchy structure, raises doubt about the repeatability of the results. Taking more surveys from different companies with different management structures could help provide a better scenario.

2. Questionable response of participants  
Part of survey involved answering for each metric whether the participant used it or would use it if the metrics were made available. The second half of this question received more votes than the first half but this might be inaccurate as it is easy for some participants to show interest but difficult to adopt it in practice. Although the authors asked in general what decision analytics would help them with, they could have added another part to this question as to how the use of each metric would affect their decision.

3. Repeatability of results  
The authors have laid out a set of information needs and tool guidelines. But the results could have been more effective if the authors would have tested the same results on a different set of developers and managers (preferably from different company and/or different management structure).
