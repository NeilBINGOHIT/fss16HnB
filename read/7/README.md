###Paper

[The Making of Cloud Applications: An Empirical Study on Software Development for the Cloud] (http://dl.acm.org/citation.cfm?id=2786826), by Jurgern Cito, Philipp Leitner, Thomas Fritz, and Harald Gall, proceedings of the 10th Joint Meeting on Foundation of Software Engineering, 2015.

###Summary
This paper reports on a systematic study on how software developers build applications for the cloud. The primary focus of the study was to examine what makes software development for the cloud “unique”, i.e. what differs in terms of processes, tools, and implementation choices, to other development projects. From the study, the authors extracted a set of guidelines for cloud development and identified challenges for researchers and tool vendors.

###Keywords
1.	DevOps  
DevOps describe the convergence of previously separated tasks of developing an application and, its deployment and operation. In DevOps, software development and operation activities are often handled by the same team, or even by the same engineer.  

2.	Infrastructure-as-a-Service (IaaS)  
In an IaaS cloud, resources like computing power, storage, networking are acquired and released dynamically, typically in the form of virtual machines. IaaS customers do not need to operate physical servers but are still required to administer their virtual servers.

3.	Platform-as-a-Service (PaaS)  
PaaS cloud provide entire application runtimes as a service. The PaaS provider manages the hosting environment and customers only submit their application bundles. They typically do not need the access to physical or virtual servers that the applications are running on. 

4.	Software-as-a-Service (SaaS)  
In SaaS, complete applications are provided as cloud services to end customers. The provider handles the entire stack, including the application. The client is only the user of the service.

###Features	
1.	Motivational Statement  
The cloud is rapidly growing area of interest. Several platforms such as Amazon’s EC2, Microsoft Azure, Google App Engine or IBM’s Bluemix are already gaining mainstream adoption. However, so far, there is little systematic research on the consumer side of cloud computing, i.e. how software developers actually develop applications in and for cloud. This user-driven approach became the motivation for this paper.

2.	Related Work  
There has been a multitude of empirical research on the development of general software applications. So far, research on cloud computing has mainly focused on provider-side issues like server-management or performance measurement. But there is a lack of client-side research. Barker et al. named “user-driven” research as one of the major opportunities for high impact cloud research. Khajeh-Hosseini et al. stated that the organizational and process-oriented changes implied by adopting the cloud is currently not sufficiently researched. Minor work on cloud programming models was carried out but it did not cover the professional software development environments.

3.	Study Instruments  
The authors conducted the study based on the techniques found in Grounded Theory. They used a mixed methodology consisting of three steps of data collection and iterative phases of data analysis. 
   First they defined a set of 23 open-ended questions and conducted qualitative semi-structured interviews with 16 participants. 
   Second, they ran a quantitative survey with 32 questions which were primarily formulated as statements, asking participants to state their agreement on a five-point Likert scale.  They gathered responses from 294 professional software developers, and using open coding they identified 4 topics of high interest: fault localization, monitoring and performance troubleshooting, cost of operation, and design for scalability. 
   Lastly, to gain a better understanding and more details on those topics they conducted a second round of qualitative deep-dive interviews with 9 professional developers. 
   The interview and survey materials can be found in this [website](http://www.ifi.uzh.ch/en/seal/people/cito/cloud-developer-study.html)
 
4.	New Results  
The results of discussion on the 4 topics – fault localization, monitoring and performance troubleshooting, cost of operation and design for scalability are as follows

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/7/Image%20-%20new%20results.jpg" width="900"/>

   Furthermore, the authors extended their research by finding out how the usage of tools and production data changed in the cloud development projects. They reported how tooling evolved in cloud, what metrics are available and how they are utilized.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/7/Image%20-%20new%20results%20tools.jpg" width="900"/>

###Improvements
1.	The 25 cloud developers, that were interviewed, raises a question that to what extent do they represent to the overall population of cloud developers. This can be resolved by re-producing similar results on a different set of cloud developers.

2.	Since the participants for the survey were chosen vis GitHub, there is room for sampling bias. This bias seemed to attracted only software engineers who are actively interested in open source development and who were following progress of at-least one big open source cloud project. Selecting participants from different mindsets could have enhanced the results.

3.	The authors could have dived deep into metrics. They could have asked the participants (developers) which metrics they would like to user and why. Analysis on the results would have helped the community decide on which metrics to focus.

###Connection to [Paper 1](https://github.com/NeilBINGOHIT/fss16gNS/tree/master/read/1)
The authors of this paper were interested in the role of data and operational metrics in cloud development. This was the basis of paper 1, where the authors pointed out that software development decisions should be largely based on metrics. By the extending this rule, the authors of this paper show that metrics indeed plays a major role in cloud development.

###Results
1.	The majority of developers thinks about cloud mostly as a deployment and hosting technology following either the IaaS or PaaS model. For these developers, the ability to easily scale applications and the ease of infrastructure maintenance is what makes cloud unique. 
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/7/Figure%202.jpg" width="500"/>

2.	The interviews also revealed that there is a large mindset gap between the developers who think of cloud as either IaaS or PaaS, and those who think of it mostly in terms of SaaS.
3.	The quantitative results for the Likert-type scale questions from the survey are summarized as follows
  &nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/7/Figure%203.jpg" width="1000"/>
  
4.	The interviews show that elasticity, ease of infrastructure maintenance and automation drive most of the changes of software development in the cloud. These can be broken down into two aspects i.e. API-driven infrastructure at scale and volatility of cloud instances.
5.	As part of the survey, the participants were asked whether they faced limitations in application architecture and design specific to the cloud. The results were as follows

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/NeilBINGOHIT/fss16gNS/blob/shrenuj/read/7/Figure%204.jpg" width="500"/>

6.	The results show that developers need better means to anticipate runtime problems and rigorously define metrics for improved fault localization. And cloud offers an abundance of operational data, however, developers still often rely on their experience and intuition rather than utilizing metrics.

###Conclusion/Take Away
1.	Cloud developers design for failure. Well known cloud users have adopted this mindset. Netflix, for instance, has stated that they use an application called [Chaos Money] (http://techblog.netflix.com/2012/07/chaos-monkey-released-into-wild.html) to randomly terminate cloud instances in production, to force the application design that can tolerate such failures when they happen unintentionally.

2.	Cloud developers design for scalability. The [Twelve-Factor] (http://12factor.net/) app design manifesto is the de-facto standard when it comes to best practices when building cloud applications.

3.	**How does the development and operation of applications change in a cloud environment?** In the cloud, servers are volatile. They are regularly terminated and re-created, often without direct influence of the cloud developer. Our study has shown that the concept of API-driven infrastructure-at-scale and the cloud instance volatility have ripple effects throughout the entire application development and operations process. They restrict the design of cloud applications and force developers to heavily rely on infrastructure automation, log management, and metrics centralization. While these concepts are also useful in non-cloud environments, they are mandatory for successful application development and operation in the cloud.

4.	**What kind of tools and data do developers utilize? for building cloud software?** Based on our research, more data, and more types of data, are utilized in the cloud, for instance business metrics (e.g., conversion rates) in addition to system-level data (e.g., CPU utilization). However, developers struggle to directly interpret and make use of this additional data, as current metrics are often not actionable for them. Similarly, cloud developers are in the abstract aware that their design and implementation decisions have monetary consequences, but in their daily work, they do not currently think much about the costs of operating their application in the cloud.

