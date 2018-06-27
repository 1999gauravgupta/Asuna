import discord
import codecs
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import random
import json
import urbandictionary as udd
import urllib
import string
import chucknorris.quips as q
import xkcd as com
import requests
import time
import spice_api as spice
import inspect
from py_thesaurus import Thesaurus
import lyricwikia
import pickle



#for loading music.py
startup_extensions = ["Music","gifs","executer"]



#for files
with codecs.open("quotes.json", "r",encoding='utf-8', errors='ignore') as f:
    quotes= json.load(f)

owner=["343395225571426304","402829897514352641"]

bot = commands.Bot(command_prefix=commands.when_mentioned_or('-','asuna ',"Asuna ","Asuna, ","asuna, "))

client=discord.Client()

#for music command class
class Main_Commands():
    def __init__(self, bot):
        self.bot = bot
    #for Music extension
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exe = '{}: {}'.format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(extension, exe))
#COMMANDS
@bot.event
async def on_ready():
    print("ready")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Listening to -help'))
    print("status changing done")

@bot.event
async def on_message(message):
    Words=["dick","pussy","motherfucker","whore", "asshole","son of a bitch","dickhead","bitch","dick head","cunt","faggot","fag","nigga","niger","nigger","slut"]
    with open("serverf.txt", "r") as f1:
        list1=f1.readlines()
        for i in list1:
            j=i.replace("\n","")
            if j==message.server.id:
                if  message.author.bot==False:
                    if message.author.id in owner:
                        pass
                    else:
                        try:
                            for i in Words:
                             if  i in message.content.lower():
                                await bot.send_message(message.channel, "|:x:| Pardon, dear {}, you said something that is not allowed in this server".format(message.author))
                                await bot.delete_message(message)
                        except Exception as e:
                            print(e)
    if message.author.bot==True:
        return
    await bot.process_commands(message)
@bot.command(pass_context=True)
async def filter(ctx,state=1):
    if state==1:
        with open("serverf.txt", "a") as f1:
            f1.write("\n"+ctx.message.server.id)
        await bot.say("Filter turned on successfully.")
    else:
        f = open("serverf.txt","r")
        lines = f.readlines()
        f.close()
        f = open("serverf.txt","w")
        for line in lines:
            p=line.replace("\n","")
            if p!=ctx.message.server.id:
                f.write(line)
        f.close()
        await bot.say("Filter turned off successfully.")


@bot.command(pass_context=True)
async def ping(self):
        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        tim = (after-before)*1000
        await self.bot.say("**Pong 🏓, took {0:.0f}ms**".format(tim))
        print("ping")

@bot.command(pass_context=True)
async def poll(ctx,*,query=None):
    p=query.replace("?","")
    p=p+" ?"
    await bot.say(p.title())
    await bot.add_reaction(ctx.message , ":arrow_up_small:")
    await bot.add_reaction(ctx.message , ":arrow_down_small:")

@bot.command()
async def cat():
    response=urllib.request.urlopen("https://nekos.life/api/v2/img/meow").read()
    response=json.loads(response.decode("utf-8"))
    await bot.say(response["url"])

@bot.command()
async def dog():
    response=urllib.request.urlopen("https://random.dog/woof.json").read()
    response=json.loads(response.decode("utf-8"))
    await bot.say(response["url"])

@bot.command()
async def duck():
    response=urllib.request.urlopen("https://random-d.uk/api/v1/random").read()
    response=json.loads(response.decode("utf-8"))
    await bot.say(response["url"])

@bot.command(pass_context=True,name="info",aliases=["user","userinfo"])
async def info(ctx,*, user: discord.Member=None):
    if ctx.message.author.bot==False:
        if user is None:
            user = ctx.message.author
        try:
            embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0xf7d28c)
            embed.add_field(name="Name", value=user.name)
            embed.add_field(name="ID", value=user.id)
            embed.add_field(name="Status", value=user.status)
            embed.add_field(name="Highest role", value=user.top_role)
            embed.add_field(name="Joined", value=user.joined_at)
            embed.add_field(name="Created",value=user.created_at)
            embed.set_thumbnail(url=user.avatar_url)
            await bot.say(embed=embed)
            print("User Info")
        except Exception as e:
            await bot.say(e)

@bot.command(pass_context=True)
async def svrinfo(ctx,name="svrinfo",aliases=["serverinfo"]):
    if ctx.message.author.bot==False:
        try:
            server = ctx.message.server
            role = [x.name for x in server.role_hierarchy]
            roles=""
            for i in role:
                roles+=(str(i)+", ")
            channelz = str(len(server.channels))
            time = str(server.created_at); time = time.split(' '); time= time[0]
            embed = discord.Embed(title= (ctx.message.server.name+" info"), description="Here's what I could find.", color=0xf7d28c)
            embed.add_field(name="Name", value=ctx.message.server.name)
            embed.add_field(name="ID", value=ctx.message.server.id)
            embed.add_field(name="Owner",value=ctx.message.server.owner.name)
            embed.add_field(name="Channels",value=channelz)
            embed.add_field(name="Emojis",value=len(ctx.message.server.emojis))
            embed.add_field(name="Members", value=len(ctx.message.server.members))
            embed.add_field(name="Roles", value=len(ctx.message.server.roles))
            embed.add_field(name="Server roles",value=roles)
            embed.set_thumbnail(url=ctx.message.server.icon_url)
            await bot.say(embed=embed)
            print("Server Info")
        except Exception as e:
            await bot.say(e)

