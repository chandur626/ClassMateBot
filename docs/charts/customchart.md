# About $customchart
This command lets admins make a custom chart of any type with any size of dataset

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/chandur626/ClassMateBot/blob/main/bot.py) and [here](https://github.com/chandur626/ClassMateBot/blob/main/cogs/charts.py).

# Code Description
## Functions

1. def customchart(self, ctx, title: str, chart: str, datacount: int, *args): <br>
This function creates a graph by getting the name of the chart, the type of chart the admin wants, data point count, data labels, and the data points for each data label. 

# How to run it? (Small Example)
Enter space-separated: "$grades (type of chart) (# students with A) (# students with B) (# students with C) (# students with D) (# students with F)

FORMAT: $customchart title (1 word), chart_type (pie, bar, line), # of categories, name for Category 1, name for Category 2, name for Category N...(continue for however many categories there are), number for Category 1, number for Category 2, number for Category N..."
(continue for however many categories there are) EX. If # of categories is 5, there should be 5 category names and 5 category numbers"
```
$customchart class_average_between_6_semesters bar 6 S18 F18 S19 F19 S20 F20 90 91 92 93 94 95
```
Successful execution will show the custom chart

![customchart](https://user-images.githubusercontent.com/60410421/140682904-4b3ca435-d34d-427c-868b-0fa78a0e2274.gif)
