from discord.ext import commands
import asyncio
import discord
import requests
import string
import codecs
import json
import random
import chucknorris.quips as q
import xkcd as com

with codecs.open("quotes.json", "r",encoding='utf-8', errors='ignore') as f:
    quotes= json.load(f)

class FUN:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dog(self):
        response=requests.get("https://random.dog/woof.json")
        response= json.loads(response.content.decode('utf-8'))
        await self.bot.say(response["url"])

    @commands.command(pass_context=True,name="ask",aliases=["8ball"])
    async def ask(self,ctx,*,p=None):
        if p!=None:
            p=p.lower()
            q=p.replace("?","")
            when= ['Soon™', 'Maybe tomorrow.', 'Maybe next year...', 'Right now.', 'In a few months.']
            what= ['A plane.', 'What? Ask again.', 'A gift.', 'Nothing.', 'A ring.', 'I do not know', "Maybe something."]
            howmuch= ['A lot.', 'A bit.', 'A few.', 'Ask me tomorrow.', 'I do not know, ask a physicist.', 'Nothing.', "2 or 3 liters, I don't remember.", 'Infinity.', '1010 liters.']
            howmany= ['A lot.', 'A bit.', 'A few.', 'Ask me tomorrow.', "I don't know, ask a physicist.", 'Nothing.', '2 or 3, I do not remember.', 'Infinity', '1010.']
            why= ['Maybe genetics.', 'Because somebody decided it.', 'For the glory of satan, of course!', 'I do not know, maybe destiny.', 'Because I said so.', 'I have no idea.', 'Harambe did nothing wrong.', 'Ask the owner of this server.', 'Ask again.', 'To get to the other side.', 'It says so in the Bible.']
            who= ['A human.', 'A robot.', 'An airplane.', 'A bird.', 'A carbon composition.', 'A bunch of zeroes and ones.', 'I have no clue, is it material?', 'That is not logical.']
            other= ['Most likely.', 'Nope.', 'YES!', 'Maybe.']
            result1 = q.find('when')
            result2 = q.find('what')
            result3 = q.find('how much')
            result4 = q.find('how many')
            result5 = q.find('why')
            result6 = q.find('who')
            if result1!=-1:
                check=len(when)
                var=random.randint(0,check)
                await self.bot.say(when[var])
            else:
                if result2!=-1:
                    check=len(what)
                    var=random.randint(0,check)
                    await self.bot.say(what[var])
                else:
                    if result3!=-1:
                        check=len(howmuch)
                        var=random.randint(0,check)
                        await self.bot.say(howmuch[var])
                    else:
                        if result4!=-1:
                            check=len(howmany)
                            var=random.randint(0,check)
                            await self.bot.say(howmany[var])
                        else:
                            if result5!=-1:
                                check=len(why)
                                var=random.randint(0,check)
                                await self.bot.say(why[var])
                            else:
                                if result6!=-1:
                                    check=len(who)
                                    var=random.randint(0,check)
                                    await self.bot.say(who[var])
                                else:
                                    check=len(other)
                                    var=random.randint(0,check)
                                    await self.bot.say(other[var])

    @commands.command(pass_context=True)
    async def quote(self,ctx):
        try:
            await self.bot.say("```"+random.choice(quotes)+"```")
            print("quote")
        except Exception as e:
            await self.bot.say(e)
    
    @commands.command(pass_context=True,name="emo",aliases=["emojify"])
    async def emo(self,ctx,*,word):   
        if word!=None:
            try:
                str=""
                for char in word:
                    if char.isalpha():
                        str+=":regional_indicator_"+char+":"
                    else:
                        str+=(char+"  ")
                await self.bot.say(str.lower())
            except Exception as e:
                await self.bot.say(e)
        print("emo")

    @commands.command(pass_context=True,name="norris",aliases=["chuck","chuck norris"])
    async def norris(self,ctx,*, user: discord.Member=None):   
        try:
            if user is None:
                user ="Chuck Norris"
            else:
                user=user.name
            word=q.random(str(user))
            embed=discord.Embed(name="Chuck Norris",color=0xf7d28c)
            embed.add_field(name="Chuck Norris",value=word)
            embed.set_thumbnail(url="https://cdn.dribbble.com/users/24711/screenshots/1701350/chuck_norris_2x.png")
            await self.bot.say(embed=embed)
            print("norris")
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True)
    async def xkcd(self,ctx,number=None):
        try:
            if number==None:
                a=com.getRandomComic()
                title=a.getTitle()
                link=a.getImageLink()
                exp=a.getExplanation()
                embed=discord.Embed(title="Xkcd",color=0xf7d28c)
                embed.add_field(name="Title",value=title,inline=False)
                embed.set_footer(text=("For explanation refer to: "+exp))
                embed.set_image(url=link)
                await self.bot.say(embed=embed)
            else:
                number=int(number)
                limit=com.getLatestComicNum()
                if number<1 or number>limit:
                    await self.bot.say("Invalid comic number :sweat_smile:")
                else:
                    a=com.getComic(number, silent=True)
                    title=a.getTitle()
                    link=a.getImageLink()
                    exp=a.getExplanation()
                    embed=discord.Embed(title="Xkcd",color=0xf7d28c)
                    embed.add_field(name="Title",value=title,inline=False)
                    embed.set_footer(text=("For explanation refer to: "+exp))
                    embed.set_image(url=link)
                    await self.bot.say(embed=embed)
            print("xkcd")
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True,name="sebi",aliases=["sebisauce","Sebi"])
    async def sebi(self,ctx): 
        try:
            response=requests.get("https://sebisauce.herokuapp.com/api/random")
            response= json.loads(response.content.decode('utf-8'))
            url=response["file"]
            embed=discord.Embed(title="SebiSauce",color=0xf7d28c)
            embed.set_image(url=url)
            await self.bot.say(embed=embed)
            print("sebi")
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True,name="fact",aliases=["facts","fun facts","fun fact","trivia","random","bored"])
    async def fact(self,ctx):
        r=requests.get("http://numbersapi.com/random/trivia")
        p=r.content
        q=p.replace("b'","")
        t=q.replace("'","")
        await self.bot.say("```"+t+"```")

def setup(bot):
    bot.add_cog(FUN(bot))
    print("Fun is loaded")