@bot.command(pass_context=True)
async def say(ctx,*,something=None):
    if ctx.message.author.bot==False:
        if ctx.message.author.id in owner:
            if something is None:
                await bot.say("What would you like me to say? :thinking:")
            else:
                await bot.say(something)
        else:
            await bot.say("I only listen to my owner")
        await bot.delete_message(ctx.message)
        print("Say")

@bot.command(pass_context=True)
async def spam(ctx,no=1,*,something=None):
    if ctx.message.author.bot==False:
        if ctx.message.author.id in owner :
            if something is None:
                await bot.say("What would you like me to say? :thinking:")
            else:
                for i in range(no):
                    await bot.say(something)
        else:
            await bot.say("I only listen to my owner")
        await bot.delete_message(ctx.message)
        print("Spam")

@bot.command(pass_context=True,name="pfp",aliases=["dp","avatar"])
async def pfp(ctx,*,user:discord.Member=None):
    if ctx.message.author.bot==False:
        if user is None:
            user = ctx.message.author
        try:
            embed=discord.Embed(title="{}'s avatar".format(user.name),color=0xf7d28c)
            embed.set_image(url=user.avatar_url)
            await bot.say(embed=embed)
            print("Avatar")
        except Exception as e:
            await bot.say(e)

@bot.command(pass_context=True,name="ask",aliases=["8ball"])
async def ask(ctx,*,p=None):
    if ctx.message.author.bot==False:
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
                await bot.say(when[var])
            else:
                if result2!=-1:
                    check=len(what)
                    var=random.randint(0,check)
                    await bot.say(what[var])
                else:
                    if result3!=-1:
                        check=len(howmuch)
                        var=random.randint(0,check)
                        await bot.say(howmuch[var])
                    else:
                        if result4!=-1:
                            check=len(howmany)
                            var=random.randint(0,check)
                            await bot.say(howmany[var])
                        else:
                            if result5!=-1:
                                check=len(why)
                                var=random.randint(0,check)
                                await bot.say(why[var])
                            else:
                                if result6!=-1:
                                    check=len(who)
                                    var=random.randint(0,check)
                                    await bot.say(who[var])
                                else:
                                    check=len(other)
                                    var=random.randint(0,check)
                                    await bot.say(other[var])
bot.remove_command("help")
@bot.command(pass_context=True)
async def help(ctx):
    help1="""
:page_with_curl: | Help Message
**General User/Server/Bot Info Commands:**
• -info [@user]→ Provides some information about the user who invoked the command or of mentioned user.
• -svrinfo → Provides some information about the server in which the command is invoked.
• -pfp [@user] → Display avatar of yours or mentioned user.
• -perms [@user] → Display user perms in that server.
• -filter [state] → Use this command to setup filter on your server. Set it off using -filter 0.
• -invite → Add Asuna to your guild.
• -ping → Runs a connection test to Discord.
• -help → Display this message.
**General Query Commands:**
• -google <query> → Searches Google for your query.
• -wiki <query> → Searches Wikipedia for your query.
• -yt <query> → Searches YouTube for your query.
• -weather <location> → Displays weather of given location.
• -pokemon <query> → Gives some data about queried pokemon.
• -ud <word> → Searches Urban Dictionary for your word.
• -define <word> → Searches Dictionary for your word.
• -anime <query> → Searches for given anime details.
• -manga <query> → Searches for given manga details.
• -translate <query> → Translates your input text."""

    help2="""
**General Fun Commands:**
• -quote → Display random motivational code to make your day.
• -ask <question>→ Asuna helps you with your questions.
• -emo <text>→ Emojifies the text.
• -norris [@user] → Display random chuck norris joke.
• -xkcd [number] → Searches xkcd for your comic else prints a random comic.
• -sebi → Display a random SebiSauce.
• -pat [@user]→ Pats somebody's head!.
• -cuddle [@user]→Cuddle somebody with a picture!.
• -slap [@user]→ Slap the baka.
• -punch [@user]→ Give them what they deserve.
• -hug [@user]→ Hug somebody with a picture!
• -kiss [@user]→ Show some love.
• -tickle [@user]→ Don't stop until they cry.
• -sleepy [@user]→ Why not sleeping then?.
• -cry [@user]→ Did someone hurt you?.
• -nom [@user]→ Hungry? have something to eat.
• -gaze [@user]→ Glare at someone.
• -cry [@user]→ Aaawww,did someone make you feel flushed?.
**General Emoji Commands:**
• -emoji <shrug,sip,bang,wonder,yay,peek,dance,j,nom> → Appends that emoji in chat.
• -blob <blush,weary,sleepy,sad,cool,wink,winkf,teeth,unamused,kiss,grr,sob,toj,owo> → Appends your favorite Google blob stickers in chat."""

    help3="""
**General Music Commands:**
• -join <query> → Make the bot join a voice channel.
• -play <query> → Name of the song/url you want to play.
• -playing → Shows info about the currently played songself.
• -volume <value> → Sets the volume of the currently playing song.
• -skip → Vote to skip a song. The song requester can automatically skip.
3 skip votes are needed for the song to be skipped.
• -pause → Pauses the currently played song.
• -resume → Resume the currently played song.
• -leave → Stops playing audio and leaves the voice channel.
This also clears the queue.
*Music commands not working atm*
**Arguments in [] are optional but arguments in <> are necessary for given function to work**
"""
    await bot.whisper(help1)
    await bot.whisper(help2)
    await bot.whisper(help3)
    await bot.say(":inbox_tray: | The list of commands you have access to has been sent to your DMs.")
    print("help")


