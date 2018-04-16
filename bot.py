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
#for quotes
with codecs.open("quotes.json", "r",encoding='utf-8', errors='ignore') as f:
    quotes= json.load(f)

bot = commands.Bot(command_prefix='-')
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

# @bot.event
# async def on_message(message):
#     if message.content == ":FeelsMagik:":
#         await bot.delete_message(message)

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
    if ctx.message.author.id=="343395225571426304" or "402829897514352641":
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

@bot.command(pass_context=True)
async def pfp(ctx,user:discord.Member=None):
    if user is None:
        user = ctx.message.author
    embed=discord.Embed(title="{}'s avatar".format(user.name),color=0xf7d28c)
    embed.set_image(url=user.avatar_url)
    await bot.say(embed=embed)
    print("Avatar")

@bot.command(pass_context=True)
async def ask(ctx):
    choice=["It is certain :8ball:","It is decidedly so :8ball:","Without a doubt :8ball:","Yes, definitely :8ball:","You may rely on it :8ball:","As I see it, yes :8ball:","Most likely :8ball:","Outlook good :8ball:","Yes :8ball:","Signs point to yes :8ball:","Reply hazy try again :8ball:","Ask again later :8ball:","Better not tell you now :8ball:","Cannot predict now :8ball:","Concentrate and ask again :8ball:","Don't count on it :8ball:","My reply is no :8ball:","My sources say no :8ball:","Outlook not so good :8ball:","Very doubtful :8ball:"]
    ch=random.randint(1,20)
    await bot.say(choice[ch])
    print("ask")

bot.remove_command("help")
@bot.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(title="Help",description="Gives you a list of command that bot curently has:",color=0xf7d28c,inline=False)
    embed.add_field(name="ping", value="Basic Ping Command",inline=False)
    embed.add_field(name="info [@User]", value="Gives you the basic information about selected user",inline=False)
    embed.add_field(name="svrinfo", value="Gives you the information of the server where the command is being used",inline=False)
    embed.add_field(name="pfp [@User]",value="Shows you the photo of required user",inline=False)
    embed.add_field(name="quote",value="Displays a random quote",inline=False)
    embed.add_field(name="invite",value="Generates invite link to add Asuna to your guild",inline=False)
    embed.add_field(name="ask <A yes/no question>",value="Gives answer to your query :stuck_out_tongue_winking_eye: ",inline=False)
    embed.add_field(name="ud <query>",value="Searches the meaning of given query in Urban Dictionary",inline=False)  
    embed.add_field(name="define <query>",value="Searches the meaning of given query in Dictionary",inline=False)
    embed.add_field(name="google <query>",value="Searches Google for your query",inline =False)
    embed.add_field(name="wiki <query>",value="Searches Wikipedia for your query",inline =False)
    embed.add_field(name="yt <query>",value="Searches YouTube for your query",inline=False)                    
    embed.add_field(name="emo <word>",value="Emojify your text :wink:",inline=False)     
    embed.add_field(name="norris [@mention]",value="Displays a random norris facts",inline=False)
    embed.add_field(name="xkcd [number]",value="Displays given comic else random comic",inline=False)  
    embed.add_field(name="weather <location>",value="Gives weather info for given location",inline=False)
    embed.add_field(name="pokemon <name>",value="Gives info about required pokemon",inline=False)     
    embed.add_field(name="sebi",value="Displays a random meme from SebiSauce collection :laughing:",inline=False)
    embed.add_field(name="shrug",value="Appends a shrug in the chat",inline=False)
    embed.set_footer(text="Arguments in [] are optional but arguments in <> are necessary for given function to work")       
    await bot.whisper(embed=embed)
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
    embed.add_field(name="Prefix",value="-")
    embed.add_field(name="Link",value="https://discordapp.com/api/oauth2/authorize?client_id=411566473350217748&permissions=8&scope=bot")
    embed.set_footer(text="Feel free to uncheck some permissions")
    embed.set_thumbnail(url=Asuna.avatar_url)
    await bot.say(embed=embed)
    print("invite")

@bot.command()
async def ud(query=None):
    if query!=None:
        defs = udd.define(query)
        for d in range(1):
            definition=defs[d].definition
            word=defs[d].word
            example=defs[d].example
            upvotes=defs[d].upvotes
            downvotes=defs[d].downvotes
        embed = discord.Embed(title=word, description="Here's what I could find.", color=0xf7d28c)
        embed.add_field(name="Defintion", value=definition, inline=False)
        embed.add_field(name="Example",value=example,inline=False)
        embed.add_field(name="Upvotes",value=str(upvotes)+":thumbsup:",inline=True)
        embed.add_field(name="Downvotes",value=str(downvotes)+":thumbsdown:",inline=True)
        await bot.say(embed=embed)
        print("ud")

@bot.command(pass_context = True)
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

@bot.command(pass_context=True)
async def google(ctx,*,query=None):
       if query!=None:
           list1=[]
           for url in search(query, stop=1):
                list1.append(url)
           await bot.say(list1[0])
       print("google")

@bot.command(pass_context=True)
async def wiki(ctx,*,query=None):
    if query!=None:
        list1=[]
        query+="wikipedia"
        for url in search(query, stop=1):
                list1.append(url)
        await bot.say(list1[0])
    print("wikipedia")


@bot.command(pass_context=True)
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

@bot.command(pass_context=True)
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
async def weather(*,location):
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

@bot.command()
async def pokemon(pokemon):
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
    print("pokemon")

@bot.command()
async def define(*,word=None):
    if word!=None:
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

@bot.command()
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

@bot.command()
async def sebi():
    response=urllib.request.urlopen("https://sebisauce.herokuapp.com/api/random").read()
    response=json.loads(response.decode("utf-8"))
    url=response["file"]
    embed=discord.Embed(title="SebiSauce",color=0xf7d28c)
    embed.set_image(url=url)
    await bot.say(embed=embed)
    print("sebi")

@bot.command(pass_context=True)
async def shrug(ctx):
    await bot.say("¯\_(ツ)_/¯")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def mikuyay(ctx):
    await bot.say("<a:mikuyay:434019400073347072>")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def sip(ctx):
    await bot.say("<a:sip:434254079246467075>")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def j(ctx):
    await bot.say("<a:j_:434254490745569282>")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def blush(ctx):
    await bot.say("<a:BLUSH:435062664884912128>")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def dance(ctx):
    await bot.say("<a:dance:434236128904609796>")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def peek(ctx):
    await bot.say("<a:peeking:435149270518333460>")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def bang(ctx):
    await bot.say("<a:bang:435149143577460752>")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def sweat(ctx):
    await bot.say("<a:blobsweat:435149054528454670>")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def wonder(ctx):
    await bot.say("<a:wonder:435147959101947905>")
    await bot.delete_message(ctx.message)
    
bot.run("NDExNTY2NDczMzUwMjE3NzQ4.DWRS8A.U2VKbHmJAbktNhhgOhSNcpgwGt4")