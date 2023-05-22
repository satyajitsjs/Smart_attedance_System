# Smart_attedance_System
1.INTRODUCTION:
Every organization requires a robust and stable system to record the attendance of their students. and every organization have their own method to do so, some are taking attendance manually with a sheet of paper by calling their names during lecture hours and some have adopted biometrics system such as fingerprint, RFID card reader, Iris system to mark the attendance. The conventional method of calling the names of students manually is time consuming event. The RFID card system, each student assigns a card with their corresponding identity but there is chance of card loss or unauthorized person may misuse the card for fake attendance. While in other biometrics such as finger print, iris or voice recognition, they all have their own flaws and also they are not 100% accurate . Use of face recognition for the purpose of attendance marking is the smart way of attendance management system. Face recognition is more accurate and faster technique among other techniques and reduces chance of proxy attendance. Face recognition provide passive identification that is a person which is to be identified does not to need to take any action for its identity. Face recognition involves two steps, first step involves the detection of faces and second step consist of identification of those detected face images with the existing database. There are number of face detection and recognition methods introduced. Face recognition works either in form of appearance based which covers the features of whole face or feature based which covers the geometric feature like eyes, nose, eye brows, and cheeks to recognize the face. Our system uses face recognition approach to reduce the flaws of existing system with the help of machine learning, it requires a good quality camera to capture the images of students, the detection process is done by  histogram of oriented gradient. And recognizing perform through deep learning. The frontend side (client side) which consist of GUI 
which is based on electron JS and backend side consist of logic and python (server side), an IPC (Inter Personal Communication) bridge is developed to communicate these two stacks. The images capture by the camera is sent to system for further analysis, the input image is then compared with a set of reference images of each of the student and mark their attendance
2.  SOFTWARE AND HARDWARE SPECIFICATION
The hardware and software are required for this project,
●	The system must be user friendly.
●	The system must be able to handle large number of data.
●	Processing speed of the system must be fast.

Hardware Configuration:
Main Processor	Intel core 2.00GHz
Random access memory	4GB
Hard disk capacity	1TB
WEB cam support	
Software Configuration:
Operating System	Window 10
User Interface	HTML, CSS, Bootstrap
Client-side Scripting	Django
Programming Language	Python
Database	SQLite
Supporting browsers: Firefox, Chrome, Internet Explorer

3.  RELATED   WORK
In recent years, a number of face recognition based attendance management system have introduced in order to improve the performance of students in different organization. In  Jomon Joseph, K. P. Zacharia proposed a system using image processing, PCA, Eigen faces, Microcontroller, based on Matlab. Their system works only with front face images and there is need of a suitable method which works with the orientation of the system. Ajinkya Patil with their fellows in  proposed a face recognition approach for attendance marking using Viola jones algorithm, Haar cascades are used to detect faces in images and recognition performs through Eigen face method.  Another approach of making attendance system easy and secure, in the author proposed a system with the help of artificial neural networks, they used PCA to extract face images and testing and training were achieved by neural networks, their system performs in various orientation. A 3D face recognition approach for attendance management system was proposed by MuthuKalyani.K, VeeraMuthu.A has proposed, they marked attendance with monthly progress of each student. There is need for an alternative algorithm which can enhance the recognition on oriented faces. Efficient Attendance Management system is designed with the help of PCA algorithm [8], the have achieved accuracy up to 83% but their system performance decreases due to slightly changes in light condition. An eigen face approach along with PCA algorithm for marking face recognition attendance system have introduced by author in [9], they mention comparison of different face recognition algorithm in their paper. Overall it was good approach to maintain record of attendance.


Literature survey for face recognition
Many technical methods have been proposed by many.  
3.1 Eigen face technique  This process is used for completing reduction in the dimensionality. This algorithm is frequently used for the recognition of faces. This detection and face recognition uses the principal component study. Eigen face acts as a core component for dividing of face into separate feature vector. Covariance matrix used for finding the data from the article vector. The faces are differentiated by using the highest Eigen values. The image having a face is then measured as grouping of Eigen expressions. The difference among faces is then measured using that of the Eigen vectors. Face space is defined as the top M Eigen faces that match with the outline of M dimensional space.  Association and training data has a much relation between them. By the authors  to expertly symbolize photographs of the faces. By recreating a image by using collecting small loads for every image and progress image as good face snapshot. Eigen picture  helps to obtain the weights of each face. The Eigen face method is widely used because of its implementation and algorithm that makes the face recognition easy. This is good for storage and time of handling is also good. Eigen face has correctness and it depends on many things. The image can be minimized to the dimension size in short period of time can be done by PCA. The result that is satisfactory can be achieved by image pre-processing. The Eigenface method makes the system work very  and we can tell that it is the main advantage .more time is consumed for both Eigen values and the Eigen vectors. This Eigen face is not suitable for location and lightening conditions  


