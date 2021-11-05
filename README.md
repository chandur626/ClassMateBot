<p align="center"><img width=100% src="https://github.com/chandur626/ClassMateBot/blob/README-update/data/title.png"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6+-yellow.svg)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/418217645.svg)](https://zenodo.org/badge/latestdoi/418217645)
[![Python application](https://github.com/chandur626/ClassMateBot/actions/workflows/main.yml/badge.svg)](https://github.com/chandur626/ClassMateBot/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/chandur626/ClassMateBot/branch/main/graph/badge.svg?token=2SKMHUAZV8)](https://codecov.io/gh/chandur626/ClassMateBot)
<p align="center">
  <a href="#dart-basic-overview">Basic Overview</a>
  ::
  <a href="#orange_book-description">Description</a>
  ::
  <a href="#arrow_down-installation">Installation</a>
  ::
  <a href="#computer-commands">Commands</a>
  ::
  <a href="#earth_americas-future-scope">Future Scope</a>
  ::
  <a href="#pencil2-contributors">Contributors</a>
  
</p>

---

## :dart: Basic Overview

https://user-images.githubusercontent.com/60410421/140225894-5da3c56e-829f-4407-ba72-c0878081e388.mp4



This project helps to improve the life of students, TAs and teachers by automating many mundane tasks which are sometimes done manually. ClassMateBot is a discord bot made in Python and could be used for any discord channel. 

In Iteration 2, we added 6 main quality-of-life improvements to be more useful to admins (Professor and TA) and students alike.

---

## :orange_book: Description

There are three basic user groups in a ClassMateBot, which are Students, Professor and TAs. Some basic tasks for the bot for the students user group should be automating the task of group making for projects or homewroks, Projection deadline reminders, etc. For TAs it is taking up polls, or answering FAQs asked by the students. Our ClassMateBot focuses on the student side of the discord channel, i.e. currently it focuses on the problems faced by the students while using these discord channels.The user stories covered here would be more concerned about the activities for the channel for Software Engineering class in North Carolina State University for the Fall 2021 semester.

For Iteration 2, we aimed to expand the Bot's functionality so Professors and TAs can be more efficient and widened our scope outside of just our Software Engineering class. We researched how different classes in different programs (ex. Social Sciences, English, Humanities) could benefit from an improved bot. We believe our bot's commands like auto-grouping students, sending emails directly from discord to students, sentiment analysis, visualizing data/statistics, greatly benefits class management and information distribution. 

---
### 0 - Original Features
You can find the Original Features from Iteration 1 [here](https://github.com/chandur626/ClassMateBot/blob/README-update/docs/Iteration1Features.md)

### 1 - Auto-Grouping Students

Auto-Grouping command allows TAs and Professors to automatically assign students into groups for project works. The Iteration 1 provided join command which can be used by students to join a specific group. Post deadline, If students have not yet joined a group, then the TA can simply use the auto-grouping command to assign those students into groups having vacant positions. Groups with maximum vacant positions are given the first priority. A simple example is shown below :


![$auto-assign](https://github.com/chandur626/ClassMateBot/blob/main/data/media/Auto-grouping.gif)


### 2 - Email Functionality
Students can now configure their email address to receive attachments and various notifications such as reminders. Students can create or update the configured email address using the below-mentioned commands in the Version 2 commands section.

<p align="left"><img width=75% src="https://github.com/chandur626/ClassMateBot/blob/main/data/media/Email_Address.gif"></p>

Students can also get the attachments mailed to their configured email address by reacting with white_heavy_mark to the attachment message.

<p align="left"><img width=75% src="https://github.com/chandur626/ClassMateBot/blob/main/data/media/Email_Attachment.gif"></p>

### 3 - Sentiment Analysis 
Students can analyze the sentiment of the message. This will give the sentiment and the polarity score of the message. 

Students can analyze the sentiment using the below comments. 

<p align="left"><img width=75% src="https://github.com/chandur626/ClassMateBot/blob/main/data/media/Sentiment_Analysis.gif"></p>


### 4 - Data Visualization

Admins (In this case, TAs and Professors) can quickly make graphcs and charts directly in discord to share with students/users. Admins can use this feature to share grade distributions, lecture participation/attendance, or other course statistics. Pre-existing graph commands (such as grades or attendance) were made for ease-of-use so there are less command arguments for the admin to type. If the admin requires a custom chart, a command exists to do just that where admins can specify all data labels and information. All charts are named and stored into a json file when they are created. Students have acess to a command that allows them to view previously presented charts. 
<p align="left"><img width=75% src="https://user-images.githubusercontent.com/60410421/139969198-dcd79af8-eb59-4fa7-934b-aca7023574a0.gif"></p>

### 5 - Link Collection

Another problem that the students face is that they cannot save all the messages which contain important URLs that are helpful to them so we have built a user command where a student can retrieve all the links which are shared in the group with one click. This command lets users access all messages which contain URLs. The messages Containing URL are automatically get appended in a file and the file is attached when the `$send_links` command is input.

<p align="left"><img width=75% src="https://github.com/chandur626/ClassMateBot/blob/main/data/media/Links.gif"></p>

### 6 - User Participation Ranking

Users are all given a participation rank the moment they join a discord community with the ClassMateBot. As the user participates in the server, such as replying to the professor, answering questions, helping other students, etc., they increase their participation score. Courses within the Humanities and Social Sciences rely on student participation. Professors can use this feature to check which students are participating more and factor that into a class participation grade. Users can also check which level/rank they hold. Admins also have the ability to add/remove points from users.
<p align="left"><img width=75% src="https://user-images.githubusercontent.com/60410421/139969309-90b590b4-fe72-45ca-9956-b65bbf6db7b9.gif"></p>

---


## :arrow_down: Installation

1. Clone the Github repository to a desired location on your computer. You will need [git](https://git-scm.com/) to be preinstalled on your machine. Once the repository is cloned, you will then ```cd``` into the local repository.
```
git clone https://github.com/War-Keeper/ClassMateBot.git
cd (into the ClassMateBot folder. If you type the commmand "ls", you should see the contents of the ClassMateBot folder)
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of those.
```
pip install -r requirements.txt
```
3. Once the installation is complete with requirements installed, you have to generate a .env file and place it in the root of your project folder. The .env file contains your bot TOKEN and your Discord GUILD (guild is your discord server name). [Check out this video](https://youtu.be/nW8c7vT6Hl4?t=256) to see how you can setup your discord developer settings and .env file. You may also contact Niraj Lavani (nrlavani@ncsu.edu) for additional information on this process. 
```
PLEASE DO NOT SHARE THE TOKEN ONLINE, 
DO NOT UPLOAD TO GITHUB OR ELSE THE TOKEN WILL AUTOMATICALLY GET DESTROYED AND HAS TO BE REGENERATED.
```
4. Once all the requirements are installed, use the python command to run the ```bot.py``` file.
```
python3 bot.py 
```

---
## Version 2 Commands
Data Visualization

:open_file_folder: [$grades command](https://github.com/chandur626/ClassMateBot/blob/main/docs/charts/grades.md)

:open_file_folder: [$attendance command](https://github.com/chandur626/ClassMateBot/blob/main/docs/charts/attendance.md)

:open_file_folder: [$customchart command](https://github.com/chandur626/ClassMateBot/blob/main/docs/charts/customchart.md)

:open_file_folder: [$checkgrade command](https://github.com/chandur626/ClassMateBot/blob/main/docs/charts/checkgrade.md)

:open_file_folder: [$checkattendance command](https://github.com/chandur626/ClassMateBot/blob/main/docs/charts/checkattendance.md)

:open_file_folder: [$checkchart command](https://github.com/chandur626/ClassMateBot/blob/main/docs/charts/checkchart.md)


User Ranking

:open_file_folder: [$levels command](https://github.com/chandur626/ClassMateBot/blob/main/docs/userRanking/level.md)

:open_file_folder: [$add_database command](https://github.com/chandur626/ClassMateBot/blob/main/docs/userRanking/add_database.md)


Email Specification

:open_file_folder: [$add_email_command](https://github.com/chandur626/ClassMateBot/blob/main/docs/EmailSpecification/add_email.md)

:open_file_folder: [$view_email_command](https://github.com/chandur626/ClassMateBot/blob/main/docs/EmailSpecification/view_email.md)

:open_file_folder: [$update_email command](https://github.com/chandur626/ClassMateBot/blob/main/docs/EmailSpecification/update_email.md)

:open_file_folder: [$delete_email_command](https://github.com/chandur626/ClassMateBot/blob/main/docs/EmailSpecification/delete_email.md)


Auto-Grouping

:open_file_folder: [$auto-assign_command](https://github.com/chandur626/ClassMateBot/blob/main/docs/Groups/auto-assign.md)

:open_file_folder: [$find-group_command](https://github.com/chandur626/ClassMateBot/blob/main/docs/Groups/find-group.md)

:open_file_folder: [member remove event](https://github.com/chandur626/ClassMateBot/blob/main/docs/Groups/member-remove.md)


Sentiment Analysis



Link Saving

:open_file_folder: [member remove event](https://github.com/chandur626/ClassMateBot/blob/main/docs/StoreLinks/Links.md)



## Original Commands
For the newComer.py file

:open_file_folder: [$verify command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Verification/verify.md)

For the voting.py file

:open_file_folder: [$projects command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Voting/projects.md)

:open_file_folder: [$vote command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Voting/vote.md)

For the deadline.py file

:open_file_folder: [$add_homework command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/add_homework.md)

:open_file_folder: [$change_reminder_due_date command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/change_reminder_due_date.md)

:open_file_folder: [$clear_all_reminders command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/clear_all_reminders.md)

:open_file_folder: [$course_due command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/course_due.md)

:open_file_folder: [$delete_reminder command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/delete_reminder.md)

:open_file_folder: [$due_this_week command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/due_this_week.md)

:open_file_folder: [$due_today command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/due_today.md)

:open_file_folder: [$list_reminders command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Reminders/list_reminders.md)

For the pinning.py file

:open_file_folder: [$pin command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/PinMessage/pin.md)

:open_file_folder: [$unpin command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/PinMessage/unpin.md)

:open_file_folder: [$pinnedmessages command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/PinMessage/pinnedmessages.md)

:open_file_folder: [$updatepin command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/PinMessage/updatepin.md)

For the groups.py file

:open_file_folder: [$group command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Groups/group.md)

:open_file_folder: [$join command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Groups/join.md)

:open_file_folder: [$remove command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Groups/remove.md)


---

## :earth_americas: Future Scope
[Project 3](https://github.com/chandur626/ClassMateBot/projects/2) TODO tasks are located in the Projects tab. 

---

## :pencil2: Contributors
### Version 2 

[Chandrahas Reddy Mandapati](https://github.com/chandur626)

[Sri Pallavi Damuluri](https://github.com/SriPallaviDamuluri)

[Niraj Lavani](https://github.com/nirajlavani)

[Harini Bharata](https://github.com/HariniBharata)

[Sandesh Aladhalli Shivarudre Gowda](https://github.com/05sandesh)

### Version 1

[Chaitanya Patel](https://github.com/War-Keeper)

[Evan Brown](https://github.com/wevanbrown)

[Kunwar Vidhan](https://github.com/kunwarvidhan)

[Sunil Upare](https://github.com/sunil1511)

[Sumedh Salvi](https://github.com/salvisumedh2396)