@bot.command(pass_context=True)
async def code(ctx,*,something=None):
    if ctx.message.author.bot==False:
        if ctx.message.author.id in owner:
            try:
                if something is None:
                    await bot.say("What would you like me to say? :thinking:")
                else:
                    await bot.say("```"+inspect.getsource(bot.get_command(something).callback)+"```")
            except Exception as e:
                await bot.say("Code may be over word limit")
                print(e)
        else:
            await bot.say("I only listen to my owner")
        print("code")

@bot.command(pass_context=True)
async def quote(ctx):
    if ctx.message.author.bot==False:
        try:
            await bot.say("```"+random.choice(quotes)+"```")
            print("quote")
        except Exception as e:
            await bot.say(e)

@bot.command(pass_context=True)
async def invite(ctx):
    if ctx.message.author.bot==False:
        try:
            member = discord.utils
            Asuna = discord.utils.get(ctx.message.server.members, id="411566473350217748")
            embed=discord.Embed(title="Asuna's Invite Link",value="Add Asuna to your guild",color=0xf7d28c)
            embed.add_field(name="Name",value="Asuna")
            embed.add_field(name="Prefix",value="-, Asuna , asuna")
            embed.add_field(name="Link",value="https://discordapp.com/api/oauth2/authorize?client_id=411566473350217748&permissions=8&scope=bot")
            embed.set_footer(text="Feel free to uncheck some permissions")
            embed.set_thumbnail(url=Asuna.avatar_url)
            await bot.say(embed=embed)
            print("invite")
        except Exception as e:
            await bot.say(e)

@bot.command(pass_context=True,name="ud",aliases=["urban"])
async def ud(ctx,*,query=None):
    if ctx.message.author.bot==False:
        if query!=None:
            try:
                defs = udd.define(query)
                for d in range(1):
                    definition=defs[d].definition
                    word=defs[d].word
                    example=defs[d].example
                    upvotes=defs[d].upvotes
                    downvotes=defs[d].downvotes
                embed = discord.Embed(title=word, description="Here's what I could find.", color=0xf7d28c)
                embed.add_field(name="Defintion", value=definition, inline=False)
                embed.add_field(name="Example",value=example if example else "\u200b" ,inline=False)
                embed.add_field(name="Upvotes",value=str(upvotes)+"👍",inline=True)
                embed.add_field(name="Downvotes",value=str(downvotes)+"👎",inline=True)
                await bot.say(embed=embed)
            except Exception:
                await bot.say("Dear User, I could not find a definition for this word in Urban Dictionary")
        print("ud")

@bot.command(pass_context = True,name="purge",aliases=["prune"])
async def purge(ctx, number=2,):
    if ctx.message.author.bot==False:
        if ctx.message.author.server_permissions.manage_messages:
            mgs = []
            number = int(number)
            if number<2:
                number=2
            if number<=100:
                async for x in bot.logs_from(ctx.message.channel, limit = number):
                    mgs.append(x)
                await bot.delete_messages(mgs)
            else:
                temp=0
                while temp!=number:
                    async for x in bot.logs_from(ctx.message.channel, limit = 100):
                        mgs.append(x)
                        temp=temp+1
                        if temp>number:
                            break
                    await bot.delete_messages(mgs)
                print(temp)

        else:
            await bot.say("You do not have required permissions")
        print("purge")

@bot.command(pass_context=True,name="google",aliases=["g","search"])
async def google(ctx,*,query=None):
    if ctx.message.author.bot==False:
       if query!=None:
           try:
                query="-".join(query.split())
                response=urllib.request.urlopen("http://api.tanvis.xyz/search/"+query).read()
                response=json.loads(response.decode("utf-8"))
                await bot.say(response[0]["link"])
           except Exception:
                await bot.say("Service unavailable atm")
       print("google")

@bot.command(pass_context=True,name="wiki",aliases=["wikipedia"])
async def wiki(ctx,*,query=None):
    if ctx.message.author.bot==False:
        if query!=None:
            try:
                query=("-".join(query.split())).encode('utf-8').strip() 
                response=urllib.request.urlopen("http://api.tanvis.xyz/search/"+"wiki"+query).read()
                response=json.loads(response.decode("utf-8"))
                await bot.say(response[0]["link"])
            except Exception:
                 await bot.say("Service unavailable atm")

