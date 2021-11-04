"""
 Copyright (c) 2021 War-Keeper
"""
import os
import csv
import discord
from discord.ext import commands



class Groups(commands.Cog):

    """
     This File contains commands for joining a group, leaving a group,
     and displaying which groups are available
    """
    student_pool = {}
    groups = {}

    """
     initialize
    """
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='join', help='To use the join command, do: $join \'Group\' <Num> \n \
    ( For example: $join Group 0 )', pass_context=True)
    async def join(self, ctx, arg='group', arg2='-1'):
        """
            Function: join(self, ctx, arg='group', arg2='-1')
            Description: joins the user to the given group
            Inputs:
            - self: used to access parameters passed to the class through the constructor
            - ctx: used to access the values passed through the current context
            - arg: the name of the group
            - arg2: the number of the group
            Outputs: adds the user to the given group or returns an error if the group is invalid or in case of
                     syntax errors
        """
        # load the groups from the csv
        groups = load_groups()
        student_pool = load_pool()

        # get the name of the caller
        member_name = ctx.message.author.display_name.upper()

        # get the arguments for the group to join
        group_num = arg.upper() + ' ' + arg2

        # if the the group is a valid option
        if group_num in groups:

            # check if group has more than 6 people
            if len(groups[group_num]) == 6:
                await ctx.send('A group cannot have more than 6 people!')
                return

            # check if member is already in another group
            for key in groups.keys():
                if member_name in groups[key]:
                    await ctx.send('You are already in ' + key.title())
                    return

            # add the member to the group and send confirmation
            groups[group_num].append(member_name)
            await ctx.send('You are now in ' + group_num.title() + '!')
            print_groups(groups)
            # updates the group number of the member in the name_mapping.csv
            for key in student_pool.keys():
                if key == member_name:
                    student_pool[key][1] = group_num
                    break
            print_pool(student_pool)

        # error handling
        else:
            await ctx.send('Not a valid group')
            await ctx.send('To use the join command, do: $join \'Group\' <Num> \n ( For example: $join Group 0 )')


    @join.error
    async def join_error(self, ctx, error):
        """
            this handles errors related to the join command
        """
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('To use the join command, do: $join \'Group\' <Num> \n ( For example: $join Group 0 )')


    @commands.command(name='remove', help='To use the remove command, do: $remove \'Group\' <Num> \n \
    ( For example: $remove Group 0 )', pass_context=True)
    async def remove(self, ctx, arg='group', arg2='-1'):
        """
               Function: remove(self, ctx, arg='group', arg2='-1')
               Description: removes the user from the given group
               Inputs:
               - self: used to access parameters passed to the class through the constructor
               - ctx: used to access the values passed through the current context
               - arg: the name of the group
               - arg2: the number of the group
               Outputs: removes the user from the given group or returns an error if the group is invalid or in
                        case of syntax errors
           """

        # load groups csv
        groups = load_groups()
        student_pool = load_pool()

        # get the name of the caller
        member_name = ctx.message.author.display_name.upper()

        # get the arguments for the group to join
        group_num = arg.upper() + ' ' + arg2

        # if the the group is a valid option
        if group_num in groups:

            # if member in is the group, then remove them from it
            if member_name in groups[group_num]:
                groups[group_num].remove(member_name)
                await ctx.send('You have been removed from ' + group_num.title() + '!')
                for key in student_pool.keys():
                    if key == member_name:
                        student_pool[key][1] = -1
                        break
                print_pool(student_pool)
            # else error message
            else:
                await ctx.send('You are not in ' + group_num.title())
            print_groups(groups)

        # if the arguments are not listed, then try to find out what group the member is in and remove them
        elif arg2 == '-1':
            for key in groups.keys():
                if member_name in groups[key]:
                    groups[key].remove(member_name)
                    await ctx.send('You are been removed from ' + key.title() + '!')
            print_groups(groups)

        # error handling
        else:
            await ctx.send(group_num.title() + ' is not a valid group')
            await ctx.send('To use the remove command, do: $remove \'Group\' <Num> \n \
            ( For example: $remove Group 0 )')


    @remove.error
    async def remove_error(self, ctx, error):
        """
         this handles errors related to the remove command
        """
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('To use the remove command, do: $remove \'Group\' <Num> \n \
            ( For example: $remove Group 0 )')


    @commands.command(name='group', help='print amount of groups that are full', pass_context=True)
    @commands.dm_only()
    async def group(self, ctx):

        """
            Function: group(self, ctx)
            Description: prints the list of groups
            Inputs:
            - self: used to access parameters passed to the class through the constructor
            - ctx: used to access the values passed through the current context
            Outputs: prints the list of groups
        """

        # load groups csv
        groups = load_groups()

        # create embedded objects
        embed = discord.Embed(title='Group List', color=discord.Color.teal())
        embed.set_thumbnail(url="https://i.pinimg.com/474x/e7/e3/bd/e7e3bd1b5628510a4e9d7a9a098b7be8.jpg")

        embed2 = discord.Embed(title='Group List', color=discord.Color.teal())
        embed2.set_thumbnail(url="https://i.pinimg.com/474x/e7/e3/bd/e7e3bd1b5628510a4e9d7a9a098b7be8.jpg")

        # ignoring the first line, add all group member counts to the embedded objects
        count = 0
        for key in groups.keys():
            if key != 'GROUP_NUM':
                if count < 20:
                    embed.add_field(name=key, value=str(len(groups[key])), inline=True)
                else:
                    embed2.add_field(name=key, value=str(len(groups[key])), inline=True)
                count += 1

        # print the embedded objects
        embed.set_footer(text="Number Represents the Group Size")
        embed2.set_footer(text="Number Represents the Group Size")
        await ctx.send(embed=embed)

        if count >= 20:
            await ctx.send(embed=embed2)


    # @commands.command(name='test_name', help='add a name to the name_mapping.csv', pass_context=True)
    # async def test_name(self, ctx, arg, arg2):
    #         """
    #          This is a testing arg, not really used for anything else but adding to the csv file
    #         """
    #     student_pool = load_pool()
    #     display_name = ctx.message.author.display_name
    #     display_name_upper = display_name.upper()
    #
    #     if student_pool.get(display_name_upper) is None:
    #         student_pool[display_name_upper] = arg.upper() + ' ' + arg2.upper()
    #     else:
    #         member_name = student_pool[display_name_upper]
    #         await ctx.send('You have already registered with the name: ' + member_name.title())
    #
    #     print_pool(student_pool)

    @commands.dm_only()
    @commands.is_owner()
    @commands.command(
        name='auto-assign',
        help="use $auto-assign to automatically assign students who are not part of a group into vacant groups",
        pass_context=True
    )
    async def automatic_grouping(self, ctx):

        """
           Function: automatic_grouping(self, ctx)
           Description: automatically assigns students who are not part of a group into vacant groups
           Inputs:
            - self: used to access parameters passed to the class through the constructor
            - ctx: used to access the values passed through the current context
            Outputs: adds the user to the given group or returns an error if the group is invalid or in case of
                     syntax errors
       """

        # load name_mapping csv
        student_pool = load_pool()

        # load groups csv
        groups = load_groups()

        # returns a dictionary with group numbers as keys and number of vacant spots available as values.
        vacant_groups = get_vacant_groups(groups)
        modifications = {}

        for key in student_pool.keys():
            if student_pool[key][1] == '-1':
                vacant_group = get_minimum(vacant_groups)
                if None in groups[vacant_group]:
                    index = groups[vacant_group].index(None)
                    groups[vacant_group][index] = key
                else :
                    groups[vacant_group].append(key)
                print_groups(groups) # update groups csv file to reflect new members in the group
                student_pool[key][1] = vacant_group
                print_pool(student_pool) # update group number in name_mapping csv
                modifications[key] = vacant_group
                vacant_groups[vacant_group] = vacant_groups[vacant_group]+1


        if bool(modifications):
            await ctx.send("Following updates are made:")
            for key, values in modifications.items():
                await ctx.send(key +  " : " + values)
            await ctx.send("Successfully assigned students into groups")

        else:
            await ctx.send("No modifications made. Every Student is part of a Group")


    @commands.dm_only()
    @commands.command(
        name='find-group',
        help="To use the find-group command, do: $find-group <StudentName> \n \
        ( For example: $find-group Jane Doe )",
        pass_context=True
    )
    async def find_group(self, ctx,*,name : str):

        """
            Function: find_group(self, ctx,name : str)
            Description: given a student name, the function returns the group number the students belongs to
            Inputs:
                - self: used to access parameters passed to the class through the constructor
                - ctx: used to access the values passed through the current context
                - * : to take input of string arguments including spaces
                - name : name of the student
            Outputs: returns the group number of the given student name or asks to re-enter the
                    command  with proper arguments.
        """

        student_pool = load_pool()
        match_found = False
        name = name.upper()
        for key in student_pool.keys():
            if name == key.upper() or name == student_pool[key][0].upper():
                await ctx.send(student_pool[key][1])
                match_found = True
                break

        if not match_found:
            await  ctx.send("Please check the name entered and try again")
            await ctx.send('To use the find-group command, do: $find-group <StudentName> \n \
                            ( For example: $find-group Jane Doe )')

    @find_group.error
    async def find_group_error(self, ctx, error):
        """
         this handles errors related to the find-group command
        """
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('To use the find-group command, do: $find-group <StudentName> \n \
            ( For example: $find-group Jane Doe )')


