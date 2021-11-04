# Copyright (c) 2021 War-Keeper
"""
This functionality provides various methods to manage reminders (in the form of creation, retrieval,
updation and deletion). An user can set up a reminder, check what is due this week or what is due
today. He/She can also check all the due homeworks based on hte course name. An user can also update
or delete a reminder if needed.
"""
import discord
from discord.ext import commands, tasks
from Utility.email_utility import EmailUtility
import json
import os
import sys
import asyncio
import time
from datetime import datetime


class Deadline(commands.Cog):
    """Class provides several methods to manage remainders."""

    def __init__(self, bot):
        self.bot = bot
        cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.chdir(cur_dir)
        self.reminders = json.load(open("data/remindme/reminders.json"))
        self.units = {"second": 1, "minute": 60, "hour": 3600, "day": 86400, "week": 604800,
                      "month": 2592000}

    @commands.command(name="addhw",
                      help="add homework and due-date "
                           "$addhw CLASSNAME HW_NAME MMM DD YYYY optional(HH:MM)"
                           " ex. $addhw CSC510 HW2 SEP 25 2024 17:02")
    async def duedate(self, ctx, coursename: str, hwcount: str, *, date: str):
        """
            Adds the homework to json in the specified format.

            Parameters:
                ctx: used to access the values passed through the current context.
                coursename: name of the course for which homework is to be added.
                hwcount: name of the homework
                date: due date of the assignment

            Returns:
                returns either an error stating a reason for failure or returns a success message
                indicating that the reminder has been added

        """
        author = ctx.message.author
        try:
            duedate = datetime.strptime(date, '%b %d %Y %H:%M')
            # print(seconds)
        except ValueError:
            try:
                duedate = datetime.strptime(date, '%b %d %Y')
            except:
                await ctx.send("Due date could not be parsed")
                return
        a_timedelta = duedate - datetime.today()
        seconds = (time.time() + a_timedelta.total_seconds())
        flag = True
        if self.reminders:
            for reminder in self.reminders:
                if ((reminder["COURSE"] == coursename) and (reminder["HOMEWORK"] == hwcount)):
                    flag = False
                    break
        if flag:
            self.reminders.append({"ID": author.id, "COURSE": coursename, "HOMEWORK": hwcount,
                                   "DUEDATE": str(duedate),
                                   "FUTURE": seconds})
            cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            os.chdir(cur_dir)
            json.dump(self.reminders, open("data/remindme/reminders.json", "w"))
            await ctx.send(
                "A date has been added for: {} homework named: {} which is due on: {} by {}.".format(
                    coursename,
                    hwcount,
                    str(duedate),
                    author))
        else:
            await ctx.send("This homework has already been added..!!")

    @duedate.error
    async def duedate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the addhw command, do: $addhw CLASSNAME HW_NAME MMM DD YYYY optional(HH:MM)'
                ' \n ( For example: $addhw CSC510 HW2 SEP 25 2024 17:02 )')

    @commands.command(name="deletereminder", pass_context=True,
                      help="delete a specific reminder using course name and homework name using"
                           " $deletereminder CLASSNAME HW_NAME ex. $deletereminder CSC510 HW2 ")
    async def deleteReminder(self, ctx, courseName: str, hwName: str):
        """
            Delete a reminder using Classname and Homework name.

            Parameters:
                ctx: used to access the values passed through the current context.
                coursename: name of the course for which homework is to be added.
                hwName: name of the homework.

            Returns:
                returns either an error stating a reason for failure or returns a success message
                indicating that the reminder has been deleted.

        """
        author = ctx.message.author
        to_remove = []
        for reminder in self.reminders:
            # print('in json '+str(reminder["HOMEWORK"])+' hwName '+hwName)
            if ((reminder["HOMEWORK"] == hwName) and (reminder["COURSE"] == courseName)):
                # print('true '+hwName)
                to_remove.append(reminder)
                # print('to_remove '+ str(to_remove))
        for reminder in to_remove:
            self.reminders.remove(reminder)
        if to_remove:
            cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            os.chdir(cur_dir)
            json.dump(self.reminders, open("data/remindme/reminders.json", "w"))
            await ctx.send(
                "Following reminder has been deleted: Course: {},"
                " Homework Name: {}, Due Date: {}".format(
                    str(reminder["COURSE"]), str(reminder["HOMEWORK"]), str(reminder["DUEDATE"])))

    @deleteReminder.error
    async def deleteReminder_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the deletereminder command, do: $deletereminder CLASSNAME HW_NAME'
                ' \n ( For example: $deletereminder CSC510 HW2 )')

    @commands.command(name="changeduedate", pass_context=True,
                      help="update the assignment date. "
                           "$changeduedate CLASSNAME HW_NAME MMM DD YYYY optional(HH:MM) "
                           "ex. $changeduedate CSC510 HW2 SEP 25 2024 17:02 ")
    async def changeduedate(self, ctx, classid: str, hwid: str, *, date: str):
        """
            Update the 'Due date' for a homework by providing the classname and homework name.

            Parameters:
                ctx: used to access the values passed through the current context.
                classid: name of the course for which homework is to be added.
                hwid: name of the homework.
                date: due date of the assignment.

            Returns:
                returns either an error stating a reason for failure or returns a success message
                indicating that the reminder has been updated.

        """
        author = ctx.message.author
        flag = False
        try:
            duedate = datetime.strptime(date, '%b %d %Y %H:%M')
        except ValueError:
            try:
                duedate = datetime.strptime(date, '%b %d %Y')
            except:
                await ctx.send("Due date could not be parsed")
                return
        for reminder in self.reminders:
            flag = False
            if ((reminder["HOMEWORK"] == hwid) and (reminder["COURSE"] == classid)):
                reminder["DUEDATE"] = str(duedate)
                a_timedelta = duedate - datetime.today()
                seconds = (time.time() + a_timedelta.total_seconds())
                reminder["FUTURE"] = seconds
                reminder["ID"] = author.id
                flag = True
                if flag:
                    cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                    os.chdir(cur_dir)
                    json.dump(self.reminders, open("data/remindme/reminders.json", "w"))
                    await ctx.send(
                        "{} {} has been updated with"
                        " following date: {}".format(classid, hwid, reminder["DUEDATE"]))

    @changeduedate.error
    async def changeduedate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the changeduedate command, '
                'do: $changeduedate CLASSNAME HW_NAME MMM DD YYYY optional(HH:MM) '
                '\n ( For example: $changeduedate CSC510 HW2 SEP 25 2024 17:02 )')

    @commands.command(name="duethisweek", pass_context=True,
                      help="check all the homeworks that are due this week $duethisweek")
    async def duethisweek(self, ctx):
        """
            Displays all homeworks that are due this week along with the coursename and due date.

            Parameters:
                ctx: used to access the values passed through the current context.

            Returns:
                returns either an error stating a reason for failure or returns a list of all the
                assignments that are due this week.

        """
        time = ctx.message.created_at
        for reminder in self.reminders:
            timeleft = datetime.strptime(reminder["DUEDATE"], '%Y-%m-%d %H:%M:%S') - time
            print("timeleft: " + str(timeleft) + " days left: " + str(timeleft.days))
            if timeleft.days <= 7:
                await ctx.send(
                    "{} {} is due this week at {}".format(reminder["COURSE"], reminder["HOMEWORK"],
                                                          reminder["DUEDATE"]))

    @commands.command(name="duetoday", pass_context=True,
                      help="check all the homeworks that are due today $duetoday")
    async def duetoday(self, ctx):
        """
            Displays all the homeworks that are due today.

            Parameters:
                ctx: used to access the values passed through the current context.

            Returns:
                returns either an error stating a reason for failure or returns a list of all the
                assignments that are due on the execution date of this command.

        """
        flag = True
        for reminder in self.reminders:
            timedate = datetime.strptime(reminder["DUEDATE"], '%Y-%m-%d %H:%M:%S')
            if timedate.date() == ctx.message.created_at.date():
                flag = False
                await ctx.send(
                    "{} {} is due today at {}".format(reminder["COURSE"], reminder["HOMEWORK"],
                                                      timedate.time()))
        if flag:
            await ctx.send("You have no dues today..!!")

    @commands.command(name="coursedue", pass_context=True,
                      help="check all the homeworks that are due for a specific course "
                           "$coursedue coursename ex. $coursedue CSC505")
    async def coursedue(self, ctx, courseid: str):
        """
            Displays all the homeworks that are due for a specific course.

            Parameters:
                ctx: used to access the values passed through the current context.

            Returns:
                returns either an error stating a reason for failure or returns a list of all the
                assignments that are due for the provided course.

        """
        course_due = []
        for reminder in self.reminders:
            if reminder["COURSE"] == courseid:
                course_due.append(reminder)
                await  ctx.send("{} is due at {}".format(reminder["HOMEWORK"], reminder["DUEDATE"]))
        if not course_due:
            await ctx.send("Rejoice..!! You have no pending homeworks for {}..!!".format(courseid))

    @coursedue.error
    async def coursedue_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'To use the coursedue command, do: $coursedue CLASSNAME'
                ' \n ( For example: $coursedue CSC510 )')

    @commands.command(name="listreminders", pass_context=True, help="lists all reminders")
    async def listreminders(self, ctx):
        """
            Print out all the reminders.

            Parameters:
                ctx: used to access the values passed through the current context.

            Returns:
                returns either an error stating a reason for failure or returns a list of all the
                assignments.

        """
        to_remove = []
        for reminder in self.reminders:
            try:
                await ctx.send(
                    "{} homework named: {} which is due on: {} by {}".format(reminder["COURSE"],
                                                                             reminder["HOMEWORK"],
                                                                             reminder["DUEDATE"],
                                                                             self.bot.get_user(
                                                                                 reminder["ID"])))
            except (discord.errors.Forbidden, discord.errors.NotFound):
                to_remove.append(reminder)
            except discord.errors.HTTPException:
                pass
            else:
                to_remove.append(reminder)
        if not self.reminders:
            await ctx.send("Mission Accomplished..!! You don't have any more dues..!!")

    @commands.command(name="clearreminders", pass_context=True, help="deletes all reminders")
    async def clearallreminders(self, ctx):
        """
            Delete all the reminders.

            Parameters:
                ctx: used to access the values passed through the current context.

            Returns:
                returns either an error stating a reason for failure or returns a
                success message stating that reminders have been deleted.

        """
        to_remove = []
        for reminder in self.reminders:
            to_remove.append(reminder)
        for reminder in to_remove:
            self.reminders.remove(reminder)
        if to_remove:
            cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            os.chdir(cur_dir)
            json.dump(self.reminders, open("data/remindme/reminders.json", "w"))
            await ctx.send("All reminders have been cleared..!!")

    @commands.command(name="remindme", pass_context=True,
                      help="Request the bot to set a reminder for a due date")
    async def remindme(self, ctx, quantity: int, time_unit: str, *, text: str):
        """
            Personal remind me functionality.

            Parameters:
                ctx: used to access the values passed through the current context.
                quantity: time after which the data will be erased

            Returns:
                returns either an error stating a reason for failure or
                returns a success message stating that reminders have been deleted.

        """
        time_unit = time_unit.lower()
        author = ctx.message.author
        s = ""
        if time_unit.endswith("s"):
            time_unit = time_unit[:-1]
            s = "s"
        if not time_unit in self.units:
            await ctx.send(
                "Invalid unit of time. Select from seconds/minutes/hours/days/weeks/months")
            return
        if quantity < 1:
            await ctx.send("Quantity must not be 0 or negative")
            return
        if len(text) > 1960:
            await ctx.send("Text is too long.")
            return

        seconds = self.units[time_unit] * quantity
        future = int(time.time() + seconds)

        self.reminders.append({"ID": author.id, "FUTURE": future, "TEXT": text})
        await ctx.send("I will remind you that in {} {}.".format(str(quantity), time_unit + s))
        json.dump(self.reminders, open("data/remindme/reminders.json", "w"))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(
            '\nUnidentified command... Refer to $help to get the list of available commands')

    async def delete_old_reminders(self):
        """
            asynchronously keeps on tracking the json file for expired reminders and cleans them.

            Parameters:

            Returns:
                return nothing as this is task to delete the old reminders.

        """
        while self is self.bot.get_cog("Deadline"):
            to_remove = []
            for reminder in self.reminders:
                if reminder["FUTURE"] <= int(time.time()):
                    try:
                        print("Deleting an old reminder..!!")
                    except (discord.errors.Forbidden, discord.errors.NotFound):
                        to_remove.append(reminder)
                    except discord.errors.HTTPException:
                        pass
                    else:
                        to_remove.append(reminder)
            for reminder in to_remove:
                self.reminders.remove(reminder)
            if to_remove:
                cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                os.chdir(cur_dir)
                json.dump(self.reminders, open("data/remindme/reminders.json", "w"))
            await asyncio.sleep(5)


