import discord
import codecs
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import string

#for loading music.py
startup_extensions = ["Music","gifs","executer","emoji","bdcommands","games","query","fun"]

owner=["343395225571426304"]

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
    Words=["dick","pussy","motherfucker","whore", "asshole","son of a bitch","dickhead","bitch","dick head","cunt","faggot","fag","nigga","nigger","slut"]
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

bot.run("NDExNTY2NDczMzUwMjE3NzQ4.DWRS8A.U2VKbHmJAbktNhhgOhSNcpgwGt4")
