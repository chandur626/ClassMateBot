<p align="center"><img width=100% src="https://github.com/chandur626/ClassMateBot/blob/README-update/data/title.png"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6+-yellow.svg)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5539956.svg)](https://doi.org/10.5281/zenodo.5539956)
![Build Status](https://github.com/War-Keeper/ClassMateBot/actions/workflows/main.yml/badge.svg)
[![codecov](https://codecov.io/gh/War-Keeper/ClassMateBot/branch/main/graph/badge.svg)](https://codecov.io/gh/War-Keeper/ClassMateBot)

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

In Iteration 2, we added 5 main quality-of-life improvements to be more useful to admins (Professor and TA) and students alike.

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


### 2 - Email Functions (Chandrahas) 

### 3 - Sentiment Analysis (Harini)

### 4 - Data Visualization

<p align="left"><img width=75% src="https://user-images.githubusercontent.com/60410421/139969198-dcd79af8-eb59-4fa7-934b-aca7023574a0.gif"></p>

Admins (In this case, TAs and Professors) can quickly make graphcs and charts directly in discord to share with students/users. Admins can use this feature to share grade distributions, lecture participation/attendance, or other course statistics. Pre-existing graph commands (such as grades or attendance) were made for ease-of-use so there are less command arguments for the admin to type. If the admin requires a custom chart, a command exists to do just that where admins can specify all data labels and information. All charts are named and stored into a json file when they are created. Students have acess to a command that allows them to view previously presented charts. 

### 5 - Link Collection (Sandesh)

### 6 - User Participation Ranking

<p align="left"><img width=75% src="https://user-images.githubusercontent.com/60410421/139969309-90b590b4-fe72-45ca-9956-b65bbf6db7b9.gif"></p>

Users are all given a participation rank the moment they join a discord community with the ClassMateBot. As the user participates in the server, such as replying to the professor, answering questions, helping other students, etc., they increase their participation score. Courses within the Humanities and Social Sciences rely on student participation. Professors can use this feature to check which students are participating more and factor that into a class participation grade. Users can also check which level/rank they hold. Admins also have the ability to add/remove points from users.

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

:open_file_folder: [$grades command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Verification/verify.md)

:open_file_folder: [$attendance command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Verification/verify.md)

:open_file_folder: [$customchart command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Verification/verify.md)

:open_file_folder: [$checkgrade command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Verification/verify.md)

:open_file_folder: [$checkattendance command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Verification/verify.md)

:open_file_folder: [$checkchart command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Verification/verify.md)


User Ranking

:open_file_folder: [$levels command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Verification/verify.md)

:open_file_folder: [$add_database command](https://github.com/War-Keeper/ClassMateBot/blob/main/docs/Verification/verify.md)


Email Verification



Auto-Grouping

:open_file_folder: [$auto-assign_command](https://github.com/chandur626/ClassMateBot/blob/main/docs/Groups/auto-assign.md)

:open_file_folder: [$find-group_command](https://github.com/chandur626/ClassMateBot/blob/main/docs/Groups/find-group.md)

:open_file_folder: [member remove event](https://github.com/chandur626/ClassMateBot/blob/main/docs/Groups/member-remove.md)


Sentiment Analysis



Link Saving



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
[Project 2](https://github.com/War-Keeper/ClassMateBot/projects/2) and [Project 3](https://github.com/War-Keeper/ClassMateBot/projects/3) user stories and TODO tasks are located in the Projects tab. 

---

## :pencil2: Contributors

<table>
  <tr>
    <td align="center"><a href="https://github.com/War-Keeper"><img src="https://avatars.githubusercontent.com/u/87688584?v=4" width="75px;" alt=""/><br /><sub><b>Chaitanya Patel</b></sub></a></td>
    <td align="center"><a href="https://github.com/wevanbrown"><img src="https://avatars.githubusercontent.com/u/89553353?v=4" width="75px;" alt=""/><br /><sub><b>Evan Brown</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/kunwarvidhan"><img src="https://avatars.githubusercontent.com/u/51852048?v=4" width="75px;" alt=""/><br /><sub><b>Kunwar Vidhan</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/sunil1511"><img src="https://avatars.githubusercontent.com/u/43478410?v=4" width="75px;" alt=""/><br /><sub><b>Sunil Upare</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/salvisumedh2396"><img src="https://avatars.githubusercontent.com/u/72020618?s=96&v=4" width="75px;" alt=""/><br /><sub><b>Sumedh Salvi</b></sub></a><br /></td>
  </tr>
</table>
