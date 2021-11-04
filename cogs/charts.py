# Copyright (c) 2021
# This functionality allows admins to create graphs/charts for various reasons based on admin necessity. The main
# function is creating a custom graph all within 1 command. Shortcut commands allow admins to quickly make charts
# like a chart for grades or a chart for attendance ($grades, $attendance, respectfully). Users can also access
# previously shown charts and graphs made by admins

import json
from discord.ext import commands
from quickchart import QuickChart
import pyshorteners


class Charts(commands.Cog):
    """Charts ...
    Holds commands to make charts
    Args:
        self: used to access parameters passed to the class through the constructor
        bot: discord bot context
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="grades",
                      help="View grade distribution; FORMAT (7 inputs): chart_type (pie, bar, line), title (1 word),"
                           "number of As, number of Bs, number of Cs, number of Ds, number of Fs")
    @commands.has_permissions(administrator=True)
    async def grades(self, ctx, chart: str, aGrade: int, bGrade: int, cGrade: int, dGrade: int, fGrade: int):
        """grades ...
        Creates a grade distribution chart and saves the chart to a json file
        Args:
            self: used to access parameters passed to the class through the constructor
            ctx: used to access the values passed through the current context
            chart (String): the chart type
            aGrade (String): the number of students who got an A
            bGrade (String): the number of students who got an B
            cGrade (String): the number of students who got an C
            dGrade (String): the number of students who got an D
            fGrade (String): the number of students who got an F
        """
        with open('data/charts/chartstorage.json', 'r') as f:
            storage = json.load(f)
        qc = QuickChart()
        qc.width = 500
        qc.height = 300
        qc.device_pixel_ratio = 2.0
        qc.config = {
            "type": "{}".format(chart),
            "data": {
                "labels": ["A", "B", "C", "D", "F"],
                "datasets": [{
                    "backgroundColor": ['rgb(128, 177, 229)',
                                        'rgb(116, 232, 219)',
                                        'rgb(246, 220, 154)',
                                        'rgb(250, 195, 149)',
                                        'rgb(245, 165, 145)'],
                    "label": "grades",
                    "data": [aGrade, bGrade, cGrade, dGrade, fGrade]
                }]
            }
        }
        link = qc.get_url()
        shortener = pyshorteners.Shortener()
        shortened_link = shortener.tinyurl.short(link)
        await self.update_chart(storage, "grades", shortened_link)
        with open('data/charts/chartstorage.json', 'w') as f:
            json.dump(storage, f, indent=4)
        await ctx.send(f"{shortened_link}")

    @grades.error
    async def grades_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "FORMAT: \n --- \n$grades chart_type (pie, bar, line), title (1 word), "
                "number of As, number of Bs, number of Cs, number of Ds, number of Fs \n"
                "\n EXAMPLE: $grades bar 5 4 3 2 1")

    @commands.command(name="attendance",
                      help="View attendance; FORMAT (2 inputs): number of attended, number of absent")
    @commands.has_permissions(administrator=True)
    async def attendance(self, ctx, attended: int, absent: int):
        """grades ...
        Creates a attendance pie chart and saves the chart to a json file
        Args:
            self: used to access parameters passed to the class through the constructor
            ctx: used to access the values passed through the current context
            attended (int): number of students attended
            absent (int): number of students absent
        """
        with open('data/charts/chartstorage.json', 'r') as f:
            storage = json.load(f)
        qc = QuickChart()
        qc.width = 500
        qc.height = 300
        qc.device_pixel_ratio = 2.0
        qc.config = {
            "type": "pie",
            "data": {
                "labels": ["Attended", "Absent"],
                "datasets": [{
                    "backgroundColor": ['rgb(128, 177, 229)',
                                        'rgb(250, 195, 149)'],
                    "label": "attendance",
                    "data": [attended, absent]
                }]
            }
        }
        link = qc.get_url()
        shortener = pyshorteners.Shortener()
        shortened_link = shortener.tinyurl.short(link)
        await self.update_chart(storage, "attendance", shortened_link)
        with open('data/charts/chartstorage.json', 'w') as f:
            json.dump(storage, f, indent=4)
        await ctx.send(f"{shortened_link}")

    @attendance.error
    async def attendance_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "FORMAT: $attendance number of attended, number of absent "
                "\n EXAMPLE: $attendance 150 50")

    @commands.command()
    async def checkgrade(self, ctx):
        """checkgrade ...
        Shows the grades chart
        Args:
            self: used to access parameters passed to the class through the constructor
            ctx: used to access the values passed through the current context
        """
        with open('data/charts/chartstorage.json', 'r') as f:
            storage = json.load(f)
            if not storage or storage["grades"] == '':
                await ctx.send(f"No grades posted!")
            else:
                await ctx.send(f" View grade distribution: {storage['grades']['URL']}")

    @commands.command()
    async def checkattendance(self, ctx):
        """checkattendance ...
        Shows the attendance chart
        Args:
            self: used to access parameters passed to the class through the constructor
            ctx: used to access the values passed through the current context
        """
        with open('data/charts/chartstorage.json', 'r') as f:
            storage = json.load(f)
            if not storage or storage["attendance"] == '':
                await ctx.send(f"No attendance chart posted!")
            else:
                await ctx.send(f" View attendance: {storage['attendance']['URL']}")

    @commands.command()
    async def checkchart(self, ctx, name: str):
        """checkchart ...
        Shows the attendance chart
        Args:
            self: used to access parameters passed to the class through the constructor
            ctx: used to access the values passed through the current context
            name (str): name of the chart being searched
        """
        with open('data/charts/chartstorage.json', 'r') as f:
            storage = json.load(f)
            if not storage or storage[name] == '':
                await ctx.send(f"No chart with that name!")
            else:
                await ctx.send(f"Your requested chart: {storage[name]['URL']}")

    @checkchart.error
    async def checkchart_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "FORMAT: \n --- \n$checkchart name (name of the chart) "
                "\n EXAMPLE: $checkchart attendance")

    @commands.command(name="customchart",
                      help="View grade distribution; FORMAT (many): chart_type (pie, bar, line) title (1 word)"
                           "list data as coordinates: (a,1), (b,2), (c,3)")
    @commands.has_permissions(administrator=True)
    async def customchart(self, ctx, title: str, chart: str, datacount: int, *args):
        """customchart ...
        Creates a custom chart of any kind and saves the chart to a json file
        Args:
            self: used to access parameters passed to the class through the constructor
            ctx: used to access the values passed through the current context
            title (str): name of the chart being searched
            chart (str): the chart type
            datacount (int): number of data points/categories
            *args: Custom combination of data categories and numbers for those categories
        """

        if len(args) / 2 != datacount:
            raise IllegalArgumentsError

        with open('data/charts/chartstorage.json', 'r') as f:
            storage = json.load(f)

        labelslist = []
        datasetlist = []

        for x in range(datacount):
            labelslist.append(args[x])
            print(args[x])

        for x in range(datacount, len(args)):
            datasetlist.append(args[x])
            print(args[x])

        qc = QuickChart()
        qc.width = 500
        qc.height = 300
        qc.device_pixel_ratio = 2.0
        qc.config = {
            "type": "{}".format(chart),
            "data": {
                "labels": labelslist,
                "datasets": [{
                    "label": "{}".format(title),
                    "data": datasetlist
                }]
            }
        }
        link = qc.get_url()
        shortener = pyshorteners.Shortener()
        shortened_link = shortener.tinyurl.short(link)

        await self.update_chart(storage, title, shortened_link)
        with open('data/charts/chartstorage.json', 'w') as f:
            json.dump(storage, f, indent=4)
        await ctx.send(f"{shortened_link}")

    @customchart.error
    async def customchart_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "FORMAT: \n --- \n$customchart title (1 word), chart_type (pie, bar, line), # of categories,  "
                "name for Category 1, name for Category 2, name for Category N..."
                "(continue for however many categories there are),"
                "number for Category 1, number for Category 2, number for Category N..."
                "(continue for however many categories there are)\n --- \n"
                "EX. If # of categories is 5, there should be 5 category names and 5 category numbers")
    
    async def update_chart(self, storage, name, link):
        if not str(name) in storage:
            storage[str(name)] = {}
        storage[str(name)]['URL'] = link

def setup(bot):
    """setup ...
    Adds file to bot's cog system
    Args:
        bot: bot context setup
    """
    bot.add_cog(Charts(bot))

class IllegalArgumentsError(Exception):
    """IllegalArgumentsError ...
        Error for incorrect arguments passed into $customchart
        Args:
            Exception: The exceptinon being thrown
        """
    print("customchart arguments invalid")
    pass