@bot.command(pass_context=True,name="translate",aliases=["trans"])
async def translate(ctx,*,query=None):
    if ctx.message.author.bot==False:
        if query!=None:
            query="%20".join(query.split())
            response=requests.get("http://api.tanvis.xyz/translate/{}",format(query))
            response = json.loads(r.content.decode('utf-8'))
            await bot.say(response["to"]["text"])
            await bot.say("The input text language is "+response["from"]["lang"])

@bot.command(pass_context=True,name="perms",aliases=["permissions","permission"])
async def perms(ctx,*, user: discord.Member=None):
    if user==None:
        user=ctx.message.author
    var=dict(user.server_permissions)
    str1=""
    for i in var:
        j=i.replace("_"," ")
        if var[i]==True:
             str1+=":small_blue_diamond:"+j.title()+"\n"
        else:
              str1+=":small_orange_diamond:"+j.title()+"\n"
    embed=discord.Embed(title=" Permissions for {} in this server".format(user.name),description=str1,color=0xf7d28c)
    await bot.say(embed=embed)

@bot.command(pass_context=True,name="emo",aliases=["emojify"])
async def emo(ctx,*,word):
    if ctx.message.author.bot==False:
        if word!=None:
            try:
                str=""
                for char in word:
                    if char.isalpha():
                        str+=":regional_indicator_"+char+":"
                    else:
                        str+=(char+"  ")
                await bot.say(str.lower())
            except Exception as e:
                await bot.say(e)
        print("emo")

@bot.command(pass_context=True,name="norris",aliases=["chuck","chuck norris"])
async def norris(ctx,*, user: discord.Member=None):
    if ctx.message.author.bot==False:
        try:
            if user is None:
                user ="Chuck Norris"
            else:
                user=user.name
            word=q.random(str(user))
            embed=discord.Embed(name="Chuck Norris",color=0xf7d28c)
            embed.add_field(name="Chuck Norris",value=word)
            embed.set_thumbnail(url="https://cdn.dribbble.com/users/24711/screenshots/1701350/chuck_norris_2x.png")
            await bot.say(embed=embed)
            print("norris")
        except Exception as e:
            await bot.say(e)

@bot.command(pass_context=True)
async def xkcd(ctx,number=None):
    if ctx.message.author.bot==False:
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
                await bot.say(embed=embed)
            else:
                number=int(number)
                limit=com.getLatestComicNum()
                if number<1 or number>limit:
                    await bot.say("Invalid comic number :sweat_smile:")
                else:
                    a=com.getComic(number, silent=True)
                    title=a.getTitle()
                    link=a.getImageLink()
                    exp=a.getExplanation()
                    embed=discord.Embed(title="Xkcd",color=0xf7d28c)
                    embed.add_field(name="Title",value=title,inline=False)
                    embed.set_footer(text=("For explanation refer to: "+exp))
                    embed.set_image(url=link)
                    await bot.say(embed=embed)
            print("xkcd")
        except Exception as e:
            await bot.say(e)

@bot.command()
async def whatif():
    a=com.getRandomWhatIf()
    link=a.getLink()
    await bot.say(link)

@bot.command(pass_context=True)
async def weather(ctx,*,location=None):
    if ctx.message.author.bot==False:
        if location!=None:
            try:
                location="-".join(location.split())
                response = urllib.request.urlopen('http://api.tanvis.xyz/weather/'+location).read()
                response = json.loads(response.decode('utf-8'))
                namee=response["name"]
                celsiuse=response["celsius"]
                farenheite=response["fahrenheit"]
                weathere=response["weather"]
                link=response["icon"]
                windspeede=response["windSpeed"]
                embed=discord.Embed(tile="Weather",description="Here's what i could find: ",color=0xf7d28c)
                embed.add_field(name="Location",value=namee)
                embed.add_field(name="Temp in Celsius",value=celsiuse)
                embed.add_field(name="Temp in Fahrenheit",value=farenheite)
                embed.add_field(name="Weather",value=weathere)
                embed.add_field(name="Wind Speed",value=windspeede)
                embed.set_thumbnail(url=link)
                await bot.say(embed=embed)
                print("weather")
            except Exception:
                await bot.say("Given location not found")

@bot.command(pass_context=True,name="pokemon",aliases=["poke"])
async def pokemon(ctx,pokemon=None):
    if ctx.message.author.bot==False:
        if pokemon!=None:
            try:
                response=urllib.request.urlopen("http://api.tanvis.xyz/pokedex/"+pokemon).read()
                response=json.loads(response.decode("utf-8"))
                name=response["name"]
                num=response["number"]
                image=response["image"]
                species=response["species"]
                height=response["height"]
                weight=response["weight"]
                check1=response["types"]
                types=""
                for t in check1:
                    types+=(t+" ")
                types=",".join(types.split())
                check2=response["abilities"]
                abilities=""
                for t in check2:
                    abilities+=(t+" ")
                abilities=",".join(abilities.split())
                des=response["description"]
                ts=response["baseStats"]["total"]
                hp=response["baseStats"]["hp"]
                attack=response["baseStats"]["attack"]
                defense=response["baseStats"]["defense"]
                spAttack=response["baseStats"]["spAttack"]
                spDefense=response["baseStats"]["spDefense"]
                speed=response["baseStats"]["speed"]
                embed=discord.Embed(title="{}'s info".format(name),desciption="Here's what i could find: ",color=0xf7d28c)
                embed.add_field(name="Pokedex Number",value=num)
                embed.add_field(name="Species",value=species)
                embed.add_field(name="Height",value=height)
                embed.add_field(name="Weight",value=weight)
                embed.add_field(name="Types",value=types)
                embed.add_field(name="Abilities",value=abilities)
                embed.add_field(name="Description",value=des)
                embed.add_field(name="Total Stats",value=ts)
                embed.add_field(name="Attack",value=attack)
                embed.add_field(name="Defense",value=defense)
                embed.add_field(name="Special Attack",value=spAttack)
                embed.add_field(name="Special Defense",value=spDefense)
                embed.add_field(name="Speed",value=speed)
                embed.set_image(url=image)
                await bot.say(embed=embed)
            except Exception:
                await bot.say("Given pokemon not found")
            print("pokemon")

