# bot.py
# Copyright (c) 2021 War-Keeper
import json
import os
import discord
from discord.utils import get
from discord import Intents
from dotenv import load_dotenv
from discord.ext.commands import Bot, has_permissions
from Utility.email_utility import EmailUtility
import asyncio
# ----------------------------------------------------------------------------------------------
# Initializes the discord bot with a unique TOKEN and joins the bot to a server provided by the
# GUILD token. Handles bot shutdown and error events
# ----------------------------------------------------------------------------------------------

# Load the environment
load_dotenv()
# Get the token for our bot
TOKEN = os.getenv("TOKEN")
# Get the token for our discord server
GUILD = os.getenv("GUILD")
UNVERIFIED_ROLE_NAME = os.getenv("UNVERIFIED_ROLE_NAME")
# Set the bots intents to all
intents = Intents.all()
# Set all bot commands to begin with $
bot = Bot(intents=intents, command_prefix="$")
spam_log=[]

# ------------------------------------------------------------------------------------------------------------------
#    Function: on_ready()
#    Description: Activates when the bot starts, prints the name of the server it joins and the names of all members
#                 of that server
#    Inputs:
#    -
#    Outputs:
#    -
# ------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    if guild:
        print(
            f"{bot.user} is connected to the following guild:\n"
            f"{guild.name}(id: {guild.id})"
            )

        members = "\n -".join([member.name for member in guild.members])
        print(f"Guild Members:\n - {members}")
    else:
        print(f"{bot.user} not part of any guild yet.")

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
    bot.load_extension("jishaku")

    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="Over This Server"
        )
    )
    print("READY!")
    while True:
        print('spam cleared')
        await asyncio.sleep(10)
        spam_log.clear()

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    counter=1    
    for i in range(len(spam_log)): 
        if spam_log[i]==str(message.author.id):
            counter=counter+1
    spam_log.append(str(message.author.id))
    if counter>4:
        await message.channel.send('please stop spamming! '+message.author.mention+', this may lead to a BAN/KICK!')
        def check(m):
            return str(m.author) == str(message.author)
        await message.channel.purge(limit=6, check=check)
# ------------------------------------------------------------------------------------------------------------------
#    Function: on_guild_join
#    Description: run when a the bot joins a guild
#    Inputs:
#    - guild: the guild the user joined from
#    Outputs:
#    -
# ------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_guild_join(guild):
    channel = get(guild.text_channels, name='general')
    if channel is None:
        await guild.create_text_channel('general')
        channel = get(guild.text_channels, name='general')
    if channel.permissions_for(guild.me).send_messages:
        await channel.send('Hi there, I\'m ClassMate Bot, and I\'m here' +
            'to help you manage your class discord! Let\'s do some quick setup.')
    role = get(guild.roles, name='Instructor')
    await guild.create_role(name="Instructor", colour=discord.Colour(0xdc143c),
                                    permissions=discord.Permissions.all())
    leadrole = get(guild.roles, name='Instructor')
    #Assign Instructor role to admin is there is no Instructor
    if role is None or len(role.members) == 0:
        leader = guild.owner
        leadrole = get(guild.roles, name='Instructor')
        await channel.send(leader.name + " has been given Instructor role!")
        await leader.add_roles(leadrole, reason=None, atomic=True)
    else:
        for member in role.members:
            await member.add_roles(leadrole, reason=None, atomic=True)
        instructors = ", ".join([str(x).rsplit("#", 1)[0] for x in leadrole.members])
        if len(leadrole.members) == 1:
            await channel.send(instructors + " is the Instructor!")
        else:
            await channel.send(instructors + " are the Instructors!")
    #await channel.send("To add Instructors, type \"!setInstructor @<member>\"")
    #await channel.send("To remove instructors, type \"!removeInstructor @<member>\"")
    await guild.create_role(name="TA", colour=discord.Colour(0x00ffff),
                                    permissions=discord.Permissions.all())
    await guild.create_role(name="student", colour=discord.Colour(0x7289da),
                                    permissions=discord.Permissions.all())
    await guild.create_role(name="guest", colour=discord.Colour(0xfffacd),
                                    permissions=discord.Permissions.all())
    #Create Text channels if they don't exist
    ic_overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False,
        send_messages=False), leadrole: discord.PermissionOverwrite(read_messages=True,
        send_messages=True)}
    role = get(guild.roles, name='TA')
    tc_overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False,
        send_messages=False), leadrole: discord.PermissionOverwrite(read_messages=True,
        send_messages=True), role: discord.PermissionOverwrite(read_messages=True,
        send_messages=True)}
    if get(guild.text_channels, name='instructor_channel') is None:
        await guild.create_text_channel('instructor_channel', overwrites=ic_overwrites)
        await channel.send("instructor_channel channel has been added!")
    else:
        await channel.send("instructor_channel channel is already present!")
    if get(guild.text_channels, name='TA_channel') is None:
        await guild.create_text_channel('TA_channel', overwrites=tc_overwrites)
        await channel.send("TA_channel channel has been added!")
    else:
        await channel.send("TA_channel channel is already present!")
    if get(guild.text_channels, name='q-and-a') is None:
        await guild.create_text_channel('q-and-a')
        await channel.send("q-and-a channel has been added!")
    else:
        await channel.send("q-and-a channel is already present!")
    if get(guild.text_channels, name='course-calendar') is None:
        await guild.create_text_channel('course-calendar')
        await channel.send("course-calendar channel has been added!")
    else:
        await channel.send("course-calendar channel is already present!")

