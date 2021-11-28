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

        await ctx.send(embed=embed)
        await ctx.send(f"{shortened_link}")


def setup(bot):
    bot.add_cog(CalAttendance(bot))