@bot.command(pass_context=True,name="yt",aliases=["youtube","Youtube"])
async def yt(ctx,*,query=None):
    if ctx.message.author.bot==False:
        if query!=None:
            try:
                query="-".join(query.split())
                response=urllib.request.urlopen("http://api.tanvis.xyz/youtube/"+query).read()
                response=json.loads(response.decode("utf-8"))
                name1=response[0]["name"]
                image=response[0]["thumbnail"]
                link1=response[0]["link"]
                name2=response[1]["name"]
                name3=response[2]["name"]
                link2=response[1]["link"]
                link3=response[2]["link"]
                embed=discord.Embed(title="YouTube",description="Here's what i could find",color=0xf7d28c)
                embed.add_field(name=name1,value=link1)
                embed.set_thumbnail(url=image)
                embed.add_field(name=name2,value=link2)
                embed.add_field(name=name3,value=link3)
                await bot.say(embed=embed)
                print("yt")
            except Exception as e:
                await bot.say(e)

@bot.command(pass_context=True,name="define",aliases=["def","dict","dictionary"])
async def define(ctx,*,word=None):
    if ctx.message.author.bot==False:
        if word!=None:
            try:
                new_instance = Thesaurus(word)
                list1=new_instance.get_definition()
                counter=1
                stri=""
                for i in list1:
                    j=i.replace("(","")
                    k=j.replace(")","")
                    stri+=(str(counter)+". "+k.capitalize()+".\n")
                    counter+=1
                await bot.say(stri)
            except Exception:
                await bot.say("Dear User, I could not find a definition for this word.")

@bot.command(pass_context=True,name="sebi",aliases=["sebisauce","Sebi"])
async def sebi(ctx):
    if ctx.message.author.bot==False:
        try:
            response=urllib.request.urlopen("https://sebisauce.herokuapp.com/api/random").read()
            response=json.loads(response.decode("utf-8"))
            url=response["file"]
            embed=discord.Embed(title="SebiSauce",color=0xf7d28c)
            embed.set_image(url=url)
            await bot.say(embed=embed)
            print("sebi")
        except Exception as e:
            await bot.say(e)



@bot.command(pass_context=True)
async def anime(ctx,*,query):
    if ctx.message.author.bot==False:
        try:
            creds=spice.init_auth("gauravgupta", "gj111999@")
            test=spice.search(query, spice.get_medium('anime'),creds)
            list1=""
            count=1
            for i in test:
                list1+=(str(count)+". "+i.title+"\n")
                count+=1
            if list1!="":
                await bot.say("```\n"+list1+"\n```")
                m =await bot.wait_for_message(author=ctx.message.author, timeout=30)
                m=int(m.content)
                m=m-1
                try:
                    mgs = []
                    async for x in bot.logs_from(ctx.message.channel, limit = 2):
                        mgs.append(x)
                    await bot.delete_messages(mgs)
                except:
                    pass
                ids=test[m].id
                title=test[m].title
                episode=test[m].episodes
                score=float(test[m].score)
                typea=test[m].anime_type
                status=test[m].status
                date=test[m].dates
                date=list(date)
                syno1=test[m].synopsis
                syno2=syno1.replace('<br />', '')
                syno3=syno2.replace("[Written by MAL Rewrite]", "")
                syno4=syno3.replace("[i]","")
                syno5=syno4.replace("[/i]","")
                syno=syno5.replace("&#039;","'")
                link=test[m].image_url
                if score>=0 and score<2:
                    emoji=":disappointed:"
                elif score>=2 and score<4:
                    emoji=":grimacing:"
                elif score>=4 and score<6:
                    emoji=":neutral_face:"
                elif score>=6 and score<9:
                    emoji=":smiley:"
                elif score>=9:
                    emoji=":heart_eyes:"
                if status=="Currently Airing":
                    embed=discord.Embed(title="{}".format(title),color=0xf7d28c)
                    embed.add_field(name="Synopsis",value=syno)
                    embed.add_field(name="Type",value=typea)
                    embed.add_field(name="Episodes",value=episode,inline=True)
                    embed.add_field(name="Status",value=status)
                    embed.add_field(name="Started",value=date[0])
                    embed.add_field(name="Score",value=(str(score)+" "+emoji))
                    embed.set_thumbnail(url=link)
                    await bot.say(embed=embed)
                else:
                    embed=discord.Embed(title="{}".format(title),color=0xf7d28c)
                    embed.add_field(name="Synopsis",value=syno)
                    embed.add_field(name="Type",value=typea)
                    embed.add_field(name="Episodes",value=episode,inline=True)
                    embed.add_field(name="Status",value=status)
                    embed.add_field(name="Started",value=date[0])
                    embed.add_field(name="Finished",value=date[1])
                    embed.add_field(name="Score",value=(str(score)+" "+emoji))
                    embed.set_thumbnail(url=link)
                    await bot.say(embed=embed)
            else:
                await bot.say("Given Anime not found")
        except Exception as e:
            await bot.say("Service unavailable atm")
            print(e)