def load_groups() -> dict:
    """
     Used to load the groups from the csv file into a dictionary
    """
    directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(directory)
    os.chdir('data')
    os.chdir('server_data')
    with open('groups.csv', mode='r') as infile:
        reader = csv.reader(infile)
        group = {rows[0].upper(): [rows[1].upper(), rows[2].upper(), rows[3].upper(), rows[4].upper(),
                                   rows[5].upper(), rows[6].upper()] for rows in reader}

    for key in group.keys():
        group[key] = list(filter(None, group[key]))

    return group


def print_groups(group):
    """
     Used to print the groups to the csv file
    """
    directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(directory)
    os.chdir('data')
    os.chdir('server_data')
    with open('groups.csv', mode='w', newline="") as outfile:
        writer = csv.writer(outfile)
        for key in group.keys():
            while len(group[key]) < 6:
                group[key].append(None)
            writer.writerow([key] + group[key])


def load_pool() -> dict:
    """
     Used to load the members from the csv file into a dictionary
    """
    directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(directory)
    os.chdir('data')
    os.chdir('server_data')
    with open('name_mapping.csv', mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            if rows == []:
                break
            student_pools = {rows[0].upper(): [rows[1].upper(), rows[2]]}

    return student_pools


def print_pool(pools):
    """
     Used to print the members to the csv file
    """
    directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir( directory)
    os.chdir('data')
    os.chdir('server_data')
    with open('name_mapping.csv', mode='w', newline="") as outfile:
        writer = csv.writer(outfile)
        for key in pools.keys():
            while len(pools[key]) < 2:
                pools[key].append(None)
            writer.writerow([key]+ pools[key])


def get_vacant_groups(groups)-> dict:
    """
     retrieves group numbers with vacant spots
    """

    vacant_groups = {}
    for group_number in groups.keys():
        if len(groups[group_number]) < 6:
            vacant_groups[group_number] = len(groups[group_number])

    return vacant_groups


def get_minimum(vacant_groups):
    """
     retrieves group number with minimum student count
    """

    vacant_groups = dict(sorted(vacant_groups.items(), key=lambda x: x[1]))
    minimum = list(vacant_groups.keys())[0]

    return minimum


def setup(bot):
    """
     add the file to the bot's cog system
    """
    bot.add_cog(Groups(bot))