@bot.event
async def on_raw_reaction_add(payload):
    print(payload)
    email = EmailUtility()
    email_list = json.load(open("data/email/emails.json"))
    guild = bot.get_guild(payload.guild_id)
    channel = guild.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    if payload.emoji.name == '\N{WHITE HEAVY CHECK MARK}':
        if str(payload.user_id) not in email_list:
            await channel.send("Please make sure you have an email address configured..!")
            return
        for attachment in message.attachments:
            filename = attachment.filename
            attachment = await attachment.read()
            email.send_email(email_list[str(payload.user_id)], attachment, filename=filename)


# ------------------------------------------------------------------------------------------------------------------
#    Function: on_member_join(member)
#    Description: Handles on_member_join events, DMs the user and asks for verification through newComer.py
#    Inputs:
#    - member: used to add member to the knowledge of the bot
#    Outputs:
#    -
# ------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_member_join(member):
    unverified = discord.utils.get(
        member.guild.roles, name=UNVERIFIED_ROLE_NAME
    )  # finds the unverified role in the guild
    await member.add_roles(unverified) # assigns the unverified role to the new member
    await member.send("Hello " + member.name + "!")
    await member.send(
        "Verify yourself before getting started! \n To use the verify command, do: $verify <your_full_name> \n \
        ( For example: $verify Jane Doe )")

# ------------------------------------------------------------------------------------------------------------------
#    Function: on_error(event, *args, **kwargs)
#    Description: Handles bot errors, prints errors to a log file
#    Inputs:
#    - member: event of the error
#    - *args: any arguments that come with error
#    - **kwargs: other args
#    Outputs:
#    -
# ------------------------------------------------------------------------------------------------------------------
@bot.event
async def on_error(event, *args, **kwargs):
    with open("err.log", "a") as f:
        if event == "on_message":
            f.write(f"Unhandled message: {args[0]}\n")
        else:
            raise
# ----------------------------------
#    Function: load
#    Description: Command for loading a cog
#    Inputs:
#    - ctx: used to access the values passed through the current context
#    - extension: name of the cog that is to be added
#    Outputs:
#    - response from bot
# ----------------------------------
@bot.command(name='loadCog',help="loads a specific cog")
@has_permissions(administrator=True)
async def load(ctx,extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(str(extension)+' cog has been added')

# ----------------------------------
#    Function: unload
#    Description: Command for unloading a cog
#    Inputs:
#    - ctx: used to access the values passed through the current context
#    - extension: name of the cog that is to be removed
#    Outputs:
#    - response from bot
# ----------------------------------

@bot.command(name='unloadCog',help="unloads a specific cog")
@has_permissions(administrator=True)
async def unload(ctx,extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send(str(extension)+' cog has been removed')


# ----------------------------------
#    Function: reload
#    Description: Command for reloading a cog after an update is made
#    Inputs:
#    - ctx: used to access the values passed through the current context
#    - extension: name of the cog that is to be reloaded
#    Outputs:
#    - response from bot
# ----------------------------------

@bot.command(name='reloadCog',help="reloads a specific cog")
@has_permissions(administrator=True)
async def reload(ctx,extension):
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")

    await ctx.send(str(extension)+' cog has been reloaded')

# ----------------------------------
#    Function: Ban
#    Description: Command for banning spammers
#    Inputs:
#    - ctx: used to access the values passed through the current context
#    - member: name of the memeber
#    - reason: reason for ban
#    Outputs:
#    - response from bot
# ----------------------------------

@bot.command(name='ban',help="bans a member")
@has_permissions(administrator=True)
async def ban(ctx,member:discord.Member,*,reason=None):

    await member.ban(reason=reason)
    await ctx.send(str(member.mention)+' has been banned for '+reason)

# ----------------------------------
#    Function: unBan
#    Description: Command for unbanning 
#    Inputs:
#    - ctx: used to access the values passed through the current context
#    - member: name of the memeber
#    Outputs:
#    - response from bot
# ----------------------------------

@bot.command(name='unban',help="unbans a member")
@has_permissions(administrator=True)
async def unban(ctx,*,member):

    banned_users= await ctx.guild.bans()

    member_name,member_discriminator=member.split('#')

    for entry in banned_users:

        user=entry.user
        if (user.name,user.discriminator)==(member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send('unbanned '+member.mention)
            return

# ------------------------------------------------------------------------------------------------------------------
#    Function: shutdown(ctx)
#    Description: Command for shutting down the bot
#    Inputs:
#    - ctx: used to access the values passed through the current context
#    Outputs:
#    -
# ------------------------------------------------------------------------------------------------------------------
@bot.command(name="shutdown", help="Shuts down the bot, only usable by the owner")
@has_permissions(administrator=True)
async def shutdown(ctx):
    await ctx.send('Shutting Down bot')
    print("Bot closed successfully")
    ctx.bot.logout()
    exit()

# Starts the bot with the current token
bot.run(TOKEN)