@bot.command(pass_context=True)
async def manga(ctx,*,query):
    if ctx.message.author.bot==False:
        try:
            creds=spice.init_auth("gauravgupta", "gj111999@")
            test=spice.search(query, spice.get_medium('manga'),creds)
            list1=""
            count=1
            for i in test:
                list1+=(str(count)+". "+i.title+"\n")
                count+=1
            if list1!="":
                await bot.say("```\n"+list1+"\n```")
                m =await bot.wait_for_message(author=ctx.message.author, timeout=30)
                m=int(m.content)
                m=m-1
                try:
                    mgs = []
                    async for x in bot.logs_from(ctx.message.channel, limit = 2):
                        mgs.append(x)
                    await bot.delete_messages(mgs)
                except:
                    pass
                ids=test[m].id
                title=test[m].title
                episode=test[m].chapters
                score=float(test[m].score)
                typea=test[m].manga_type
                status=test[m].status
                syno1=test[m].synopsis
                syno2=syno1.replace('<br />', '')
                syno3=syno2.replace("[Written by MAL Rewrite]", "")
                syno4=syno3.replace("[i]","")
                syno5=syno4.replace("[/i]","")
                syno=syno5.replace("&#039;","'")
                link=test[m].image_url
                if score>=0 and score<2:
                    emoji=":disappointed:"
                elif score>=2 and score<4:
                    emoji=":grimacing:"
                elif score>=4 and score<6:
                    emoji=":neutral_face:"
                elif score>=6 and score<9:
                    emoji=":smiley:"
                else:
                    emoji=":heart_eyes:"
                embed=discord.Embed(title="{}".format(title),color=0xf7d28c)
                embed.add_field(name="Synopsis",value=syno)
                embed.add_field(name="Type",value=typea)
                embed.add_field(name="Chapters",value=episode,inline=True)
                embed.add_field(name="Status",value=status)
                embed.add_field(name="Score",value=(str(score)+" "+emoji))
                embed.set_thumbnail(url=link)
                await bot.say(embed=embed)
            else:
                await bot.say("Given Manga not found")
        except Exception as e:
            await bot.say("Service unavailable atm")
            print(e)

@bot.command(pass_context=True,name="fact",aliases=["facts","fun facts","fun fact","trivia","random","bored"])
async def fact(ctx):
    r=requests.get("http://numbersapi.com/random/trivia")
    await bot.say(r.content)

@bot.command(pass_context=True,name="lyrics",aliases=["lyric","lines"])
async def lyrics(ctx,*,song):
    if ctx.message.author.bot==False:
        try:
        #     song="%20".join(song.split())
        #     r=requests.get('http://api.musixmatch.com/ws/1.1/track.search?q_track={}&page_size=1&page=1&s_track_rating=desc&apikey=9da66e17efa9fc8d188c6cf152a2b21f'.format(song))
        #     response = json.loads(r.content.decode('utf-8'))
        #     t=response["message"]["body"]["track_list"][0]["track"]["track_id"]
        #     p=requests.get('http://api.musixmatch.com/ws/1.1/track.lyrics.get?track_id={}&apikey=9da66e17efa9fc8d188c6cf152a2b21f'.format(t))
        #     responses= json.loads(p.content.decode('utf-8'))
        #     k=responses["message"]["body"]["lyrics"]["lyrics_body"].split("\n\n")
        #     embed=discord.Embed(title="{}".format(response["message"]["body"]["track_list"][0]["track"]["track_name"]),color=0xf7d28c)
        #     for a in k:
        #             embed.add_field(name="\u200b",value=a+"\n")
        #     embed.set_footer(text=responses["message"]["body"]["lyrics"]["lyrics_copyright"],url=responses["message"]["body"]["lyrics"]["script_tracking_url"])
        #     try:
        #         img=response["message"]["body"]["track_list"][0]["track"]["album_coverart_100x100"]
        #         embed.set_thumbnail(url=img)
        #         await bot.say(embed=embed)
        #     except Exception:
        #         await bot.say(embed=embed)
        # except Exception as e:
        #     await bot.say("Lyrics not available for this song. Are you sure you entered correct details?")
        #     print(e)
            await bot.say(":mag: Singer Name")
            singer =await bot.wait_for_message(author=ctx.message.author, timeout=30)
            singer=str(singer.content)
            print(song,singer)
            l = lyricwikia.get_lyrics(singer, song)
            str1=""
            ls=l.split("\n\n")
            embed=discord.Embed(title="{}".format(song.title()),color=0xf7d28c)
            for a in ls:
                    embed.add_field(name="\u200b",value=a+"\n")
            await bot.say(embed=embed)
        except Exception as e:
            await bot.say("Lyrics not available for this song. Are you sure you entered correct details?")
            print(e)
		
