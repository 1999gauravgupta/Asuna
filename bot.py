import discord
import codecs
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import json
import urbandictionary as udd
import urllib
import string
import chucknorris.quips as q
import xkcd as com
import requests
from googlesearch import search
import time
#for files
with codecs.open("quotes.json", "r",encoding='utf-8', errors='ignore') as f:
    quotes= json.load(f)

bot = commands.Bot(command_prefix=['-','asuna ',"Asuna "])
client=discord.Client()

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

@bot.command(pass_context=True)
async def ping(self):
        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        tim = (after-before)*1000
        await self.bot.say("**Pong 🏓, took {0:.0f}ms**".format(tim))
        print("ping")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member=None):
    if user is None:
        user = ctx.message.author
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

@bot.command(pass_context=True)
async def svrinfo(ctx):
    embed = discord.Embed(title= (ctx.message.server.name+" info"), description="Here's what I could find.", color=0xf7d28c)
    embed.add_field(name="Name", value=ctx.message.server.name)
    embed.add_field(name="ID", value=ctx.message.server.id)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles))
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)
    print("Server Info")

@bot.command(pass_context=True)
async def say(ctx,*,something=None):
    if ctx.message.author.id=="343395225571426304":
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
    if ctx.message.author.id=="343395225571426304" :
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
async def pfp(ctx,user:discord.Member=None):
    if user is None:
        user = ctx.message.author
    embed=discord.Embed(title="{}'s avatar".format(user.name),color=0xf7d28c)
    embed.set_image(url=user.avatar_url)
    await bot.say(embed=embed)
    print("Avatar")

@bot.command(pass_context=True,name="ask",aliases=["8ball"])
async def ask(ctx,*,p=None):
    if p!=None:
        p=p.lower()
        when= ['Soon™', 'Maybe tomorrow.', 'Maybe next year...', 'Right now.', 'In a few months.']
        what= ['A plane.', 'What? Ask again.', 'A gift.', 'Nothing.', 'A ring.', 'I do not know', "Maybe something."]
        howmuch= ['A lot.', 'A bit.', 'A few.', 'Ask me tomorrow.', 'I do not know, ask a physicist.', 'Nothing.', "2 or 3 liters, I don't remember.", 'Infinity.', '1010 liters.']
        howmany= ['A lot.', 'A bit.', 'A few.', 'Ask me tomorrow.', "I don't know, ask a physicist.", 'Nothing.', '2 or 3, I do not remember.', 'Infinity', '1010.']
        why= ['Maybe genetics.', 'Because somebody decided it.', 'For the glory of satan, of course!', 'I do not know, maybe destiny.', 'Because I said so.', 'I have no idea.', 'Harambe did nothing wrong.', 'Ask the owner of this server.', 'Ask again.', 'To get to the other side.', 'It says so in the Bible.']
        who= ['A human.', 'A robot.', 'An airplane.', 'A bird.', 'A carbon composition.', 'A bunch of zeroes and ones.', 'I have no clue, is it material?', 'That is not logical.']
        other= ['Most likely.', 'Nope.', 'YES!', 'Maybe.']
        result1 = p.find('when')
        result2 = p.find('what')
        result3 = p.find('how much')
        result4 = p.find('how many')
        result5 = p.find('why')
        result6 = p.find('who')
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

**General Fun Commands:**
• -quote → Display random motivational code to make your day.
• -ask <question>→ Asuna helps you with your questions.
• -emo <text>→ Emojifies the text.
• -norris [@user] → Display random chuck norris joke.
• -xkcd [number] → Searches xkcd for your comic else prints a random comic.
• -sebi → Display a random SebiSauce.[Service not available atm]
• -pat [@user]→ Pats somebody's head!.
• -cuddle [@user]→Cuddle somebody with a picture!.
• -slap [@user]→ Slap the baka.
• -hug [@user]→ Hug somebody with a picture!

**General Emoji Commands:**
• -emoji <shrug,sip,bang,wonder,mikuyay,peek,dance,j> → Appends that emoji in chat.
• -blob <blush,weary,sleepy,sad,cool,wink,winkf,teeth,notlike,kiss,grr,sob,toj> → Appends your favorite Google blob stickers in chat.

