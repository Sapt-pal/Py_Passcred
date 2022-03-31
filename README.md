# -*- Py_Passcred -*-

![GitHub last commit](https://img.shields.io/github/last-commit/Sapt-pal/Py_Passcred/?style=for-the-badge)
<br>
<br>
<br>
[![CodeFactor](https://www.codefactor.io/repository/github/sapt-pal/py_passcred/badge)](https://www.codefactor.io/repository/github/sapt-pal/py_passcred)

#### Py_PassCred PGaMA (Password Generator and Management Application)


#### _Created on Sat Sep  4 18:29:04 2021._

### @authors: Saptarshi Pal; Ishan Das
#### @Project: Py PassCred PGaMA (Password Generator and Management Application)


Index

Sl.No
Topic
Pg.No.
1.
Preface
5
2.
Introduction
6
3.
Objective
7
4.
Scope of the Project
8
5.
The Existing System
8
6.
The Proposed System
9
7.
Flowchart
10
8.
System design
11
9.
Tables and Fields for Database
12
10.
Security Control
12
11.
Hardware and Software Requirements
13
12.
Conclusion
14
13.
Bibliography
15

Py PassCred
Python and MySQL Automated Password Management
Preface
One of the most popular means of securing our online content is securing access to such content by the means of a password, be it our pictures which we cherish and enjoy but want to keep private, or certain sensitive data regarding credentials of a person, containing data identifying the person with some governmental institution, or the documents of importance which persons concerned might want to keep preserved and quickly accessible to him but not to anyone else with malicious intents.
The means used to secure data have evolved with time in accordance with security demands by the concerned clients. This requires even the client to take a definitive responsibility in the process by cooperating and complying with security policies as recommended by the organization.
People new to this rigorous system face a lot of difficulties in complying with such high demands, which though are well-meant and are intended for the welfare of their clients, are nevertheless very demanding of the average client, failing its purpose for the masses at the very start.
We recognized this problem soon and decided to simplify those tiring routines associated with generating and safe-keeping of passwords by automating almost 90% of the process with Python Programming and MySQL Database Management System (RDBMS). The software we developed as a solution to the mentioned problem is: “Py PassCred'' which helps users in either generating a strong password in accordance to the enjoinders of the most popular SOCs (Cyber Security Operations Centres) throughout the world and additionally also lets them store their credentials securely in their local system MySQL database for both ease in access and security of sensitive credentials.
In this way, the software “Py PassCred” helps users in simplifying and augmenting their cyber security.
Introduction

Nowadays, people have social media, shopping websites, and different accounts all over the internet with different login information and different passwords. Moreover, people struggle with remembering passwords and end up keeping the same password for every login information which makes all of their accounts on the internet vulnerable to a hacker attack. A strong password is always recommended but it is next to impossible for an individual to remember these passwords, that too different for every website.
 
PyPassCred solves this real-life problem quite swiftly. PyPassCred generates a strong password for a particular website and stores it in a database, which then later helps to retrieve the password when required. Custom saving of passwords for a particular website is also available. It not only helps in ensuring the cyber security of the person but also helps the individual with easy access to the credentials of a particular site. It provides an extra layer of security of the passwords with the help of a Master Password to access the database and the password generator. It makes PyPassCred more secure and safe to use.
 
PyPassCred is a virtual notebook where we note down all the passwords for different websites and keep them safe with us in a virtual house. Retrieval and Updating of password feature help the user to keep his passwords up to date with time.
 
It is the first step that every individual needs to take to ensure cyber-security for himself as well as his/her relatives and friends. This concept is the base ground of cyber-security and in present times it is essential for everyone to contribute and to take part in strengthening individuals’ cyber-security.




Objective

The security of sensitive credentials is a wearisome task which demands much of the user's valuable time and hard work in remembering them, yet it is not out of harm's way. The main goal that is to be achieved by PyPassCred is to create a system that generates a strong password and also manually receives one and stores them with proper credentials in a password-protected database. This would be an effective system that eliminates all the problems faced with password management today, by using this application people will be able to manage their credentials in a more meaningful manner. The development of a secure and accurate password generator is the first step towards a more robust, usable, and cost-efficient security system.
 
PyPassCred is useful to persons who surf the internet multiple times a day and regularly use different services on the platform which requires passwords to access the particular website. The interface and working may look very simple but it is immensely helpful for the people who spend most of the time of day in front of the screens. It will soon become an indispensable application that is required for anyone who has an active presence on the internet.
 
The system has been designed to aid in the creation of passwords that are tough enough to prevent hackers from breaking into accounts. One of the main goals that are intended to be achieved by this application is to remove all the flaws that are usually associated with creating, managing, and using passwords on a day-to-day basis. This tool will greatly reduce the likelihood of getting hacked as it creates strong and complex passwords for its users even if they do not have much knowledge about password creation.






Scope of the project
The software tool, while being quite ready to use out-of-the-box, does have abundant amounts of future development scopes. One of them is bringing out a native desktop application based on python and with MySQL integration which will further make the tool more accessible while also adding to security.  
Other aspects of up-gradation include the possibility of the development of a web-based application with python-based scripting and back-end processing systems along with an online MySQL server integration.
We also expect to regularly push updates to the online repository at Github <git-repo-link-here> which will include version advancements and feature updates.
The Existing System 
The method of creating and safe-keeping of sensitive credentials is very tedious and entails much of the users’ valuable time, yet the means is not safe enough from even the casual attacks.
In the present scenario, manual generation of passwords is much in the picture wherein the users have to apply their creative thinking and have to come up with strong passwords. The passwords may seem to be secure enough for them yet, most of the general public do not know much in detail about the various parameters of determining the strength of the passwords, nor is it possible for a human to successfully incorporate all these principles and yet create a ‘memorable’ password. Moreover, once a password is generated, safe-keeping is another task that is very important but is executed successfully by very few.
As a solution to such a scenario, we have aimed towards automating much of the work so that the user can concentrate more on their tasks than spending time on credentials.
In the Py PassCred, we take care of the principles of creating a strong password in accordance with the enjoinders of the most popular SOCs (Cyber Security Operations Centres) throughout the world. Additionally, the tool also lets users create ‘memorable’ passwords.
Proposed system
We have a better alternative to the manual maintenance of passwords namely: creating and storing passwords by automating much of the manual work using python. The automation includes the generation of random/custom passwords and then securing them in a way that ensures both quick access and also high security compared to manual storage in human/machine-readable text files.
In its present completion stage, the Python-based software tool Py PassCred helps the users automate the following:
1. Creating a new random/custom password along with corresponding credentials
2. Storing existing or new passwords and related credentials
3. *(optional/BETA) Determining effective strength of passwords from a ‘brute-force attack’ algorithm in a visual manner
Along with it,  Py PassCred also:
1. Relieves the users of unnecessary stress while choosing the right password
2. Takes away the pains taken by users in manual safe-keeping of passwords
3. Enables quicker and easier access to credentials in times of need thus saving time
4. Works offline on each machine so no risk or worry about tapping or misuse attempts
5. Entails minimal efforts and money as compared to heavy-premium paid services

Flowchart

System Design
PyPassCred has been designed in such a way that users feel comfortable while operating it and the application feels more interactive to them. This system is not sophisticated to work with, rather very simple to understand and to operate. The interface is designed to be very simple with just enough frames for generating, modifying, and retrieving the password. To create the graphic user interface of the system, we used a Python module, TKinter, which helped us to create a simple and basic user interface for the system.

With the help of Tkinter, we developed the whole system which contains multiple frames, labels, buttons, drop-down boxes, and entry widgets. For every different purpose of the application, a particular frame has been created to help the user to navigate to perform a particular activity. Moreover, all these widgets are restricted from use until the user enters the required Master Password for the application.

The image below shows the interface of the application prepared to provide the service of password managing:



Tables and fields for database
The database system used by Py PassCred is the world's most popular open-source database MySQL.
In addition to the general database management, we have also enabled the Relational-Data management feature to increase its relevance in our project.
Below is an overall Tables and Fields schema used for storing credential data of the user:



Security Control
This section of the project provides information about username and password. The user's data is secured by the database and master password , where if the user forgets his/her password , then the user can reopen it by using the master password or database password. 
Hardware and software requirements
Here as we are making this code for a computer with an Python editor (Spyder/PyCharm), which is a software indeed, so we need certain software and hardware requirements which are as follows:-
System/Application Software Requirements:
a) Supported Operating System:
•Windows 10,8,7
b) Supported Database:
•MySQL
                   *Only recommended for smaller installation(1-100) users.
•MySQL server:
                   * Version 5.7 or higher
                   * Including high availability features (Always on  availability groups, windows server, failover cluster)

System Hardware Requirements:
Small Installation(1k-10k entries, 1-100 users):
•Dual-core 2 Ghz or higher
•4GB Ram
•1GB free disk space

Medium Installation (10k+ entries, 100-1000 users):
•Dual-Core 2 Ghz or higher
•8GB Ram
•2GB Free disk space
Conclusion
 
In light of the needs of the future, Py PassCred is a highly dynamic software which has been developed with the needs of the future of security and users. This software relieves the user of the routine tasks and instead automates them so that people can focus on their more important tasks which need time and effort.
In addition to creating randomised (or as desired) memorable passwords, It also relieves the user of the pains required to safe-keep them. It is easy to use, beginner friendly, has a gentle learning curve and a lot of out of the way modifications at the users reach should they need it because the software is completely open-sourced and is a freeware whose source code is universally available (*subject to a few restrictions).
In addition to the regular updates, we also expect more of the idea to be periodically equipped with stronger security features which, in addition to enhancing the software’s usability, will also multiply its relevance and applicability in this world of rapidly advancing computer and programming systems and architecture.
We sincerely hope that our software serves our users’ requirements to the very optimum.

Bibliography
The following resources were quite helpful to us during the development of this project and we’d like to cite the following links as a small token of thanks.

Special mention to:

docs.python.org and python.org
The following websites too provided the support and resources which were helpful while completing this project:
geeksforgeeks.org
stackexchange.com
stackoverflow.com
freecodecamp.org