# @bot.command(pass_context=True,name="ecard",aliases=["kaiji"])
# async def ecard(ctx,bet):



@bot.command(pass_context=True,name="bj",aliases=["blackjack"])
async def bj(ctx,bet,user: discord.Member=None):
    if user==None:
        user=ctx.message.author
    start=int(bet)
    startf=start
    bal=0
    d_valuea=[]
    fc=["KING","QUEEN","JACK"]
    for i in range(3):
        await bot.say("Round {}".format(i+1))
        await bot.say("Betting Amount: ")
        bet =await bot.wait_for_message(author=ctx.message.author, timeout=30)
        bet=int(bet.content)
        if bet>startf:
            await bot.say("You cannot bet more than {} so resetting your bet value to {}".format(startf,startf))
            bet=startf
        r=requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
        r= json.loads(r.content.decode('utf-8'))
        deck=r["deck_id"]
        draw=requests.get("https://deckofcardsapi.com/api/deck/{}/draw/?count=2".format(deck))
        draw= json.loads(draw.content.decode('utf-8'))
        u_value=0
        u_cards=[]
        d_cards=[]
        for j in range(2):
            if draw["cards"][j]["value"] in fc:
                u_value+=10
            elif draw["cards"][j]["value"]=="ACE":
                u_value+=11
            else:
                u_value+=int(draw["cards"][j]["value"])
            u_cards.append(draw["cards"][j]["code"])
        d_value=0
        draw=requests.get("https://deckofcardsapi.com/api/deck/{}/draw/?count=1".format(deck))
        draw= json.loads(draw.content.decode('utf-8'))
        if draw["cards"][0]["value"] in fc:
            d_value+=10
        elif draw["cards"][0]["value"]=="ACE":
            d_value+=11
        else:
            d_value+=int(draw["cards"][0]["value"])
        d_cards.append(draw["cards"][0]["code"])
        d_valuea.append(d_value) 
        q=""
        w=""
        for a in u_cards:
            q+=(a+" ")
        for b in d_cards:
            w+=(b+" ")
        embed=discord.Embed(title="Blackjack",color=0xf7d28c)  
        embed.add_field(name="Betting Amount",value=bet)
        embed.add_field (name="User Cards",value=q)
        embed.add_field(name="Dealer Cards",value=w)
        embed.add_field(name="\u200b",value="Hit/Stand/Double Down")
        await bot.say(embed=embed)
        # print(u_value,d_value)
        option =await bot.wait_for_message(author=ctx.message.author, timeout=30)
        option=str(option.content)
        if option.lower()=="hit":
            draw=requests.get("https://deckofcardsapi.com/api/deck/{}/draw/?count=1".format(deck))
            draw= json.loads(draw.content.decode('utf-8'))
            if draw["cards"][0]["value"] in fc:
                u_value+=10
            elif draw["cards"][0]["value"]=="ACE":
                u_value+=11
            else:
                u_value+=int(draw["cards"][0]["value"])
            u_cards.append(draw["cards"][0]["code"])
        elif option.lower()=="double down":
            bet=bet*2
            draw=requests.get("https://deckofcardsapi.com/api/deck/{}/draw/?count=1".format(deck))
            draw= json.loads(draw.content.decode('utf-8'))
            if draw["cards"][0]["value"] in fc:
                u_value+=10
            elif draw["cards"][0]["value"]=="ACE":
                u_value+=11
            else:
                u_value+=int(draw["cards"][0]["value"])
            u_cards.append(draw["cards"][0]["code"])
        else:
            bet=bet
        draw=requests.get("https://deckofcardsapi.com/api/deck/{}/draw/?count=2".format(deck))
        draw= json.loads(draw.content.decode('utf-8'))
        for k in range(2):
            if draw["cards"][k]["value"] in fc:
                d_value+=10
            elif draw["cards"][k]["value"]=="ACE":
                d_value+=11
            else:
                d_value+=int(draw["cards"][k]["value"])
            d_valuea.append(d_value)
            d_cards.append(draw["cards"][k]["code"])
        for i in d_valuea:
            if i<=21:
                d_value=i
        try:
            mgs = []
            async for x in bot.logs_from(ctx.message.channel, limit = 2):
                mgs.append(x)
            await bot.delete_messages(mgs)
        except:
            pass
    # print(u_value,d_value)
        if u_value>21:
            bal=bal-bet
            if bal>0:
                start=start-bal
                start=start*(1.5)
            else:
                start=start*(1.5)
            q=""
            w=""
            for a in u_cards:
                q+=(a+" ")
            for b in d_cards:
                w+=(b+" ")
            embed=discord.Embed(title="Blackjack",color=0xf23c3c)  
            embed.add_field(name="Betting Amount",value=bet)
            embed.add_field (name="User Cards",value=q)
            embed.add_field(name="Dealer Cards",value=w)
            embed.add_field(name="\u200b",value="Bust of {}".format(bet))
            await bot.say(embed=embed)
        elif u_value<=21 and u_value>=d_value:
            bal+=bet*2
            if bal>0:
                start=start-bal
                start=start*(1.5)
            else:
                start=start*(1.5)
            q=""
            w=""
            for a in u_cards:
                q+=(a+" ")
            for b in d_cards:
                w+=(b+" ")
            embed=discord.Embed(title="Blackjack",color=0x3cf279)  
            embed.add_field(name="Betting Amount",value=bet)
            embed.add_field (name="User Cards",value=q)
            embed.add_field(name="Dealer Cards",value=w)
            embed.add_field(name="\u200b",value="You won {}".format(bet*2))
            await bot.say(embed=embed)
        else:
            bal=bal-bet
            if bal>0:
                start=start-bal
                start=start*(1.5)
            else:
                start=start*(1.5)
            q=""
            w=""
            for a in u_cards:
                q+=(a+" ")
            for b in d_cards:
                w+=(b+" ")
            embed=discord.Embed(title="Blackjack",color=0xf23c3c)  
            embed.add_field(name="Betting Amount",value=bet)
            embed.add_field (name="User Cards",value=q)
            embed.add_field(name="Dealer Cards",value=w)
            embed.add_field(name="\u200b",value="Bust of {}".format(bet))
            await bot.say(embed=embed)
        if i>0:
            try:
                mgs = []
                async for x in bot.logs_from(ctx.message.channel, limit = 1):
                    mgs.append(x)
                await bot.delete_messages(mgs)
            except:
                pass
    embed=discord.Embed(title="Blackjack",color=0xf7d28c)  
    embed.add_field(name="\u200b",value="Credits at end of game: {}".format(bal-start))
    await bot.say(embed=embed)
    with open("bjlb.txt", "a") as f1:
            f1.write("\n"+user+" "+str(bal-start))

