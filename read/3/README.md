###Paper
[Linking Software Development and Business Strategy through Measurement] (http://ieeexplore.ieee.org.prox.lib.ncsu.edu/stamp/stamp.jsp?arnumber=5445168), by Victor Basili, Mikael Lindvall, Myrna Regardie, Carolyn Seaman, Jens Heidrich, Jurgen Munch, Dieter Rombach, and Adam Trendowicz, published in 43rd volume IEEE Computer Journal in 2010.   

###Summary
The paper talks about using the GQM+ (goals, question, metric) paradigm to measure the success of goals and strategies on all organizational levels.

This strategy helps to decide when and how to transform goals into operations and how to evaluate the success of strategies with respect to those goals.

Steps to use this model (The model goes from left to right and top to bottom. See Figure 2 in the paper)

1.	The starting point of GQM+ Strategies is a business goal. Along with this, it requires explicit documentation of relevant context factors and assumptions necessary for understanding and evaluating goals. Use the business goal template for documentation (Figure 3 in paper).  
2.	The next step is to ask questions necessary to interpret the goal.  
3.	The questions will yield metrics required to measure the goal and an interpretation that provides the information whether the goal 
is achieved or not.  
4.	Finally, list all the possible strategies and select one for implementation.  
5.	At the next level down in the model, a software development goal is derived from the strategy.  
6.	Steps 2-4 are repeated for this level.  
7.	Similarly, project level goal is derived and Steps 2-4 are followed  

###Keywords
1.	Business Alignment   
This phrase is used to talk about aligning the business goal with software development strategies.

2.	Capability Maturity Model Integration (CMMI)  
CMMI is a process improvement training and appraisal program. CMMI models provide guidance for developing or improving processes that meet the business goals of an organization. The model has maturity levels from 1-5 namely Initial, Managed, Defined, Quantitatively Managed and Optimizing. See [wiki]( https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration#Maturity_levels_in_CMMI_for_services) for details regarding the maturity models.

3.	MoSCoW  
It is a prioritization approach for requirements and release planning. The term MoSCoW is derived from the first letter of each of four prioritization categories – Must have, Should have, Could have, Would like but won’t get. Developers will initially try to deliver all the Must have, Should have, and Could have requirements but the Should and Could requirements will be the first to be removed if the delivery timescale looks threatened. For details see [wiki](https://en.wikipedia.org/wiki/MoSCoW_method)

4.	COCOMO  
Cost Constructive Model is a procedural software cost estimation model which uses a basic regression formula with parameters that are derived from historic project data and current as well as future project characteristics. Basic COCOMO computes software development effort (and cost) as a function of program size (in KLOC). 

###Features
1.	Motivational Statement  
Organizations constantly need alignment of business goals with development strategies and justifying of cost and resources for software and system development. But we do not have effective methods for linking business goals and software related effort. GQM+ tries to bridge the gap between business strategies and their project level implementation.

2.	Related Work  
The paper talks about related measurement programs like GQM, BSC, and PSM. GQM approach provides a method for an organization or a project to define goals, refine those goals into specifications of the data to be collected, and then analyze and interpret the resulting data in the light of the original goals. BSC (Balanced Scorecard) approach links strategic objectives and measures through a scorecard which consists of four perspectives: financial, customer, internal business processes and learning and growth. PSM (Practical Software Measurement) approach offers detailed guidance on software measurement, including providing a catalog of specific measures and information on how an organization can apply those measures in projects.

3.	Informative Visualizations  
The paper has a list of figures and tables explaining GQM+ strategies and their ongoing applications. The following figure depicts the eight conceptual components, that form basis for constructing a consistent model, and how these components interrelate. The eight components are business goals, context factors, assumptions, strategies, level i goals, interpretation models, goal+ Strategies elements and GQM graph.
![alt tag](https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/3/Figure%201.jpg)

4. Tutorial Materials    
The paper takes on a sample application and teaches how to apply the GQM+ Strategy. The authors start with a business goal of “increasing profit from software service usage”. They build assumptions, questions, metrics and interpretation models around it. They then derive lower level goals and perform the same task. Finally relate how the lower tasks will help determine the success of the higher level goals. The following figure depicts the outcome of the application. 
![alt tag](https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/3/Figure%202.jpg)

###Improvements
1.	Absence of backup plan  
The users are supposed to make assumptions and select strategies that work best. But the authors did not mention what to do if at some point during the lifecycle, the assumption backfires or goals are not met completely.

2.	Effectiveness of GQM+ approach  
The paper offers a list of industries that have adopted the GQM+ paradigm but it might make more impact on the readers if the authors had provided supporting data of the effectiveness of the method.

3.	User lacking knowldege of linking goals and strategies   
The paper also fails to point out the importance of determining goals and strategies. Mentioning a list of heuristics or defining who should be responsible for coming up with the correct and effective goals and strategies would help new engineers to pick up this method. The model is more likely to fail, when a person taking charge has a weak understanding of the links between the goals and strategies. 