3.2 Neural networks patterns  The main goal of neural networks is that it has the capability to perform complex face patterns. The neural networks are employed in many layers, different number nodes, and also different learning for achieving good performance. The applications if this methods are driving of robot autonomously, recognition of objects, and problem recognition. Principal component analysis more efficient than the feature abstraction. Neural network is non-linear so it is used for face recognition. If there are 40 individuals and are having 400 images then the correctness of the face identification is attained by 96.2% by the authors. The time taken for arrangement is 0.5 second and time taken for training is 4 hours and sends slight invariance to rotation translation and scale.in supervised pattern matching because of its ability and plainness we choose MLP algorithm that is multi-layer perceptron. For pattern classification neural networks are used. For extracting of feature vectors and also for finding specific feature points Gabor wavelet method is used. By experimenting this we got better results compared with other algorithms like Eigen approaches and matching of patterns.A new technique that polynomial neural network is proposed for face recognition. This principal component analysis method used from extracting the features and dimensionality of the image designs . When there is a non-linear vector SRDKA can give precise solutions than that of the subspace .when there is pushing of inhibitory neurons a new method coevolutionary network s proposed. SRDKA is used for solving the computation of Eigen vector computation and regression difficulties by saving of enormous costs . By using of single system authors more finding rate and less false optimistic rate with that of the composite training.  



3.3 Fisher face approach  Fisher faces the most widely and effectively used methods for recognition of faces. This method depends on the method of appearance. Linear or fisher discriminant analysis for face recognition established in the year 1930 by Fisher. It one of successful methods that are used for face recognition procedure Belhumer et al. authenticated the method called LDA. This LDA method used for the finding of set of centre images that maximizes the ratio of the outside the class scatter and within the class scatter. This method has some drawbacks that the session the distribute medium will be perpetually alone ever since pixels of number image more than that pictures that are maximized for detection error rate so that if any alteration is posed and brightness if there changes that is inside the pictures that are same. Many algorithms have been proposed to overcome the above drawbacks. Belhumeur et al.have designated fisher face method for face recognition by practising the linear discriminant analysis and principal component analysis that lead to the subspace projection matrix same as that of the Eigen face method. This fisher face method has the advantages of by taking exclusive course data and by falling dissimilarity surrounded by course and then exploit the class separation. In this fisher face method N * M images are composed and then reformed into N *M)*1 vector.one can set to categorize the training data compact changed persons and their different pictures .The main disadvantage of thismethod further testing conclude prediction image planetary compared to that the Eigen face and also it takes a lot of time for calculating the ratio between the outsideclass scatter to inside class scatter. The dimension of projection of the face space is not that much compared to Eigen face that results in more handling time for recognition and then large storage for face.  


3.4 Elastic bunch graphing approach  This conventional of the features with the help data structure method entirely different to that of the both fisher face and then the Eigen method. This face recognition method uses the elastic bunch matching method that deals with that of the identifying the faces considering athat is called as the bunch graph[13] and also it same for query image and also for the landmarks that are expected and they are followed by using that of the bunch graph. By taking the instances of Gabor filters which has other name called the face graph the features are taken out. The fraction that is used for control sebum is done on the source of similarities between the query image and the face images of the database.  EBGM that is elastic of bunch graph matching makes uses structure material of face method and then reproduces that of images of the same subject such as scale, rotate, and then deform in the plane of the image. During the matching process one model is taken and then deform, rotate, scale and translated. Labelled graph boundaries are used in this and distant data and nodes are labelled by using constant wavelet jets. To yield the local features the images Gabor wavelet conversion is used. These are inspired difficulty kernels that are controlled by the Gaussian enclose function that contains the set convolution constants for different kernel’s advices occurrences. Elastic graph matching the simple process for new graphs and also associate to graphs with the images.  In this version a single labelled graph directed into an image. The graph that labelled has set organised jets in particular spatial order. By making using Gabor wavelet relative set of jets can be designated to transform of the image. The image jets the same relative spatial arrangement to that the graph jets and each image jet related one graph jet. For likeliness of growth allows for some translation, distortion and rotation up some of the extent. The typical correspondence stuck both the picture the diagram the similarity of the graph with that of the image. One difference

 compared Eigen faces method that it treats one vector per feature of faces. Because of this even when it modified or missing one feature we can identify the person. The data that deposited can be added to database for storage. This makes easy when new image is added and no energy need because already it kept the database. It finds a person up to 23 points. The weakness in method is blatant to relieving surroundings for this it needs diagrams has substantially image. Consequence have substantial reduction in the identification rate when the variations in illumination are larger.  
