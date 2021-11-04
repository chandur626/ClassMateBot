# Copyright (c) 2021
"""This functionality tracks student activity and rewards students
 with level ups. Students can track their activities with $level and see their
 progress towards the next level. The bot continually listens for user messages
 and adds it to the user's personal experience/level score"""
from math import floor
import discord
from discord.ext import commands
import json
import sys
import os
from datetime import datetime


class userRanking(commands.Cog):
    """userRanking ...
    Holds commands to track user participation
    Args:
        self: used to access parameters passed to the class through the constructor
        bot: discord bot context
    """
    def __init__(self, client):
        cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.chdir(cur_dir)
        """initialization for userRanking"""
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """on_member_join ...
        Sees a user has joined and adds their information
        Args:
            self: used to access parameters passed to the class through
            member: used to access the values passed through the current context
        """
        with open('data/participation/users.json', 'r') as f:
            users = json.load(f)

        await self.update_data(users, member)

        with open('data/participation/users.json', 'w') as f:
            json.dump(users, f, indent=4)

    @commands.Cog.listener()
    async def on_message(self, message):
        """on_message ...
        Sees a user has messaged and adds their information
        Args:
            self: used to access parameters passed to the class through
            message: used to access the values passed through the current context
        """
        if not message.author.bot:
            cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            os.chdir(cur_dir)
            with open('data/participation/users.json', 'r') as f:
                users = json.load(f)
            await self.update_data(users, message.author)
            await self.add_experience(users, message.author)
            await self.level_up(message, users)

            with open('data/participation/users.json', 'w') as f:
                json.dump(users, f, indent=4)

    async def update_data(self, users, user):
        if not str(user.id) in users:
            users[str(user.id)] = {}
            users[str(user.id)]['experience'] = 0
            users[str(user.id)]['level'] = 1

    async def add_experience(self, users, user):
        users[str(user.id)]['experience'] += 15

    async def level_up(self, ctx, users):
        user = ctx.author
        experience = users[str(user.id)]['experience']
        lvl = users[str(user.id)]['level']
        lvl_end = 5 * (lvl ** 2) + (50 * lvl) + 100

        if lvl_end <= experience:
            # channel = self.client.get_channel(900580609540362303)
            channel = discord.utils.get(ctx.guild.channels, name="general")
            await channel.send('{} has levelled up to level {} ! 🙌'.format(user.mention, lvl + 1))
            users[str(user.id)]['level'] = lvl + 1
            users[str(user.id)]['experience'] -= lvl_end

    async def to_integer(self, dt_time):
        answer = 100000000 * dt_time.year + 1000000 * \
                 dt_time.month + 10000 * dt_time.day + 100 * dt_time.hour + dt_time.minute
        return int(answer)

    @commands.command()
    async def level(self, ctx, user: discord.Member = None):
        """level ...
        presents level information about a user
        Args:
            self: used to access parameters passed to the class through
            ctx: used to access the values passed through the current context
            user: the discord member
        """
        with open('data/participation/users.json', 'r') as f:
            users = json.load(f)

        if user is None:
            if not str(ctx.author.id) in users:
                users[str(ctx.author.id)] = {}
                users[str(ctx.author.id)]['experience'] = 0
                users[str(ctx.author.id)]['level'] = 0

            user = ctx.author
            lvl = int(users[str(ctx.author.id)]['level'])
            exp = int(5 * (lvl ** 2) + (50 * lvl) + 100)  # XP cap
            experience = int(users[str(user.id)]['experience'])
            boxes = floor((experience * 20) / exp)
            val = 5 * (lvl ** 2) + (50 * lvl) + 100
            embed = discord.Embed(Title=f"**{user}'s Rank**",
                                  Description=f"Experience: {lvl}/{exp}", color=0x0091ff)
            embed.set_thumbnail(url=f"{user.avatar_url}")
            embed.add_field(name=f"**{user}'s Rank**",
                            value="🙌  ", inline=False)
            embed.add_field(name="Level",
                            value=f"**{users[str(user.id)]['level']}**", inline=True)
            embed.add_field(name="Experience",
                            value=f"**{str(int(users[str(user.id)]['experience']))} / {exp}**",
                            inline=True)
            embed.add_field(name="Progress Bar",
                            value=boxes * ":blue_square:" + (20 - boxes) *
                                    ":white_large_square:", inline=False)
            embed.set_footer(text="Contribute more to level up!")
            await ctx.send(embed=embed)

        else:
            if not str(user.id) in users:
                users[str(user.id)] = {}
                users[str(user.id)]['experience'] = 0
                users[str(user.id)]['level'] = 0
                users[str(user.id)]['LastMessage'] = await self.to_integer(datetime.now())
            lvl = int(users[str(user.id)]['level'])
            exp = int(5 * (lvl ** 2) + (50 * lvl) + 100)
            experience = int(users[str(user.id)]['experience'])
            boxes = floor((experience * 20) / exp)

            embed = discord.Embed(Title=f"**{user}'s Rang**",
                                  Description=f"Experience: {lvl}/"
                                              f"{5 * (lvl ** 2) + (50 * lvl) + 100}",
                                  color=0x0091ff)
            embed.set_thumbnail(url=f"{user.avatar_url}")
            embed.add_field(name=f"**{user}'s Rang**", value="🙌  ", inline=False)
            embed.add_field(name="Level",
                            value=f"**{users[str(user.id)]['level']}**", inline=True)
            embed.add_field(name="Experience",
                            value=f"**{str(int(users[str(user.id)]['experience']))} / {exp}**",
                            inline=True)
            embed.add_field(name="Progress Bar",
                            value=boxes * ":blue_square:" + (20 - boxes) *
                                  ":white_large_square:", inline=False)
            embed.set_footer(text="Contribute more to level up!")
            await ctx.send(embed=embed)

        with open('data/participation/users.json', 'w') as f:
            json.dump(users, f, indent=4)

    @commands.command()
    async def add_database(self, ctx, user: discord.Member):
        """add_database ...
        Adds user to the database
        Args:
            self: used to access parameters passed to the class through
            ctx: used to access the values passed through the current context
            user: the discord member to be added
        """
        with open('data/participation/users.json', 'r') as f:
            users = json.load(f)
        if not str(user.id) in users:
            users[str(user.id)] = {}
            users[str(user.id)]['experience'] = 0
            users[str(user.id)]['level'] = 0
            users[str(user.id)]['LastMessage'] = await self.to_integer(datetime.now())
            await ctx.send("added to database!")
        else:
            await ctx.send("already in database!")

        with open('data/participation/users.json', 'w') as f:
            json.dump(users, f, indent=4)



def setup(bot):
    """setup ...
    Add the file to the bot's cog system
    Args:
        bot: bot context setup
    """
    bot.add_cog(userRanking(bot))
