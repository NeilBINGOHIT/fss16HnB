###Paper 
[Analyze This! 145 Questions for Data Scientist in Software Engineering](http://dl.acm.org/citation.cfm?id=2568233), by Andrew Begel and Thomas Zimmermann, proceedings of the 36th International Conference on Software Engineering 2014.

###Summary
The paper is about two surveys related to data science applied to software engineering. The first survey solicited questions that software engineers would like to ask data scientists to investigate about software, software processes and practices. This yielded 145 questions grouped in 12 categoriesThe second survey asked a different pool of software engineers to rate the 145 questions. Respondents favored questions that focus on how customers typically use their applications. The idea behind categorizing and cataloging 145 questions is to help researchers, practitioners, and educators to more easily focus on their efforts on topics that are important to the software industry.

<img src="https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/5/Figure%201.jpg" width="48">

###Keywords

1.	Software Analytics
It is a subfield of analytics with the focus on software data.

2.	Affinity Chart

3. TBD

4. TBD

###Features

1.	Motivational Statement  
The data science stream is growing. All businesses want to use analytics to better reach their customers. As a result, there are keynote speeches and panel talks about how to make the software engineering community more data-driven. With this survey the authors have given the software developers a chance to express their doubts regarding to data-science. 

2.	Related Work  
With the big data boom, several research groups pushed for more use of data for decision making, and shared their experiences collaborating with industry on analytics projects.  Zhang et al. emphasized the trinity oh software analytics in the form of three research topics (development process, system, users) as well as three technology pillars (information visualizations, analysis algorithms, large-scale computing). Buse and Zimmermann argued for a dedicated analyst role in software projects and presented an empirical survey on guidelines for analytics in software development ( [original paper](https://github.com/NeilBINGOHIT/fss16gNS/tree/master/read/1) )

3.	Data  
The full list of 145 questions is provided on this [page](https://www.microsoft.com/en-us/research/publication/appendix-to-analyze-this-145-questions-for-data-scientists-in-software-engineering/) under the Related Info tab.
 
4.	Patterns  
The authors received 728 items in 203 responses in the first survey. In order to categorize they used the open card sort technique. Card sorting is a technique that is widely used to create mental models and derive taxonomies from data. In this case, card sorting also helps us to deduce a higher level of abstraction and identify common themes. 

Card sorting has three phases: in the preparation phase, cards for each question written by the respondents are created; in the execution phase cards are sorted into meaningful groups with a descriptive title; finally, in the analysis phase, abstract hierarchies are formed in order to deduce general categories and themes. 

5.	Visualizations  
The following affinity diagram summarizes the list of popular activities (in oval shape) that drew the attention of the respondents which are classified based on the job role (in box shape).

![alt tag](https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/5/Figure%203.jpg=100x20)


###Improvements

1.	The survey could have been both internal and external  
The survey was internal to Microsoft. The authors could have reached out to a bigger audience and weighted the opinions of other software engineers around the world.

2.	Data scientists view on the survey results  
Since the idea to help researchers, practitioners and educators improve their focus and efforts on topics that are important, the authors could have added a step where the data scientists explain how each of the top 24 questions could be analyzed.

3.	**Taking input from data scientists**  
The motivation is to make software processes more data driven. Then why not include the opinion of data scientists (since they are also part of the organization and possess knowledge about the processes). The authors could have collaborated with data scientists to rate the questions. Moreover, they could also have created a reverse survey where data scientists ask the questions regarding current software practices and then told the data scientists to analyze how these practices could be transformed into data driven practices.

###Connection to [Paper 1](https://github.com/NeilBINGOHIT/fss16gNS/tree/master/read/1)

The authors in this paper tried to understand the questions that software engineers would like to ask to data scientists about software. To me, this paper seems to be inspired from the [paper](http://dl.acm.org/citation.cfm?id=2337343), where the authors have surveyed 110 software developers to present a spectrum of information needs and the corresponding insights gained from them. Moreover, the authors categorized those information needs into 9 categories. Interestingly, Thomas Zimmermann, co-author of that paper.

###Results

1.	The findings suggest that engineers favor questions that focus on how customers typically use their applications. Also there was opposition against the use of analytics to assess the performance of individual employees or compare them with one another. 

2.	First survey yielded questions which were cataloged into the following categories

![alt tag](https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/5/Figure%203.jpg)

3.	Top 24 desired questions (rated essential or worthwhile) 

(Icon with People) Questions that concern about customers
(Icon with Setting) Questions that focus on engineering and effects of software development practices on work
(Icon with Star) Questions concerned with product quality issues

![alt tag](https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/5/Figure%204%20-%20Top%2024.jpg)

4.	Top 10 opposed questions (rated unwise)
![alt tag](https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/5/Figure%204%20-%20Top%2010.jpg)


###Conclusion/Take Away
1.	Researchers can use such survey results to collaborate with industry and influence their software development processes, practices and tools. Professionals can get idea about which factors to analyze. Educators can get guidance on what analytical techniques to teach.