3.5 Template matching approach  Template matching method is used for describing the face patterns of the single face. Bruneli and Poggio obtained four features that is nose, mouth, eyes, and face for template matching. The results are compared with the algorithm that is geometrical centred on 188 images of the 47 subjects by the system. The algorithm that is design matching is very good and its chives 100% face recognition. For linear arrangement patterns it uses the PCA method that is principal component analysis method by using Eigen faces. When there is extraction of patterns then their-arises the difficulty. Advantage of this method is it easy to implement and also less costly compared to other classifiers. Template based methods gives good results compared to that of the feature based methods. The pattern algorithms are very costly and also they cannot be handled. The pattern that is given and the input image can be easily fingered by using recognition procedure. Karungaru et al practised that genetic algorithm with different outcomes on the target image by using template as pre-processing. The functioning of these method is said that additional features are needed for this for the face recognition problems. The pattern matching of a test image is signified by two dimensional array of strength values with appropriate method of Euclidean distance such as single pattern on behalf of that of the whole face. Some additional efforts are needed for increasing 
the performance of the face recognition approaches when they come across the
surroundings of real world . The method that is currently used is not free from the boundaries. Template matching method is a reasonable approach  
3.6 Geographical feature matching  The working out fixed of image expressions as of image of a surface depends on geometrical matching. Automatic facial acknowledgement and other works that are important are done by that of the geometrical of feature matching since 1973.the chief facial features such as mouth, nose eyebrows and eyes and outline of a face is defined by the vector that is used for representing of the location and size of the facial  .the recognition was done by using Bayes classifier. The system attained a recognition rate of 75% on the database of a 20 people by making use of two pictures those are model image and the other is the test image. The geometry expressions are taken from picture mouth position is taken out a set for by authors. These people has taken 35 features and formed a 35 dimensional vector. By doings so they achieved a 90% acknowledgment percentage databank certain persons. The author authors of  offered assortment detachment process that accomplished acknowledgment level of 95% interrogation data store 687 personalities.30 manually signified distances was signified by every face. The other authors reprocessed the methods to find the features themes every image that leads to decreased packing inevitability data store. Accurately there will be 35 to 45 feature points for every face that is produced. In this method two cost are evaluated they are similarity cost and topological cot were evaluated the geometrical feature identification depends mostly on the exactly measured distances between the features that are useful for finding out matches from the database. This method depends on the exactness of the feature location algorithms. The main drawback of this method is that the automated feature position algorithms do not offer a required substantial computational time and a high degree of correctness. This procedure

 mainly includes the improvement of the facial images with chin and ears and also include the potential features because it enhances the method that are used for face recognition process. The capability to identify the face model is planned by dividing it into four steps .the first step that is used is the preprocessing step. Here in this step it decreases the sound then effort picture transmuted to that of double. The next method is used for grouping the spitting image geographies it discovers basis of the labelled structures. Finally the probable distance used for identifying process is calculated.to decrees the examine planetary trough diminishing imagines sorts data has been presented by the Khalid et al author. This process achieves a recognition rate of 86%.In Haiku and Sadka the calculation of face image is formed by the distribution of distance. The image that are formed by the distribution of distance defines the shape Gabor sieves that involves mass then and degree. The concerns to partial image is taken for differentiating among the illustrations at data list is presented by the Gabor filter. Zhental and other authors proposed a acknowledgement process that is assembled the image graphics. Here mainly imageseparate to various face images are then face alignment reformed measure and image space. The next step is the LBP and it presents a virtuous surface demonstration defining makeover related data for changed spaces that provides good -arranged image acknowledgement structures. Geometry that depends on the face recognition technique that makes use of the makes use of the subspace that are related to that of the models.This provide the geometrical asserts image space that provide active acknowledgement server some expanse tenders that are related to images.



 












