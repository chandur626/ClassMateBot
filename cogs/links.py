"""This file contains several modules to store or display messages which contain urls"""
import re
import discord
from discord.ext import commands



class Links(commands.Cog):
    """ This File contains commands for Saving the links in a file,
        Display all the messages which contains links."""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """TO store messgaes contanning url to links.txt"""
        url=[]
        message_links = []
        temp=[]
        print(message.content)
        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+" \
                r"\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        url = re.findall(regex, message.content)
        for url_count in url:
            temp.append(url_count[0])
        if temp:
            message_links.append(message.content)
            with open(r'.\data\links\links.txt', "a") as text_file:
                text_file.write("Message containing url :-  " + message.content + "\n")
                text_file.close()
        else:
            pass


    @commands.command(name='send_links', help='Command will output all the messages which contain url')
    async def send_links(self, ctx):
        """To display all messages which contain url."""
        await ctx.send("The below list of messages contains URLs")
        await ctx.send(file=discord.File(r'.\data\links\links.txt'))


def setup(bot):
    """add the file to the bot's cog system"""
    bot.add_cog(Links(bot))
