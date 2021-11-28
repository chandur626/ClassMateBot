# About $auto-assign
This command lets the Professor or TA's automatically assign students into groups (i.e if a student is not already part of a group).
Groups with maximum vacant positions are given the first priority.

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/cogs/groups.py)

# Code Description
## Functions
automatic_grouping(self, ctx): <br>

This function takes as arguments the values provided by the constructor through self, context in which the command was called. No additional arguments are needed

# How to run it? (Small Example)
Let's say that you are in the server that has the Classmate Bot active and online. All you have to do is dm bot and
enter the command 'auto-assign'.
```
$auto-assign
```
Successful execution of this command will display the names of the students and the groups they are assigned to along with a success message.
If all students are already part of some group, a message is displayed notifying that they weren’t any modifications made.

![$auto-assign](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/data/media/Auto-grouping.gif)