@bot.command(pass_context=True,name="lb",aliases=["leaderboard"])
async def lb(ctx):
    with open("bjlb.txt", "r") as f1:
        list1=f1.readlines()
        if len(list1>10):
            limit=11
        else:
            limit=len(list1)+1
        p="```"
        for i in range(1,limit):
            a=f1.readline()
            p+=a+"\n"
        p+="```"
        await bot.say(p)

@bot.command()
async def big(emo):
        """Enlarge emoji"""
        emo = emo.split(':')[-1].replace('>' , '')
        await bot.say("https://discordapp.com/api/emojis/{}.png".format(emo))

#blob commands
@bot.group(pass_context=True)
async def blob(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say("Invalid blob command passed...")
@blob.command(pass_context=True)
async def blush(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:blush:436934532587847681>")
        await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def weary(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:weary:436934578415075331>")
        await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def sleepy(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:sleepy:436934625164656659>")
        await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def sad(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:sad:436934649563054090>")
        await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def cool(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:cool:436934671117582356>")
        await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def wink(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:wink:436934691141058561>")
        await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def winkf(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:winkf:436934713077268480>")
        await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def teeth(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:teeth:436934738771574797>")
        await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def unamused(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:not_like:436934761962012702>")
        await bot.delete_message(ctx.message)
@blob.command(pass_context=True)        
async def owo(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:OwO:458251627443519488>")
        await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def kiss(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:kiss:436934782803378187>")
        await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def grr(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:grr:436934802331926529>")
        await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def sob(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:sob:436934823492190210>")
        await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def toj(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:tears_of_joy:436934851040378900>")
        await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def sweat(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:blobsweat:435149054528454670>")
        await bot.delete_message(ctx.message)

#Emoji commands
@bot.group(pass_context=True)
async def emoji(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say('Invalid emoji command passed...')
@emoji.command(pass_context=True)
async def shrug(ctx):
    if ctx.message.author.bot==False:
        await bot.say("¯\_(ツ)_/¯")
        await bot.delete_message(ctx.message)
@emoji.command(pass_context=True)
async def mikuyay(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:mikuyay:434019400073347072>")
        await bot.delete_message(ctx.message)
@emoji.command(pass_context=True)
async def sip(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:sip:434254079246467075>")
        await bot.delete_message(ctx.message)
@emoji.command(pass_context=True)
async def j(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:j_:434254490745569282>")
        await bot.delete_message(ctx.message)
@emoji.command(pass_context=True)
async def dance(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:dance:434236128904609796>")
        await bot.delete_message(ctx.message)
@emoji.command(pass_context=True)
async def peek(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:peeking:435149270518333460>")
        await bot.delete_message(ctx.message)
@emoji.command(pass_context=True)
async def bang(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:bang:435149143577460752>")
        await bot.delete_message(ctx.message)
@emoji.command(pass_context=True)
async def wonder(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:wonder:435147959101947905>")
        await bot.delete_message(ctx.message)
@emoji.command(pass_context=True)
async def nom(ctx):
    if ctx.message.author.bot==False:
        await bot.say("<a:nom:456715700845674509>")
        await bot.delete_message(ctx.message)        
        

bot.run("NDExNTY2NDczMzUwMjE3NzQ4.DWRS8A.U2VKbHmJAbktNhhgOhSNcpgwGt4")