4.  METHODOLOGY 
The proposed system is designed for automating the attendance of the different organization and reduces the flaws of existing manual system. The system calculate the attendance subject wise, that is the data of students and subjects are added manually by administrator, and whenever time for corresponding subject arrives the system automatically starts taking snaps and find whether human faces are appear in the given image or not. We have used Histogram of Oriented Gradient for face detection and deep learning techniques to calculate and compare 128-d face features for face recognition. Once faces are detected and recognize with the existing database, system calculate attendance for the recognize students with the respective subject id in real time. And an excel sheet generated and saved by the system automatically. Our system splits into two parts, First the front end side which consist of GUI which is based on Electron JS that is JavaScript stack which is serving as a client and the second is the backend side which consist of logic and based on Python which is serving as a server. And we know that both the languages cannot communicate with each other directly so we have used IPC (Inter Personal Communication) techniques with zero library as a bridge to communicate these two languages. The Electron JS call the python functions and interchange data via TCP with help of Zero PC Library.
Many data repositories already mint unique identifiers such as Digital Object Identifiers (DOIs) 
to registered datasets, which partially reflect people’s efforts to make data as a kind of formal 
publication. The word data publication is derived from paper publication. If a journal paper is 
comparable to a registered dataset in a repository, then the repository is comparable to a journal. 
A paper has metadata such as authors, publication date, title, journal name, volume number, 
issue number and page numbers. Most papers also have DOIs which resolve to the landing 
webpages of those papers on their publisher websites. By documenting metadata, minting DOIs 
to registered datasets in a repository, the datasets are made similar to published papers. The 
procedure of data publication is already technically established in many data repositories.  

However, data publication is not just a technical issue. There are also social issues to be 
considered, because data is not conventional regarded as a “first class” product of scientific 
research. Many datasets were previously published as supplemental materials of papers. 
Although data repositories make it possible to publish data as standalone products, the science 
community still needs more time to give data an equal position as paper. A few publishers 
recently released so called data journals to publish short description papers for datasets published 
in repositories, which can be regarded as a way to promote data publication. Funding 
organizations have also taken actions to promote data as formal products of scientific research. 
For example, the National Science Foundation in United States now allows funding applicants to 
list data and software programs as products in their bio-sketches.     

A data repository has both data providers and data users. Accordingly, there are issues to be 
considered for both data publication and data citation. If a registered dataset is tagged with 
metadata such as contributor, date, title, source, publisher, etc. and is minted a DOI, then it is 
intuitively citable just like a published journal paper. To promote common and machine readable 
metadata items among data repositories, a global initiative, the DataCite, has been working on 
standards of metadata schema and identifier for datasets since 2009. For example, DataCite
suggests five mandatory metadata items for a registered dataset: identifier, creator, title, 
publisher, and publication year. It also suggests a list of additional metadata items such as 
subject, resource type, size, version, geographical location, etc. The methodology and technology 
developed by DataCite are increasing endorsed by leading data repositories across the world, 
which make possible a common technological infrastructure for data citation. 

Various communities have also taken efforts to promote best practices in data citation, especially 
the guidelines for data users. The FORCE11 published the Joint Declaration of Data Citation 
Principles in 2013 to promote good research practice of citing datasets. Earlier than that, in 2012, 
the Federation of Earth Science Information Partners (2012) published Data Citation Guidelines 
for Data Providers and Archives, which offers more practical details on how a published dataset 
should be cited. For example, it suggests seven required elements to be included in a data 
citation: authors, release date, title, version, archive and/or distributor, locator/identifier, and 
access date/time. 
Many data repositories already mint unique identifiers such as Digital Object Identifiers (DOIs) to registered datasets, which partially reflect people’s efforts to make data as a kind of formal publication. The word data publication is derived from paper publication. If a journal paper is comparable to a registered dataset in a repository, then the repository is comparable to a journal. A paper has metadata such as authors, publication date, title, journal name, volume number, issue number and page numbers. Most papers also have DOIs which resolve to the landing webpages 
of those papers on their publisher websites. By documenting metadata, minting DOIs to registered datasets in a repository, the datasets are made similar to published papers. The procedure of data publication is already technically established in many data repositories.   However, data publication is not just a technical issue. There are also social issues to be considered, because data is not conventional regarded as a “first class” product of scientific research. Many datasets were previously published as supplemental materials of papers. Although data repositories make it possible to publish data as standalone products, the science community still needs more time to give data an equal position as paper. A few publishers recently released so called data journals to publish short description papers for datasets published in repositories, which can be regarded as a way to promote data publication. Funding organizations have also taken actions to promote data as formal products of scientific research. For example, the National Science Foundation in United States now allows funding applicants to list data and software programs as products in their bio-sketches.      
A data repository has both data providers and data users. Accordingly, there are issues to be considered for both data publication and data citation. If a registered dataset is tagged with metadata such as contributor, date, title, source, publisher, etc. and is minted a DOI, then it is intuitively citable just like a published journal paper. To promote common and machine-readable metadata items among data repositories, a global initiative, the Data Cite, has been working on standards of metadata schema and identifier for datasets since 2009. For example, Data Cite suggests five mandatory metadata items for a registered dataset: identifier, creator, title, publisher, and publication year. It also suggests a list of additional metadata items such as subject, resource type, size, version, geographical location, etc. The methodology and technology developed by Data Cite are increasing endorsed by leading data
repositories across the world, which make possible a common technological infrastructure for data citation.  Various communities have also taken efforts to promote best practices in data citation, especially the guidelines for data users. The FORCE11 published the Joint Declaration of Data Citation Principles in 2013 to promote good research practice of citing datasets. Earlier than that, in 2012, the Federation of Earth Science Information Partners (2012) published Data Citation Guidelines for Data Providers and Archives, which offers more practical details on how a published dataset should be cited. For example, it suggests seven required elements to be included in a data citation: authors, release date, title, version, archive and/or distributor, locator/identifier, and access date/time.
















