from discord.ext import commands
import asyncio
import discord
import random

class REMINDER():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="remind",aliases=["remind me","remindme","reminder","reminds"])
    async def remind(self, ctx):
        try:
            prefix=["-","Asuna","asuna","asuna ","Asuna ","-remind","-reminds","-remindme","-remind me","-reminder"]
            week=["weeks","week","wk","w"]
            days=["days","day","d"]
            hours=["hors","hour","hrs","hr","h"]
            minutes=["minutes","minute","min","m"]
            seconds=["seconds","second","sec","s"]
            total=0
            list1=ctx.message.content.split(" ")  
            for i in list1:
                for j in week:
                    if i in j:
                        p=int(i.replace(j,""))
                        total+=p*604800
                for j in days:
                    if i in j:
                        p=int(i.replace(i,""))
                        total+=p*86400
                for j in hours:
                    if i in j:
                        p=int(i.replace(i,""))
                        total+=p*3600
                for j in minutes:
                    if i in j:
                        p=int(i.replace(i,""))
                        total+=p*60
                for j in seconds:
                    if i in j:
                        p=int(i.replace(i,""))
                        total+=p*1
            index = string.index("in")
            list2=list1[0:index]
            stri=""
            for i in list2:
                if i not in prefix:
                    stri+=str(i)
            await asyncio.sleep(float(total))
            embed = discord.Embed(title='Reminder',description=stri, color=random.randint(0, 16777215))
            await ctx.author.send(embed=embed)
        except Exception as e:
            await ctx.send("Maybe you provided invalid inputs.Try again.")
            print(e)

def setup(bot):
    bot.add_cog(REMINDER(bot))
    print('Reminder is loaded')