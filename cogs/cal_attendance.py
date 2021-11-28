import discord
from discord.ext import commands
import json
from quickchart import QuickChart
import pyshorteners


class CalAttendance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def takeattendance(self, ctx):
        attendees = []
        absentees = []
        wanted_channel_id = 0

        for channel in ctx.guild.channels:
            if channel.name == "General":
                wanted_channel_id = channel.id

        audio_channel = self.bot.get_channel(wanted_channel_id)
        text_channel = self.bot.get_channel(ctx.channel.id)

        embed = discord.Embed(title="Attendance Sheet",
                              colour=discord.Colour.orange())

        for attendee in audio_channel.members:
            attendees.append(attendee.name)
        if attendees:
            embed.add_field(name=f"Attendees: {len(attendees)}",
                            value='\n'.join(attendees), inline=True)
        else:
            embed.add_field(name="Attendees: 0", value="None", inline=True)

        for student in text_channel.members:
            if student.name not in attendees and not student.bot:
                absentees.append(student.name)

        if absentees:
            embed.add_field(name=f"Absentees: {len(absentees)}",
                            value='\n'.join(absentees), inline=True)
        else:
            embed.add_field(name="Absentees: 0",
                            value="None", inline=True)
        
        with open('data/charts/chartstorage.json', 'r', encoding='utf-8') as file:
            storage = json.load(file)
        quick_chart = QuickChart()
        quick_chart.width = 500
        quick_chart.height = 300
        quick_chart.device_pixel_ratio = 2.0
        quick_chart.config = {
            "type": "pie",
            "data": {
                "labels": ["Attendees", "Absentees"],
                "datasets": [{
                    "backgroundColor": ['rgb(128, 177, 229)',
                                        'rgb(250, 195, 149)'],
                    "label": "attendance",
                    "data": [len(attendees), len(absentees)]
                }]
            }
        }
        name = 'attendance'
        link = quick_chart.get_url()
        shortener = pyshorteners.Shortener()
        shortened_link = shortener.tinyurl.short(link)

        if not str(name) in storage:
            storage[str(name)] = {}
        storage[str(name)]['URL'] = shortened_link
        with open('data/charts/chartstorage.json', 'w', encoding='utf-8') as file:
            json.dump(storage, file, indent=4)
            
        await ctx.send(embed=embed)
        await ctx.send(f"{shortened_link}")


def setup(bot):
    bot.add_cog(CalAttendance(bot))
