import discord
import codecs
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import string

startup_extensions = ['music', 'gifs', 'executer', 'emoji', 'bdcommands', 'games', 'query', 'fun']
owner = [343395225571426304, 402829897514352641]  
bot = commands.Bot(command_prefix=commands.when_mentioned_or('-', 'asuna ', 'Asuna ', 'Asuna, ', 'asuna, '))
client = discord.Client()

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

if __name__ == '__main__':
    for extension in startup_extensions: 
        try:
            bot.load_extension(extension)
        except Exception as e:
            exe = '{}: {}'.format(type(e).__name__, e)  
            print('Failed to load extension {}\n{}'.format(extension, exe))


@bot.event
async def on_ready():
    print('ready')
    print('I am running on ' + bot.user.name)
    print('With the ID: ' + bot.user.id)


#COMMANDS
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Listening to -help'))
    print('status changing done')


@bot.event
async def on_message(message):
    Words = [
        'dick', 'pussy', 'motherfucker', 'whore', 'asshole', 'son of a bitch', 'dickhead', 'bitch', 'dick head', 'cunt',
        'faggot', 'fag', 'nigga', 'nigger', 'slut'
    ]
    with open('serverf.txt', 'r') as f1:
        list1 = f1.readlines()
        for i in list1:
            j = i.replace('\n', '')
            if j == message.guild.id:
                if message.author.bot == False:
                    if message.author.id in owner:
                        pass
                    else:
                        try:
                            for i in Words:
                                if i in message.content.lower():
                                    await message.channel.send(
                                        '|:x:| Pardon, dear {}, you said something that is not allowed in this server'.
                                        format(message.author))
                                    await message.delete()
                        except Exception as e:
                            print(e)
    if message.author.bot == True:
        return
    await bot.process_commands(message)


@bot.command()
async def filter(ctx, state=1):
    if ctx.author.guild_permissions.administrator:
        if state == 1:
            with open('serverf.txt', 'a') as f1:
                f1.write('\n' + ctx.guild.id)
            await ctx.send('Filter turned on successfully.')
        else:
            f = open('serverf.txt', 'r')
            lines = f.readlines()
            f.close()
            f = open('serverf.txt', 'w')
            for line in lines:
                p = line.replace('\n', '')
                if p != ctx.guild.id:
                    f.write(line)
            f.close()
            await ctx.send('Filter turned off successfully.')
    else:
        await ctx.send("You do not have required permissions.")

bot.remove_command('help')

@bot.command()
async def help(ctx):
    help1 = '\n:page_with_curl: | Help Message\n**General User/Server/Bot Info Commands:**\n• -info [@user]→ Provides some information about the user who invoked the command or of mentioned user.\n• -svrinfo → Provides some information about the server in which the command is invoked.\n• -pfp [@user] → Display avatar of yours or mentioned user.\n• -perms [@user] → Display user perms in that server.\n• -filter [state] → Use this command to setup filter on your server. Set it off using -filter 0.\n• -invite → Add Asuna to your guild.\n• -ping → Runs a connection test to Discord.\n• -help → Display this message.\n**General Query Commands:**\n• -google <query> → Searches Google for your query.\n• -wiki <query> → Searches Wikipedia for your query.\n• -yt <query> → Searches YouTube for your query.\n• -weather <location> → Displays weather of given location.\n• -pokemon <query> → Gives some data about queried pokemon.\n• -ud <word> → Searches Urban Dictionary for your word.\n• -define <word> → Searches Dictionary for your word.\n• -anime <query> → Searches for given anime details.\n• -manga <query> → Searches for given manga details.\n• -translate <query> → Translates your input text.'
    help2 = "\n**General Fun Commands:**\n• -quote → Display random motivational code to make your day.\n• -ask <question>→ Asuna helps you with your questions.\n• -emo <text>→ Emojifies the text.\n• -norris [@user] → Display random chuck norris joke.\n• -xkcd [number] → Searches xkcd for your comic else prints a random comic.\n• -sebi → Display a random SebiSauce.\n• -pat [@user]→ Pats somebody's head!.\n• -cuddle [@user]→Cuddle somebody with a picture!.\n• -slap [@user]→ Slap the baka.\n• -punch [@user]→ Give them what they deserve.\n• -hug [@user]→ Hug somebody with a picture!\n• -kiss [@user]→ Show some love.\n• -tickle [@user]→ Don't stop until they cry.\n• -sleepy [@user]→ Why not sleeping then?.\n• -cry [@user]→ Did someone hurt you?.\n• -nom [@user]→ Hungry? have something to eat.\n• -gaze [@user]→ Glare at someone.\n• -cry [@user]→ Aaawww,did someone make you feel flushed?.\n**General Emoji Commands:**\n• -emoji <shrug,sip,bang,wonder,yay,peek,dance,j,nom> → Appends that emoji in chat.\n• -blob <blush,weary,sleepy,sad,cool,wink,winkf,teeth,unamused,kiss,grr,sob,toj,owo> → Appends your favorite Google blob stickers in chat."
    help3 = '\n**General Music Commands:**\n• -join <query> → Make the bot join a voice channel.\n• -play <query> → Name of the song/url you want to play.\n• -playing → Shows info about the currently played songself.\n• -volume <value> → Sets the volume of the currently playing song.\n• -skip → Vote to skip a song. The song requester can automatically skip.\n3 skip votes are needed for the song to be skipped.\n• -pause → Pauses the currently played song.\n• -resume → Resume the currently played song.\n• -leave → Stops playing audio and leaves the voice channel.\nThis also clears the queue.\n*Music commands not working atm*\n**Arguments in [] are optional but arguments in <> are necessary for given function to work**\n'
    await ctx.author.send(help1)
    await ctx.author.send(help2)
    await ctx.author.send(help3)
    await ctx.send(':inbox_tray: | The list of commands you have access to has been sent to your DMs.')
    print('help')


bot.run('NDExNTY2NDczMzUwMjE3NzQ4.DWRS8A.U2VKbHmJAbktNhhgOhSNcpgwGt4')