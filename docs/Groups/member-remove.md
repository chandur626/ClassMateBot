# About Member Remove Event

This event is triggered when a member leaves the server. If assigned to a group, the member will be removed from it creating vacant positions for others.

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/cogs/groups.py)

# Code Description
## Functions
on_member_remove(self,member): <br>
This function takes as arguments the values provided by the constructor through self and a discord member object. No additional arguments are needed

# How does it work? (Small Example)
Let's say that you are in the server or bot dm that has the Classmate Bot active and online. You also have an another member who is part of some group,if that
member leaves the server, use $find-group command along with his name. A message will be displayed notifying that the name isn't valid.

![$group HW](https://github.com/Ashwinshankar98/ClassMateBot/blob/main/data/media/member-remove.gif)