**Arguments in [] are optional but arguments in <> are necessary for given function to work**
"""
    await bot.whisper(help1)
    await bot.say(":inbox_tray: | The list of commands you have access to has been sent to your DMs.")
    print("help")

@bot.command()
async def quote():
    await bot.say("```"+random.choice(quotes)+"```")
    print("quote")

@bot.command(pass_context=True)
async def invite(ctx):
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

@bot.command(name="ud",aliases=["urban"])
async def ud(query=None):
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
       if query!=None:
           list1=[]
           for url in search(query, stop=1):
                list1.append(url)
           await bot.say(list1[0])
       print("google")

@bot.command(pass_context=True,name="wiki",aliases=["wikipedia"])
async def wiki(ctx,*,query=None):
    if query!=None:
        list1=[]
        query+="wikipedia"
        for url in search(query, stop=1):
                list1.append(url)
        await bot.say(list1[0])
    print("wikipedia")


@bot.command(pass_context=True,name="emo",aliases=["emojify"])
async def emo(ctx,*,word):
    if word!=None:
        str=""
        for char in word:
            if char.isalpha():
                str+=":regional_indicator_"+char+":"
            else:
                str+=(char+"  ")
        await bot.say(str.lower())
    print("emo")

@bot.command(pass_context=True,name="norris",aliases=["chuck","chuck norris"])
async def norris(ctx, user: discord.Member=None):
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

@bot.command()
async def xkcd(number=None):
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

@bot.command()
async def whatif():
    a=com.getRandomWhatIf()
    link=a.getLink()
    await bot.say(link)

@bot.command()
async def weather(*,location=None):
    if location!=None:
        try:
            location="-".join(location.split())
            response = urllib.request.urlopen('https://cheeze.club/api/weather/'+location).read()
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
        except KeyError:
            await bot.say("Given location not found")

@bot.command(name="pokemon",aliases=["poke"])
async def pokemon(pokemon=None):
    if pokemon!=None:
        try:
            response=urllib.request.urlopen("https://cheeze.club/api/pokedex/"+pokemon).read()
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
        except ValueError:
            await bot.say("Given pokemon not found")
        print("pokemon")

@bot.command(name="define",aliases=["dict","dictioanry"])
async def define(*,word=None):
    if word!=None:
        try:
            word=word.title()
            response=urllib.request.urlopen("https://cheeze.club/api/dictionary/"+word).read()
            response=json.loads(response.decode("utf-8"))
            definition=response["noun"][0]["definition"]
            example=response["noun"][0]["example"]
            embed=discord.Embed(title="{}'s info".format(word),description="Here's what i could find",color=0xf7d28c)
            embed.add_field(name="Definition",value=definition)
            embed.add_field(name="Example",value=example)
            await bot.say(embed=embed)
            print("define")
        except KeyError:
            await bot.say("Dear User, I could not find a definition for this word.")

@bot.command(name="yt",aliases=["youtube","Youtube"])
async def yt(*,query=None):
    if query!=None:
        query="-".join(query.split())
        response=urllib.request.urlopen("https://cheeze.club/api/youtube/"+query).read()
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

# @bot.command()
# async def translate(*,query=None):
#     if query!=None:
#         await bot.say(query)
#         response=urllib.request.urlopen("https://cheeze.club/api/translate/"+query).read()
#         print(response)
#         await bot.say(response)

@bot.command(name="sebi",aliases=["sebisauce","Sebi"])
async def sebi():
    response=urllib.request.urlopen("https://sebisauce.herokuapp.com/api/random").read()
    response=json.loads(response.decode("utf-8"))
    url=response["file"]
    embed=discord.Embed(title="SebiSauce",color=0xf7d28c)
    embed.set_image(url=url)
    await bot.say(embed=embed)
    print("sebi")

@bot.command(pass_context=True,name="pat",aliases=["pats"])
async def pat(ctx, user: discord.Member=None):
        link=["https://media1.tenor.com/images/1e92c03121c0bd6688d17eef8d275ea7/tenor.gif","https://thumbs.gfycat.com/FoolhardyJoyousBear-max-1mb.gif","https://media1.tenor.com/images/f79a9ec48bde0e592e55447b17ecfbad/tenor.gif","https://cdn.weeb.sh/images/Sk2FyQHpZ.gif","https://cdn.weeb.sh/images/B1PnJJYP-.gif","https://cdn.weeb.sh/images/Sky1x1YwW.gif","https://cdn.weeb.sh/images/SktIxo20b.gif","https://cdn.weeb.sh/images/Sk2f7J39G.gif","https://cdn.weeb.sh/images/B1TQcTNCZ.gif","https://cdn.weeb.sh/images/SJLaWWRSG.gif"]  
        p=link[random.randint(0,len(link)-1)]      
        if user!=None:
            embed=discord.Embed(description="{} gently pats {} <:pats:436961578961600512>".format(ctx.message.author.name,user.name),color=0xf7d28c)
        else:
            embed=discord.Embed(title="There there, i will pat you {} <:pats:436961578961600512>".format(ctx.message.author.name),color=0xf7d28c)
        embed.set_image(url=p)
        await bot.say(embed=embed)

@bot.command(pass_context=True,name="cuddle",aliases=["cuddles"])
async def cuddle(ctx, user: discord.Member=None):
    link= [
"https://cdn.discordapp.com/attachments/424460621053034497/436497239221862400/S4WQfufMwrP33qaWTpUbY327OiY.gif", "https://cdn.discordapp.com/attachments/424460621053034497/436496258249654272/TRcGA-wb3FBs39e7haOFTe-mA_s.gif", "https://cdn.discordapp.com/attachments/424460621053034497/436495448396660737/zC4nmZRNAcR_HUz1idD6GE-V9iY.gif", "https://cdn.weeb.sh/images/BywGX8caZ.gif", "https://cdn.weeb.sh/images/BkTe8U7v-.gif", "https://cdn.weeb.sh/images/ryfyLL7D-.gif", "https://cdn.discordapp.com/attachments/424460621053034497/436487630515994634/C-8H8sShkykA_pfng9WrWrGncHU.gif", "https://cdn.weeb.sh/images/SJbGLUQwZ.gif",
"https://cdn.discordapp.com/attachments/424460621053034497/436497045491154974/aW0d0t965qyCKT1gAbZkLJvIrKg.gif",
"https://cdn.weeb.sh/images/SJLkLImPb.gif",
"https://cdn.weeb.sh/images/BJCCd_7Pb.gif",
"https://cdn.discordapp.com/attachments/424460621053034497/436508238142242816/BbpmqdFoWtePuhOQu_AAvOey4i4.gif",
"https://cdn.discordapp.com/attachments/424460621053034497/436508843296423947/VBSyXo7VbTRkki3LE4oLvu2j7Tw.gif"]
    p=link[random.randint(0,len(link)-1)]      
    if user!=None:
            embed=discord.Embed(description="{} cuddles {} <:cuddle:436520636278374429>".format(ctx.message.author.name,user.name),color=0xf7d28c)
    else:
            embed=discord.Embed(description="Here {} have some cuddles <:cuddle:436520636278374429>".format(ctx.message.author.name),color=0xf7d28c)
    embed.set_image(url=p)
    await bot.say(embed=embed)

@bot.command(pass_context=True,name="hug",aliases=["hugs"])
async def hug(ctx, user: discord.Member=None):
    link= [
"https://cdn.discordapp.com/attachments/424460621053034497/436488319438815232/OoEK1pufpxGvpfWA-qL8DuSoLtk.gif", 
"https://cdn.discordapp.com/attachments/424460621053034497/436492112175824896/mqC9WtmX2LFyTRqw8ux26ziuSEE.gif", "https://cdn.discordapp.com/attachments/424460621053034497/436488752869933056/y-Qzmrr1NMMFUqGTB3kDUSs0V1E.gif",
"https://cdn.discordapp.com/attachments/424460621053034497/436492528553033728/Njo4sAAJYsVV8vErcujEPQChhy0.gif",
"https://cdn.weeb.sh/images/HyNJIaVCb.gif",
"https://cdn.discordapp.com/attachments/424460621053034497/436505988452057088/f8aqtullCnYLfTZ-sclVtyOiYUw.gif",
"https://cdn.discordapp.com/attachments/424460621053034497/436506633263251465/Yh2-H4-hgeOvI8E5bQBPvZQZTgk.gif",
"https://cdn.discordapp.com/attachments/424460621053034497/436507047392051200/Y1imtlb9MAhTxzhQz2ZyervdhQU.gif",
"https://cdn.discordapp.com/attachments/424460621053034497/436507914824318976/XpPkI_Q9y2bKiV8l3zVStJwUfws.gif",
"https://cdn.discordapp.com/attachments/424460621053034497/436509146448134144/jeOuIHlc_cWbxfHx8fcuIvAQ2eA.gif",
"https://cdn.discordapp.com/attachments/424460621053034497/436509947237236746/AjLRblhWqwoCH1E05C0I3zhOx74.gif",
"https://cdn.discordapp.com/attachments/424460621053034497/436510123217911808/v47c1jnQvxv3m3QQPg0LDEO7puA.gif",
"https://cdn.discordapp.com/attachments/424460621053034497/436510371931750410/2derXdykHPW1hVIrhKBsYvfjFkw.gif",
"https://cdn.discordapp.com/attachments/424460621053034497/436510649770573845/nTphroCP85a9C4Ny77VnOStOc0.gif",
"https://cdn.discordapp.com/attachments/429288271122792469/436511361636499457/PkwyV8KjIp2Mcsg5-X89uLVrPc0.gif"]
    p=link[random.randint(0,len(link)-1)]      
    if user!=None:
            embed=discord.Embed(description="{} tightly hugs {} <:hug:436520609980219415>".format(ctx.message.author.name,user.name),color=0xf7d28c)
    else:
            embed=discord.Embed(description="There you go {} hugs <:hug:436520609980219415>".format(ctx.message.author.name),color=0xf7d28c)
    embed.set_image(url=p)
    await bot.say(embed=embed)

@bot.command(pass_context=True,name="slap",aliases=["slaps"])
async def slap(ctx, user: discord.Member=None):
    link= ["https://cdn.weeb.sh/images/ByTR7kFwW.gif","https://cdn.weeb.sh/images/HkK2mkYPZ.gif","https://cdn.weeb.sh/images/SJ-CQytvW.gif","https://cdn.weeb.sh/images/BJLCX1Kw-.gif","https://cdn.weeb.sh/images/ry2tWxcyf.gif","https://cdn.weeb.sh/images/HyPjmytDW.gif","https://cdn.weeb.sh/images/HJKiX1tPW.gif","https://cdn.weeb.sh/images/HJfXM0KYZ.gif","https://cdn.weeb.sh/images/BJSpWec1M.gif","https://cdn.weeb.sh/images/HyV5mJtDb.gif","https://media.giphy.com/media/t1CsJ1o1sdOHm/giphy.gif","https://media.giphy.com/media/3eKfsCZKKb3c4/giphy.gif","https://m.popkey.co/d5f999/4Vv51_s-200x150.gif","https://m.popkey.co/1121ac/16jO8_s-200x150.gif","http://www.teampwnicorn.com/wp-content/uploads/2013/03/Joffrey-gets-slapped-5.gif"]
    p=link[random.randint(0,len(link)-1)]      
    if user!=None:
            embed=discord.Embed(description="{} slapped {}... Must have been a real baka :wave:".format(ctx.message.author.name,user.name),color=0xf7d28c)
    else:
            embed=discord.Embed(description="Hmm {} is slapping themselves, what? :wave:".format(ctx.message.author.name),color=0xf7d28c)
    embed.set_image(url=p)
    await bot.say(embed=embed)

#blob commands
@bot.group(pass_context=True)
async def blob(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say("Invalid blob command passed...")
@blob.command(pass_context=True)
async def blush(ctx):
    await bot.say("<a:blush:436934532587847681>")
    await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def weary(ctx):
    await bot.say("<a:weary:436934578415075331>")
    await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def sleepy(ctx):
    await bot.say("<a:sleepy:436934625164656659>")
    await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def sad(ctx):
    await bot.say("<a:sad:436934649563054090>")
    await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def cool(ctx):
    await bot.say("<a:cool:436934671117582356>")
    await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def wink(ctx):
    await bot.say("<a:wink:436934691141058561>")
    await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def winkf(ctx):
    await bot.say("<a:winkf:436934713077268480>")
    await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def teeth(ctx):
    await bot.say("<a:teeth:436934738771574797>")
    await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def notlike(ctx):
    await bot.say("<a:not_like:436934761962012702>")
    await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def kiss(ctx):
    await bot.say("<a:kiss:436934782803378187>")
    await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def grr(ctx):
    await bot.say("<a:grr:436934802331926529>")
    await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def sob(ctx):
    await bot.say("<a:sob:436934823492190210>")
    await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def toj(ctx):
    await bot.say("<a:tears_of_joy:436934851040378900>")
    await bot.delete_message(ctx.message)
@blob.command(pass_context=True)
async def sweat(ctx):
    await bot.say("<a:blobsweat:435149054528454670>")
    await bot.delete_message(ctx.message)

#Emoji commands
@bot.group(pass_context=True)
async def emoji(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say('Invalid emoji command passed...')
@emoji.command(pass_context=True)
async def shrug(ctx):
    await bot.say("¯\_(ツ)_/¯")
    await bot.delete_message(ctx.message)
@emoji.command(pass_context=True)
async def mikuyay(ctx):
    await bot.say("<a:mikuyay:434019400073347072>")
    await bot.delete_message(ctx.message)
@emoji.command(pass_context=True)
async def sip(ctx):
    await bot.say("<a:sip:434254079246467075>")
    await bot.delete_message(ctx.message)
@emoji.command(pass_context=True)
async def j(ctx):
    await bot.say("<a:j_:434254490745569282>")
    await bot.delete_message(ctx.message)
@emoji.command(pass_context=True)
async def dance(ctx):
    await bot.say("<a:dance:434236128904609796>")
    await bot.delete_message(ctx.message)
@emoji.command(pass_context=True)
async def peek(ctx):
    await bot.say("<a:peeking:435149270518333460>")
    await bot.delete_message(ctx.message)
@emoji.command(pass_context=True)
async def bang(ctx):
    await bot.say("<a:bang:435149143577460752>")
    await bot.delete_message(ctx.message)
@emoji.command(pass_context=True)
async def wonder(ctx):
    await bot.say("<a:wonder:435147959101947905>")
    await bot.delete_message(ctx.message)
    
bot.run("NDExNTY2NDczMzUwMjE3NzQ4.DWRS8A.U2VKbHmJAbktNhhgOhSNcpgwGt4")