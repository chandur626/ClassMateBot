# About $checkchart
This command lets students/users check any chart if previously stated

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/chandur626/ClassMateBot/blob/main/bot.py) and [here](https://github.com/chandur626/ClassMateBot/blob/main/cogs/charts.py).

# Code Description
## Functions

1. def checkchart(self, ctx, name: str): <br>
This function checks if any chart with the given name exists in users.json and if so, outputs the corresponding chart. 

# How to run it? (Small Example)
Enter space-separated: "$checkchart (name of the chart you are looking for)
```
$checkattendance
```
Successful execution will show a chart or a message saying the chart being searched doesn't exist