@tasks.loop(seconds=10)
async def email_remainders():
    """
        asynchronously keeps on tracking the reminders and email about the same to users.

        Parameters:

        Returns:
            return nothing as this is task to email the reminders.

    """
    cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(cur_dir)
    with open('data/remindme/reminders.json', 'r') as rfile, open('data/email/emails.json',
                                                                  'r') as efile:
        reminders = json.load(rfile)
        email_list = json.load(efile)
        for reminder in reminders:
            due_date = datetime.strptime(reminder["DUEDATE"], '%Y-%m-%d %H:%M:%S')
            remaining_time = due_date - datetime.today()
            if 'eactive' in reminder.keys() and reminder['eactive'] == 0:
                continue
            if remaining_time.total_seconds() <= 86400:
                if str(reminder['ID']) in email_list:
                    EmailUtility().send_email(email_list[str(reminder['ID'])],
                                              subject='CLASSMATE BOT REMINDER',
                                              body="This email is to let you know that "
                                                   "{} is due at {}".format(
                                                  reminder["HOMEWORK"], reminder["DUEDATE"]))
                    reminder['eactive'] = 0
                    json.dump(reminders, open("data/remindme/reminders.json", "w"))
                else:
                    continue


def check_folders():
    """checks if the folder that is going to hold json exists else creates a new one."""
    cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(cur_dir)
    if not os.path.exists("data/remindme"):
        print("Creating data/remindme folder...")
        os.makedirs("data/remindme")


def check_files():
    """checks if a json file exists else creates a new one"""
    cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(cur_dir)
    f = "data/remindme/reminders.json"
    print("Creating file...")
    if not os.path.exists(f):
        print("Creating empty reminders.json...")
        json.dump([], open(f, "w"))


def setup(bot):
    """add the file to the bot's cog system"""
    check_folders()
    check_files()
    n = Deadline(bot)
    loop = asyncio.get_event_loop()
    loop.create_task(n.delete_old_reminders())
    bot.add_cog(n)
