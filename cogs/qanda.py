from discord import NotFound
from discord.ext import commands
import json


class Object:
    def __init__(self, question, number, author, message, ans):
        self.question = question
        self.number = number
        self.author = author
        self.msg = message
        self.answer = ans


class QuestionsAnswers(commands.Cog):
    ''' Class containing needed question/answer information and identification '''
    def __init__(self, bot):
        self.bot = bot
        with open('data/qanda/qandastorage.json', 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    @commands.command()
    async def ask(self, ctx, question):
        if ctx.channel.name == 'q-and-a':
            ''' add a question '''
            global QUESTION_NUMBER

            with open('data/qanda/qandastorage.json', 'r', encoding='utf-8') as file:
                self.data = json.load(file)

            if self.data:
                QUESTION_NUMBER = len(self.data) + 1
            else:
                QUESTION_NUMBER = 1

            # format question
            q_str = 'Q' + str(QUESTION_NUMBER) + ': ' + question + f"\t*-{ctx.author}*" + '\n'

            message = await ctx.send(q_str)

            self.data[str(QUESTION_NUMBER)] = {
                "question": question,
                "author": str(ctx.author),
                "id": str(message.id),
                "answer": ""
            }
            with open('data/qanda/qandastorage.json', 'w', encoding='utf-8') as file:
                json.dump(self.data, file)

            # delete original question
            await ctx.message.delete()
        else:
            await ctx.message.delete()
            await ctx.author.send('Questions can only be posted on q-and-a channel')

    @commands.command()
    async def askanonym(self, ctx, question):
        if ctx.channel.name == 'q-and-a':
            ''' add a question '''
            global QUESTION_NUMBER

            with open('data/qanda/qandastorage.json', 'r', encoding='utf-8') as file:
                self.data = json.load(file)
            if self.data:
                QUESTION_NUMBER = len(self.data) + 1
            else:
                QUESTION_NUMBER = 1

            # format question
            q_str = 'Q' + str(QUESTION_NUMBER) + ': ' + question + f"\t*-Anonymous*" + '\n'

            message = await ctx.send(q_str)

            self.data[str(QUESTION_NUMBER)] = {
                "question": question,
                "author": "Anonymous",
                "id": str(message.id),
                "answer": ""
            }
            with open('data/qanda/qandastorage.json', 'w', encoding='utf-8') as file:
                json.dump(self.data, file)

            # delete original question
            await ctx.message.delete()
        else:
            await ctx.message.delete()
            await ctx.author.send('Questions can only be posted on q-and-a channel')
            
    @commands.command()
    async def answer(self, ctx, q_num, ans):
        if ctx.channel.name == 'q-and-a':
            with open('data/qanda/qandastorage.json', 'r', encoding='utf-8') as file:
                self.data = json.load(file)

            if not self.data or q_num not in self.data.keys():
                await ctx.author.send('Invalid question number: ' + str(q_num))
                # delete user msg
                await ctx.message.delete()
                return

            try:
                message = await ctx.fetch_message(int(self.data[q_num]["id"]))
            except NotFound:
                await ctx.author.send('Invalid question number: ' + str(q_num))
                # delete user msg
                await ctx.message.delete()
                return

            # generate and edit msg with answer
            if "instructor" in [role.name.lower() for role in ctx.author.roles]:
                role = 'Instructor'
            else:
                role = 'Student'
            new_answer = role + ' Ans: ' + ans

            if not self.data[q_num]["answer"] == '':
                self.data[q_num]["answer"] += '\n'
            self.data[q_num]["answer"] += new_answer

            q_str = 'Q' + str(q_num) + ': ' + self.data[q_num]["question"] + f"\t*-{self.data[q_num]['author']}*"
            content = q_str + '\n' + self.data[q_num]["answer"]

            try:
                await message.edit(content=content)
                with open('data/qanda/qandastorage.json', 'w', encoding='utf-8') as file:
                    json.dump(self.data, file)
            except NotFound:
                await ctx.author.send('Invalid question number: ' + str(q_num))

            # delete user msg
            await ctx.message.delete()
        else:
            await ctx.message.delete()
            await ctx.author.send('Questions can only be posted on q-and-a channel')


def setup(bot):
    bot.add_cog(QuestionsAnswers(bot))
