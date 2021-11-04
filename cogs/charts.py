"""
This functionality creates charts for the admin to quickly present to the rest
of the server. Simple charts like grades and attendance are made for quick access
while custom chart command is used to make any kind of chart. Students can
recall the chart presented by admins at any time by providing a name.
"""
import json
from discord.ext import commands
from quickchart import QuickChart
import pyshorteners


class Charts(commands.Cog):
    """Class provides several methods to manage charting."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="grades",
                      help="View grade distribution; FORMAT (7 inputs): "
                           "chart_type (pie, bar, line), title (1 word),"
                           "number of As, number of Bs, number of Cs, "
                           "number of Ds, number of Fs")
    @commands.has_permissions(administrator=True)
    async def grades(self, ctx, chart: str,
                     a_grade: int, b_grade: int, c_grade: int, d_grade: int, f_grade: int):
        """
            Creates grades chart with given specs
            Parameters:
                ctx: used to access the values passed through the current context.
                chart: chart type
                a_grade: the number of students with an A
                b_grade: the number of students with an B
                c_grade: the number of students with an C
                d_grade: the number of students with an D
                f_grade: the number of students with an F
            Returns:
                returns a graph in the chat box
        """
        with open('data/charts/chartstorage.json', 'r', encoding='utf-8') as file:
            storage = json.load(file)
        quick_chart = QuickChart()
        quick_chart.width = 500
        quick_chart.height = 300
        quick_chart.device_pixel_ratio = 2.0
        quick_chart.config = {
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
                    "data": [a_grade, b_grade, c_grade, d_grade, f_grade]
                }]
            }
        }
        link = quick_chart.get_url()
        shortener = pyshorteners.Shortener()
        shortened_link = shortener.tinyurl.short(link)
        await self.update_chart(storage, "grades", shortened_link)
        with open('data/charts/chartstorage.json', 'w', encoding='utf-8') as file:
            json.dump(storage, file, indent=4)
        await ctx.send(f"{shortened_link}")

    @grades.error
    async def grades_error(self, ctx, error):
        """
            Finds error if grades format was wrong
            Parameters:
                ctx: used to access the values passed through the current context.
                error: the error being thrown
        """
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "FORMAT: \n --- \n$grades chart_type (pie, bar, line), title (1 word), "
                "number of As, number of Bs, number of Cs, number of Ds, number of Fs \n"
                "\n EXAMPLE: $grades bar 5 4 3 2 1")

    @commands.command(name="attendance",
                      help="View attendance; FORMAT (2 inputs):"
                           " number of attended, number of absent")
    @commands.has_permissions(administrator=True)
    async def attendance(self, ctx, attended: int, absent: int):
        """
            Creates attendance chart with given specs
            Parameters:
                ctx: used to access the values passed through the current context.
                attended: students who attended
                absent: students who were absent
            Returns:
                returns a graph in the chat box
        """
        with open('data/charts/chartstorage.json', 'r', encoding='utf-8') as file:
            storage = json.load(file)
        quick_chart = QuickChart()
        quick_chart.width = 500
        quick_chart.height = 300
        quick_chart.device_pixel_ratio = 2.0
        quick_chart.config = {
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
        link = quick_chart.get_url()
        shortener = pyshorteners.Shortener()
        shortened_link = shortener.tinyurl.short(link)
        await self.update_chart(storage, "attendance", shortened_link)
        with open('data/charts/chartstorage.json', 'w', encoding='utf-8') as file:
            json.dump(storage, file, indent=4)
        await ctx.send(f"{shortened_link}")

    @attendance.error
    async def attendance_error(self, ctx, error):
        """
            Finds error if attendance format was wrong
            Parameters:
                ctx: used to access the values passed through the current context.
                error: the error being thrown
        """
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "FORMAT: $attendance number of attended, number of absent "
                "\n EXAMPLE: $attendance 150 50")

    @commands.command()
    async def checkgrade(self, ctx):
        """
            Lets students check the grade chart
            Parameters:
                ctx: used to access the values passed through the current context.
            Returns:
                returns a graph in the chat box if grades chart exists
        """
        with open('data/charts/chartstorage.json', 'r', encoding='utf-8') as file:
            storage = json.load(file)
            if not storage or storage["grades"] == '':
                await ctx.send("No grades posted!")
            else:
                await ctx.send(f" View grade distribution: {storage['grades']['URL']}")

    @commands.command()
    async def checkattendance(self, ctx):
        """
            Lets students check the attendance chart
            Parameters:
                ctx: used to access the values passed through the current context.
            Returns:
                returns a graph in the chat box if attendance chart exists
        """
        with open('data/charts/chartstorage.json', 'r', encoding='utf-8') as file:
            storage = json.load(file)
            if not storage or storage["attendance"] == '':
                await ctx.send("No attendance chart posted!")
            else:
                await ctx.send(f" View attendance: {storage['attendance']['URL']}")

    @commands.command()
    async def checkchart(self, ctx, name: str):
        """
            Lets students check the a custom chart
            Parameters:
                ctx: used to access the values passed through the current context.
                name: the name of the chart they are looking for
            Returns:
                returns the custom chart in the chat box if it exists
        """
        with open('data/charts/chartstorage.json', 'r', encoding='utf-8') as file:
            storage = json.load(file)
            if not storage or storage[name] == '':
                await ctx.send("No chart with that name!")
            else:
                await ctx.send(f"Your requested chart: {storage[name]['URL']}")

    @checkchart.error
    async def checkchart_error(self, ctx, error):
        """
            Finds error if check chart format was wrong
            Parameters:
                ctx: used to access the values passed through the current context.
                error: the error being thrown
        """
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "FORMAT: \n --- \n$checkchart name (name of the chart) "
                "\n EXAMPLE: $checkchart attendance")

    @commands.command(name="customchart",
                      help="View grade distribution; FORMAT (many): chart_type "
                           "(pie, bar, line) title (1 word)"
                           "list data as coordinates: (a,1), (b,2), (c,3)")
    @commands.has_permissions(administrator=True)
    async def customchart(self, ctx, title: str, chart: str, data_count: int, *args):
        """
            Creates a custom chart with given specs
            Parameters:
                ctx: used to access the values passed through the current context.
                title: the name of the chart
                chart: the type of the chart
                data_count: number of data points
                *args: a list of data labels and data numbers for each label
            Returns:
                returns a graph in the chat box
        """

        if len(args) / 2 != data_count:
            raise IllegalArgumentsError

        with open('data/charts/chartstorage.json', 'r', encoding='utf-8') as file:
            storage = json.load(file)

        labels_list = []
        dataset_list = []

        for data_label in range(data_count):
            labels_list.append(args[data_label])
            print(args[data_label])

        for data_point in range(data_count, len(args)):
            dataset_list.append(args[data_point])
            print(args[data_point])

        quick_chart = QuickChart()
        quick_chart.width = 500
        quick_chart.height = 300
        quick_chart.device_pixel_ratio = 2.0
        quick_chart.config = {
            "type": "{}".format(chart),
            "data": {
                "labels": labels_list,
                "datasets": [{
                    "label": "{}".format(title),
                    "data": dataset_list
                }]
            }
        }
        link = quick_chart.get_url()
        shortener = pyshorteners.Shortener()
        shortened_link = shortener.tinyurl.short(link)

        await self.update_chart(storage, title, shortened_link)
        with open('data/charts/chartstorage.json', 'w', encoding='utf-8') as file:
            json.dump(storage, file, indent=4)
        await ctx.send(f"{shortened_link}")

    @customchart.error
    async def customchart_error(self, ctx, error):
        """
            Finds error if custom chart format was wrong
            Parameters:
                ctx: used to access the values passed through the current context.
                error: the error being thrown
        """
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "FORMAT: \n --- \n"
                "$customchart title (1 word), chart_type (pie, bar, line), "
                "# of categories,  "
                "name for Category 1, name for Category 2, name for Category N..."
                "(continue for however many categories there are),"
                "number for Category 1, number for Category 2, number for Category N..."
                "(continue for however many categories there are)"
                "\n --- \n"
                "EX. If # of categories is 5, there should be 5 category names "
                "and 5 category numbers")

    async def update_chart(self, storage, name, link):
        """
            Updates the URL of the chart
            Parameters:
                storage: the json file
                name: the name of the chart
                link: the link to the chart
        """
        if not str(name) in storage:
            storage[str(name)] = {}
        storage[str(name)]['URL'] = link

def setup(bot):
    """
        Adds the cog to the bot's list
        Parameters:
            bot: the bot adding the cog
    """
    bot.add_cog(Charts(bot))

class IllegalArgumentsError(Exception):
    """A custom illegal argument error when custom chart parameters are wrong"""
    print("custom chart arguments invalid")
