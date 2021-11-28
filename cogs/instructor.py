"""This file contains several methods to add/remove instructor"""
import os
import discord
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_role

class Instructor(commands.Cog):
    """Instructor addition/removal functionality"""
    GUILD = os.getenv("GUILD")
    VERIFIED_MEMBER_ROLE = os.getenv("VERIFIED_MEMBER_ROLE")
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='getInstructor', help='Find Instructors')
    async def get_instructor(self, ctx):
        """Function:get_instructor(ctx)
        Description: gets list of instructors
        Inputs:
        - ctx: used to access the values passed through the current context
        -  Outputs: Bots response """
        irole = get(ctx.guild.roles, name='Instructor')
        instructors = ", ".join([str(x).rsplit("#", 1)[0] for x in irole.members])
        if len(irole.members) == 1:
            await ctx.send(instructors + " is the Instructor!")
        else:
            await ctx.send(instructors + " are the Instructors!")


    @commands.command(name='setInstructor', help='Set member to Instructor.')
    async def set_instructor(self, ctx, member:discord.Member):
        """Function:set_instructor(self, ctx, member:discord.Member)
        Description: Sets a member as instructor
        Inputs:
        - self: used to access parameters passed to the class through the constructor
        - ctx: used to access the values passed through the current context
        - member: name of member to be made instructor 
        -  Outputs: Bots response """
        if ctx.channel.name == 'instructor-channel':
            irole = get(ctx.guild.roles, name='Instructor')
            srole = get(ctx.guild.roles, name=self.VERIFIED_MEMBER_ROLE)
            trole = get(ctx.guild.roles, name='TA')
            if irole in member.roles:
                await ctx.channel.send(member.name + " is already an Instructor!")
            else:
                await member.add_roles(irole, reason=None, atomic=True)
                if srole in member.roles:
                    await member.remove_roles(srole)
                if trole in member.roles:
                    await member.remove_roles(trole)
                await ctx.channel.send(member.name + " has been given Instructor role!")
        else:
            await ctx.channel.send('Not a valid command for this channel')


    @commands.command(name='removeInstructor', help='Remove member from Instructor.')
    async def remove_instructor(self, ctx, member:discord.Member):
        """Function:remove_instructor(self, ctx, member:discord.Member)
        Description: removes a member from instructor
        Inputs:
        - self: used to access parameters passed to the class through the constructor
        - ctx: used to access the values passed through the current context
        - member: name of member to be removed from instructor 
        -  Outputs: Bots response """
        if ctx.channel.name == 'instructor-channel':
            irole = get(ctx.guild.roles, name='Instructor')
            srole = get(ctx.guild.roles, name=self.VERIFIED_MEMBER_ROLE)
            if irole not in member.roles:
                await ctx.channel.send(member.name + " is not an Instructor!")
            else:
                await member.remove_roles(irole, reason=None, atomic=True)
                await member.add_roles(srole, reason=None, atomic=True)
                await ctx.channel.send(member.name + " has been removed from Instructor role and given student role!")
        else:
            await ctx.channel.send('Not a valid command for this channel')

def setup(bot):
    """add the file to the bot's cog system"""
    bot.add_cog(Instructor(bot))