5.PROPOSED SYSTEM
In our procedure comprises camera is used catching of the pictures of lecture hall image then directing pictures to picture enlargement segment. Spitting image rises identification and appreciation of the modules after theimage improvement and being present noticeable at particular time to the recorder system. The experimental setup figure2 depicted. Patterns of face pictures of an single student is stored in the databank at time ofregistration.so the faces are then recognised from that of the image then the procedure matches with the database. The attendance marked on server if any of the face identified from the database and it can be accessed by everyone for numerous reasons. This also habits the procedure that can be used for attendance. The system is also attached with the time table unit that robotically gets class at what time and what subject. The system robotically becomes presence deprived of opinions the learners and the teachers. So teachers after coming to the class when taking attendance they just press the attendance button to start the attendance procedure. This method is highly protected method here no one can give the attendance of the other and also saves a lot of time.  The presence deposited system that all right to use administrations or blood relation the learners can use for them only. The device is used to take picture that is attached to that of the system takes the pictures endlessly to identify and also to find the students those who are sitting in the classroom .For avoidance of false recognition of images skin classification method is used.This skin classification method  progresses the proficiency and the correctness that acknowledgement procedure. Mainly it is considered all other images recaps the other images then kept as black in skin classification method, it expressively improves truthfulness face tracking procedure . In the experimental arrangement show in figure1 two databases are shown. Assembling of face images and the images that are mined geographies at period procedure of registration is done by 


using of the face database .The data around instructors and learners take presence the second attendance of database is used. 



 







Data Acquisition 
Image acquisition: Image is acquire using a high definition camera which is placed in the classroom. This image is given as an input to the system. 

Dataset Creation: Dataset of students is created before the recognition process. Dataset was created only to train this system. We have created a dataset of 5 students which involves their name, roll number, department and images of student in different poses and variations. For better accuracy minimum 15 images of each students should be captured. Whenever we register student’s data and images in our system to create dataset, deep learning applies to each face to compute 128-d facial features and store in student face data file to recall that face in recognition process. This process is applies to each image taken during registration. 

Storing: We have used JSON to store the student’s data. 
JavaScript Object Notation (JSON): To represent a structured data based on JavaScript object syntax, a standard text based format is introduced. JSON is used for transmitting data in web application. It is a perfect solution for storing temporary data that’s consumed by the entity that’s creates the data. JSON can store data in String, Number, Object, Array, Boolean, Null form which means it has limitation of storing data in functions, dates and undefined data form. If you are trying to store or exchange data in functions or dates than JSON is not right choice for you

 


Flow digram

 








6.FACE RECOGNIZATION PROCESS
Face Detection and Extraction: Face detection is important as the image taken through the camera given to the system, face detection algorithm applies to identify the human faces in that image, the number of image processing algorithms are introduce to detect faces in an images and also the location of that detected faces. We have used HOG method to detect human faces in given image.  
Face Positioning:  There are 68 specific points in a human face. In other words we can say 68 face landmarks. The main function of this step is to detect landmarks of faces and to position the image. A python script is used to automatically detect the face landmarks and to position the face as much as possible without distorting the image. 
Face Encoding: Once the faces are detected in the given image, the next step is to extract the unique identifying facial feature for each image. Basically whenever we get localization of face, the 128 key facial point are extracted for each image given input which are highly accurate and these 128-d facial points are stored in data file for face recognition.



