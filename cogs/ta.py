"""This file contains several methods to add/remove TA"""
import os
import discord
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_role

class TA(commands.Cog):
    """Instructor addition/removal functionality"""
    GUILD = os.getenv("GUILD")
    VERIFIED_MEMBER_ROLE = os.getenv("VERIFIED_MEMBER_ROLE")
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='getTA', help='Find TAs')
    async def get_ta(self, ctx):
        """Function:get_ta(ctx)
        Description: gets list of TA's
        Inputs:
        - ctx: used to access the values passed through the current context
        -  Outputs: Bots response """
        trole = get(ctx.guild.roles, name='TA')
        tas = ", ".join([str(x).rsplit("#", 1)[0] for x in trole.members])
        if len(trole.members) == 1:
            await ctx.send(tas + " is the TA!")
        else:
            await ctx.send(tas + " are the TA's!")


    @commands.command(name='setTA', help='Set member to TA.')
    async def set_ta(self, ctx, member:discord.Member):
        """Function:set_ta(self, ctx, member:discord.Member)
        Description: Sets a member as TA
        Inputs:
        - self: used to access parameters passed to the class through the constructor
        - ctx: used to access the values passed through the current context
        - member: name of member to be made TA 
        -  Outputs: Bots response """
        if ctx.channel.name == 'instructor-channel' or ctx.channel.name == 'ta-channel':
            irole = get(ctx.guild.roles, name='Instructor')
            srole = get(ctx.guild.roles, name=self.VERIFIED_MEMBER_ROLE)
            trole = get(ctx.guild.roles, name='TA')
            if irole in member.roles:
                await ctx.channel.send(member.name + " is already has higher role of" +
                " instructor! If you want to make just TA use remove from instructor role and try again.")
            else:
                if trole in member.roles:
                    await ctx.channel.send(member.name + " is already a TA!")
                else:
                    await member.add_roles(trole, reason=None, atomic=True)
                    if srole in member.roles:
                        await member.remove_roles(srole)
                    await ctx.channel.send(member.name + " has been given TA role!")
        else:
            await ctx.channel.send('Not a valid command for this channel')


    @commands.command(name='removeTA', help='Remove member from TA.')
    async def remove_ta(self, ctx, member:discord.Member):
        """Function:remove_ita(self, ctx, member:discord.Member)
        Description: removes a member from TA
        Inputs:
        - self: used to access parameters passed to the class through the constructor
        - ctx: used to access the values passed through the current context
        - member: name of member to be removed from TA 
        -  Outputs: Bots response """
        if ctx.channel.name == 'instructor-channel' or ctx.channel.name == 'ta-channel':
            trole = get(ctx.guild.roles, name='TA')
            srole = get(ctx.guild.roles, name=self.VERIFIED_MEMBER_ROLE)
            if trole not in member.roles:
                await ctx.channel.send(member.name + " is not a TA!")
            else:
                await member.remove_roles(trole, reason=None, atomic=True)
                await member.add_roles(srole, reason=None, atomic=True)
                await ctx.channel.send(member.name + " has been removed from TA role and given student role!")
        else:
            await ctx.channel.send('Not a valid command for this channel')

def setup(bot):
    """add the file to the bot's cog system"""
    bot.add_cog(TA(bot))
