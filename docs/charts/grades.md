# About $grades
This command lets admins make a quick grade distribution chart

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/chandur626/ClassMateBot/blob/main/bot.py) and [here](https://github.com/chandur626/ClassMateBot/blob/main/cogs/charts.py).

# Code Description
## Functions

1. def grades(self, ctx, chart: str, aGrade: int, bGrade: int, cGrade: int, dGrade: int, fGrade: int): <br>
This function creates a graph by getting the type of chart the admin wants, and the data points for each grade. 

# How to run it? (Small Example)
Enter space-separated: "$grades (type of chart) (# students with A) (# students with B) (# students with C) (# students with D) (# students with F)
```
$verify grades pie 50 40 30 20 10
$verify grades line 10 20 30 40 50
```
Successful execution will show a a grade distribution chart
<p align="left"><img width=75% src="https://user-images.githubusercontent.com/60410421/139969198-dcd79af8-eb59-4fa7-934b-aca7023574a0.gif"></p>
