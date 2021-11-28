# About $find-group
This command lets us find the group number a student belongs to.

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/cogs/groups.py)

# Code Description
## Functions
find_group(self, ctx,*,name : str): <br>
This function takes as arguments the values provided by the constructor through self, context in which the command was called , * to take input of string arguments including spaces and name of the student.

# How to run it? (Small Example)
Let's say that you are in the server or bot dm that has the Classmate Bot active and online. All you have to do is 
enter the command 'find-group <student-name>'.
```
$find-group <student-name>
```
Successful execution of this command will display the group number of the given student name or asks to re-enter the command  with proper arguments.

![$group HW](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/data/media/Find-group.gif)
