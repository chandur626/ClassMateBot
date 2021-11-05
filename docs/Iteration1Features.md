## Features from Iteration 1

### 1 - Student Verification
Once the new member joins the server, before giving them the access to the channels there is a need to get the real full name of the member to map it with the discord nick name. This mapping can later be used for group creation, voting and so on. To do this we first assign the unverified role to the new comer and then ask them to verify their identity using $verify command. If that goes through, the member is assigned a student role and has full access to the server resources. The bot then welcomes the member and also provides important links related to the course. A little example is provided below.
![$verify Jane Doe](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/verify.gif)

### 2 - Project Voting
The most important task in the upcoming semester that the bot automates is Project Voting which takes place at the end of the month of September and October. Our ClassMateBot allows the student to vote for a particular project which they would like to work on in the coming cycle. This task if done manually could be tedious as the students would have to wait for the TAs or Professor to announce which project they would be getting if voting is done manually. But the bot automates this process and would give out the results as soon as all the students have voted for their choices. A little example is provided below.
![$vote HW](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/vote.gif)

### 3 - Deadline Reminder
Next important thing our project covers is the Deadline reminder feature of our bot. Whenever a homework or project deadline is close the bot itself sends out a reminder to all the students so that they could submit their work on time. This feature also lets the students add other reminders along with the scheduled ones. For example, HW4 is due on 7th october, along with that the student is working on different assignments or homeworks of other subjects then they could add the other reminders too so that they are in touch with all their pending work. A little example is provided below.
![$addhw CSC510 HW2 SEP 25 2024 17:02](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/addhomework.gif)

### 4 - Personally Pinning Messages
Another problem that the students face is that they cannot pin the important messages which they could come back to if they need so. This could be done through the bot as the students could send in the link of the message they would want to pin and the bot would do that. This way all the students could pin the messages personally through the bot. The pinned messages of other students would not be visible to the current user as we have added the validation of only showing the reminders added by the user not by other students. A little example is provided below.
![$pin HW https://discordapp.com/channels/139565116151562240/139565116151562240/890813190433292298 HW8 reminder](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/pin.gif)

### 5 - Group Creation
Another unique and useful feature of our ClassMateBot is that it helps the students in the process of group making for their projects. Through this feature the bot could help the students to identify other members of the class who have the same requirements and acts as a medium to connect them initially. Afterwards, they can talk to each other in any way possible. This feature is also helpful for times when a person is randomly assigned to a group then the mebers could ask the bot to connect them with the new member and this would not only save time for the students but also, saves effort as many times students do not have their names as their usernames on discord. Through this students can join, leave or connect with others. A little example is provided below. 
![$join HW](https://github.com/War-Keeper/ClassMateBot/blob/main/data/media/join.gif)
