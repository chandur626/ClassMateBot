import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class Dm(commands.Cog):
    """DM functionality"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='DM', help='DM function')
    async def dm(self, ctx,user:discord.User,*,message=None):
        """Function: dm(self, ctx,user:discord.User,*,message=None)
        Description: Sends a DM to a specific person in the guild
        Inputs:
        - self: used to access parameters passed to the class through the constructor
        - ctx: used to access the values passed through the current context
        - recipient name 
        - content
        -  Outputs: Bots response """


        try:
            await user.send(str(user.mention)+' has sent the following : '+message)
            print(f"Successfully DMed users!")
        except:
            print(f"Unsuccessfully DMed users, try again later.")
        await ctx.send("Hello World!")

    @commands.command(name='reminder', help='reminder function')
    @has_permissions(administrator=True)
    async def reminder(self, ctx,*,message=None):
        """Function: reminder(self, ctx,*,message=None)
        Description: Send a reminder to all users in the guild
        Inputs:
        - self: used to access parameters passed to the class through the constructor
        - ctx: used to access the values passed through the current context
        - content
        -  Outputs: Bots response """
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"Successfully sent the reminder to users!")
            except:
                print(f"Unsuccessfully DMed users, try again later.")

def setup(bot):
    """add the file to the bot's cog system"""
    bot.add_cog(Dm(bot))