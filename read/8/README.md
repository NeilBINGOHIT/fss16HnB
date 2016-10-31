###Paper 
[Using metrics in Agile and Lean Software Development -  A Systematic literature review of industrial studies] (http://dl.acm.org/citation.cfm?id=2784627), by Eetu Kupiainen, Mia Mantyla, and Juha Itkonen, published in Journal of Information and Software Technology Volume 62 Issue C (pages 143-163), 2015

###Summary
This paper makes a systematic literature review to investigate what metrics are used in industrial projects.  The authors analyze the reported motivations i.e. benefits of applying the metrics, as well as the effects of using metrics in Agile teams. 

###Keywords
1.	Agile  
In Agile software development methods, the focus is in lightweight working practices, constant deliveries and customer collaboration over long planning periods, heavy documentation and inflexible development phases. Characteristics of Agile are team in control, customer focus, simplicity, following a plan, fast feedback, responding to change.

2.	Kaban  
Kaban is neither a software development lifecycle methodology nor a project management approach. Instead, it can be applied to incrementally applied to change and improve some underlying, existing process. 

3.	Lean  
It is a software development process translated from lean manufacturing. It was adopted from Toyota Production systems. It shares similar values and principles with Agile Methods.

4.	Systematic Literature Review  
It is a study methodology that aggregates and synthesizes existing knowledge, identifies the gap in earlier research and provides background information to start investigating a new research topic. 



###Features	
1.	Motivational Statement  
Software metrics have been studied for decades and several literature reviews have been published. However, there are no systematic literature reviews on the reasons for and effects of using metrics in Agile software development context. 

2.	Checklists   
The paper lays down the following research questions to achieve their goal
   *	Research Question 1: What metrics are used in industrial Lean and Agile Software Development?
   *	Research Question 2: What are the reasons for and effects of using metrics in industrial Lean and Agile software development?
   *	Research Question 3: What metrics have high influence in industrial Lean and Agile software development?

3.	Patterns  
The authors chose to perform a systematic literature review (SLR).

   The guidelines provided by Kitchenham were used as a basis to develop the SLR protocol. Moreover, the protocol was developed iteratively, performing first a small pilot study and iterating the details of the protocol in weekly meeting among the researchers. 

   The strategy for finding primary studies was to (1) automate search (gave 774 papers), (2) select based on title and extract (reduced to 163 papers), and (3) select based on full text (reduced to 30 papers). The pilot study was then carried out by selecting 15 papers (5 by relevance, 5 by number of citations and 5 by random selection). Based on the pilot study, a few improvements to the SLR protocol were made. Finally, data extraction was performed by reading the complete text of all the selected papers and coding the relevant excerpts. Integrated coding was selected as data extraction strategy. The coding started by reading the full text and marking relevant quotes with a temporary code. After reading the full text, the first author checked each quote and coded again with an appropriate code based on the built understanding. In weekly meetings, all authors iteratively built a rule set for collecting metrics and discussed borderline cases. 
   
   The final rule set was as follows:

   * Collect metric if team or company uses it.
   *	Collect metric only if something is said about why it is used, what effects it causes, or if it is described as important.
   *	Do not collect metrics that are only used for the comparison and selection of development methods.
   *	Do not collect metrics that are primarily used to compare teams. (There were cases where a researcher or management uses a metric to compare teams. The authors wanted to find metrics a team could use.)

4.	Data  
[Scopus] (http://www.scopus.com), which contains IEEE and ACM database, was used as a search engine. The search string, hits and dates for the search process of the papers can be found in Appendix A. The criteria for the selection process of the searched papers can be found in Appendix B. The authors used the capture-recapture method, where authors evaluated each other’s findings to establish repeatability. To do this they adopted a quality assessment technique – details of the list can be found in Appendix C. Finally a list of definitions of metrics can be found in Appendix D.

###Improvements
1.	Losing valuable metrics because of stringent criteria. The authors accepted only those studies that talked about a metric and had reasons and effects of using it. This implied that if the study talked about a valid metric with compelling reason but no evidence of effect, then it would not be selected. This could yield to sampling bias which might affect the results.

2.	Another source of sampling bias is the selection of 30 studies. 7 of them were from enterprise information systems domain and 10 of them large telecom industries. Moreover 8 of them were from the same company – Ericsson. This over-representation of large companies in the studies could have affected the results. The authors could have targeted small or medium sized company to equally represent the study set.

3.	The manual process of searching and selecting studies, understanding which metric is involved and what reasons are explicitly stated in the study, and understanding its impact could have caused incorrect interpretations. To mitigate threats from such sources, the authors could have reached out for outside council or validated its primary result from survey. 


###Connection to [Paper 1] (https://github.com/NeilBINGOHIT/fss16gNS/tree/master/read/1)
The authors in this paper are focused on metrics in Agile software development. This is similar to paper 1, where authors Buse and Zimmermann surveyed information needs of software managers and developers at Microsoft and found that the most used information is related to quality. The information needs for metrics are related to supporting communication and decision making. This paper can be viewed as an extension of paper 1, where the focus is on what are metrics, what are the reasons for and effects of the metrics in Agile software development.

###Results
1.	The study identified 30 primary studies with 3 cases in total. The primary studies were published in 12 different journals, conferences or workshops. A large share of the primary studies were published in the Agile conferences. The following table summarizes the 30 studies ([S1] to [S30]). It also has information about the year, the type of Agile methodology described, the team size team and the domain of the company adopting it.  

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/8/Figure%201.jpg" width="500"/>

2.	**RQ1** - The authors found 102 metrics in the primary studies. The following table provides the raw results. 

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/8/Figure%202.jpg" width="500"/>

   Further analysis was performed on this set and it was classified based on two categorizations. One of the categorization was by Fenton and Pfleeger (see table 7 in the paper) because their work on software metrics is widely known in the community. Second, it was categorized and compared with the metrics suggested in the original works on Agile methods (see table 8 in the paper) because this would allow us to see whether practitioners follow the metrics suggested in the agile methods or not.

   The Fenton and Pfleeger classification showed that the **metrics were largely applied to products, test plans, code, builds, features, requirements, and defects**. 

   The other classification showed that **most popular metrics suggested by the Agile literature are Effort estimate and Velocity**.  Also it showed that many metrics (39%) found in the primary studies were not suggested in the original works on Agile methods.

3.	**RQ2** - the authors divided the reasons and effects of using the metrics to five categories: Sprint and project planning, Sprint and project progress tracking, Understanding and Improving quality, Fixing Software process problems and Motivating People. The following table lists the number of papers and metrics in different categories.

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/8/Figure%203.jpg" width="500"/>

4.	**RQ3** - the authors have highlighted the most influential metrics found in the study. The performed quantitative analysis be assessing the perceived importance of each metric from 1(low) to 3(high). The metrics are considered important if the author of the primary study or case employee praised it, if there were signs of continuous use, and if metrics had positive correlation to important output measures. 

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/8/Figure%204.jpg" width="900"/>      
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/8/Figure%205.jpg" width="900"/>

###Conclusion/Take Away
1.	Common Agile software development methods in industry are Scrum, Extreme Programming, Lean Software Development and Kanban.
2.	Agile methods value individuals and interactions, working software, customer collaboration, and responding to change over processes, documentation, contracts, and plans. Agile development emphasizes short development cycles, frequent deliveries, continuous face-to-face communication and learning.
3.	According to Pfleeger, we use metrics every day to understand, control, improve what we do and how we do it.
4.	In Agile, practitioners can add and invent new metrics according to their needs.