Face matching: This is last step of face recognition process. We have used the one of the best learning technique that is deep metric learning which is highly accurate and capable of outputting real value feature vector. Our system ratifies the faces, constructing the 128d embedding (ratification) for each.  Internally compare_faces function is used to compute the Euclidean distance between face in image and all faces in the dataset. If the current image is matched with the 60% threshold with the existing dataset, it will move to attendance marking.

Attendance Marking 
Once the face is identify with the image stored in JSON file, python generate roll numbers of present students and return that, when data is returned, the system generates attendance table which includes the name, roll number, date, day and time with corresponding subject id. And then passes the data to python to store the table into an excel sheet automatically. Each sheet is saved according to the subjects which already entered by the administrator, for example when system generates excel sheet by sending the compiled sheet in an array to python, the python first checks whether there exit any excel sheet of that date, if yes then it create separate worksheet by subject id, so that attendance is differentiated for different subjects.















 













7.SOFTWARE SYSTEM PROCEDURE
In the first step the image is taken from the camera and as image is taken with help of camera there will be lighting effects that in image that is captured .Because of this there will be dissimilar lighting condition and there will also be some noise that has disconnected from further phases. For elimination of noise medium filter taken and unlikeness enlargement three-dimensional area histogram normalization has been taken. Here in this next is explanation of that of the every phase algorithms that are directly above pictures after every process.

The algorithm that has been taken for is subdivided from system process.
 Subsequent stages are comprised from the system algorithm. 
1)	Image Acquisition 
Image procurement  Image Procurement is also called as image acquisition.  The picture is settled that of the pixels that are collected.   
2)	Histogram Normalisation
The spitting image that is taken rarely consume brilliance else dimness that is used for decent results. The key is the RGB one .The picture then renovated grey picture the progress. 
For dissimilarity enhancement in spatial domain histogram normalization is a good method. This helps to identify the learners meeting on rear rows are obviously realized now. 
From this straightforwardly perceived the people meeting on rear rows are evidently met. So we can without difficulty recognised. 
At hand also other procedures that are used creating of picture illumination system in a different way .
3)	Noise filtering 
There may exist a lot of causes of sound in the participation image when we 
take picture with the camera. Many methods available there is one method that 
is low permit clarifying in the frequency area it might be a virtuous choice but this also leads to the elimination of some significant information in image. Medium cleaning is used in our system for the reason for sound dismissal in form of normalised spitting image.  
4)	Classification of skin
This method is to improve the adeptness of face identification procedure. It is castoff to rise effectiveness of the face identification procedure. The scanning of the process of faces, viola and jonnes procedure is recycled for discovering and exactness is developed if membrane categorized . First pixel is systematically interconnected skin and transfigures white and remaining black. The thresholding of skin colours is done by the second image
Face detection method notices the segment faces by shaping spheres on image having pictures of learners. Haar classifiers are used for the recognition of the faces. After performing the classification of skin the degree of algorithm has been enriched. This face detection algorithm are first used for changeability of images with different action and then it used for illumination conditions and this also applied for detecting the expressions on face in existent phase audio-visual. First this procedure used for pictures and functioned for classroom of image for finding of multiple faces in the image. Next step after discovery from images the faces are collected for identifying faces. This procedure winding  is recycled to rise the speed of the algorithm. The image that is collected is then allotted to distinct drift because of purpose of knowledge reasons  
5)	Attendance and face recognition
Next stage that used after the image recognition method is face identification method. It can be accomplished by collecting the image that is first identified face from image then is matched with images that are in the database. In this manner the images the learners are verified one after another with record
that is having faces by using Eigen image technique the being present noticeable on the system. This approach termed as collection of region attention



8.SAMPLE OUTPUT
Home page:
 
Signup Page:
 
Login Page:
 


Dashboard:
 
Add 	Student:
 

Take Image:
 
Successfully filled student details:
 









Train Database:
 
Take Attendance:
 




View Attendance:
 
Send Mail:
 


9. CONCLUSION
Smart attendance management system is designed to solve the issues of existing manual systems. We have used face recognition concept to mark the attendance of student and make the system better. The system performs satisfactory in different poses and variations. In future this system need be improved because these system sometimes fails to recognize students from some distance, also we have some processing limitation, working with a system of high processing may result even better performance of this system. 

