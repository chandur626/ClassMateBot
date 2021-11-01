# Copyright (c) 2021
# This functionality tracks student activity and rewards students with level ups. Students can track their activity
# with $levels and see their progress towards the next level. The bot continually listens for user messages and adds
# it to the user's personal experience/level score which is stored in data/participation/users.json
from math import floor
import discord
from discord.ext import commands
import json
from datetime import datetime

class userRanking(commands.Cog):

    def __init__(self, client):
        self.client = client

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: on_member_join(self, member)
    #    Description: Sees a user has joined and adds their information to data/participation/users.json
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - member: used to access the values passed through the current context
    # -----------------------------------------------------------------------------------------------------------------
    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('data/participation/users.json', 'r') as f:
            users = json.load(f)

        await self.update_data(users, member)

        with open('data/participation/users.json', 'w') as f:
            json.dump(users, f, indent=4)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: on_message(self, message)
    #    Description: Sees a user message and updates data/participation/users.json
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - message: used to access the values passed through the current context
    # -----------------------------------------------------------------------------------------------------------------
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            with open('data/participation/users.json', 'r') as f:
                users = json.load(f)
            await self.update_data(users, message.author)
            await self.add_experience(users, message.author)
            await self.level_up(users, message.author)

            with open('data/participation/users.json', 'w') as f:
                json.dump(users, f, indent=4)

    async def update_data(self, users, user):
        if not str(user.id) in users:
            users[str(user.id)] = {}
            users[str(user.id)]['experience'] = 0
            users[str(user.id)]['level'] = 1

    async def add_experience(self, users, user):
        users[str(user.id)]['experience'] += 15

    async def level_up(self, users, user):
        experience = users[str(user.id)]['experience']
        lvl = users[str(user.id)]['level']
        lvl_end = 5 * (lvl ** 2) + (50 * lvl) + 100
        # print(user)
        # print(f"Level:{lvl}")
        # print(f"experience:{experience}")
        # print(f"lvl_end: {lvl_end} ")

        if lvl_end <= experience:
            channel = self.client.get_channel(900580609540362303)
            await channel.send('{} has levelled up to level {} ! 🙌'.format(user.mention, lvl + 1))
            users[str(user.id)]['level'] = lvl + 1
            users[str(user.id)]['experience'] -= lvl_end

    async def to_integer(self, dt_time):
        answer = 100000000 * dt_time.year + 1000000 * \
                 dt_time.month + 10000 * dt_time.day + 100 * dt_time.hour + dt_time.minute
        return int(answer)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: level(self, ctx, user)
    #    Description: Outputs a student's level/progress which is stored in data/participation/users.json
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - user: the user that created the command
    #    Outputs: returns a message with a progress bar on the user's progress
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command()
    async def level(self, ctx, user: discord.Member = None):
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

            embed = discord.Embed(Title=f"**{user}'s Rank**",
                                  Description=f"Experience: {lvl}/{5 * (lvl ** 2) + (50 * lvl) + 100}", color=0x0091ff)
            embed.set_thumbnail(url=f"{user.avatar_url}")
            embed.add_field(name=f"**{user}'s Rank**", value="🙌  ", inline=False)
            embed.add_field(name="Level", value=f"**{users[str(user.id)]['level']}**", inline=True)
            embed.add_field(name="Experience", value=f"**{str(int(users[str(user.id)]['experience']))} / {exp}**",
                            inline=True)
            embed.add_field(name="Progress Bar",
                            value=boxes * ":blue_square:" + (20 - boxes) * ":white_large_square:", inline=False)
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
                                  Description=f"Experience: {lvl}/{5 * (lvl ** 2) + (50 * lvl) + 100}", color=0x0091ff)
            embed.set_thumbnail(url=f"{user.avatar_url}")
            embed.add_field(name=f"**{user}'s Rang**", value="🙌  ", inline=False)
            embed.add_field(name="Level", value=f"**{users[str(user.id)]['level']}**", inline=True)
            embed.add_field(name="Experience", value=f"**{str(int(users[str(user.id)]['experience']))} / {exp}**",
                            inline=True)
            embed.add_field(name="Progress Bar",
                            value=boxes * ":blue_square:" + (20 - boxes) * ":white_large_square:", inline=False)
            embed.set_footer(text="Contribute more to level up!")
            await ctx.send(embed=embed)

        with open('data/participation/users.json', 'w') as f:
            json.dump(users, f, indent=4)

    # -----------------------------------------------------------------------------------------------------------------
    #    Function: add_database(self, ctx, user)
    #    Description: Add a user to the database in data/participation/users.json
    #    Inputs:
    #    - self: used to access parameters passed to the class through the constructor
    #    - ctx: used to access the values passed through the current context
    #    - user: the user that needs to be added
    #    Outputs: updates users.json or indicates if user is already in the database
    # -----------------------------------------------------------------------------------------------------------------
    @commands.command()
    async def add_database(self, ctx, user: discord.Member):
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

# -------------------------------------
# add the file to the bot's cog system
# -------------------------------------
def setup(bot):
    bot.add_cog(userRanking(bot))
