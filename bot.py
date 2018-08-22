import discord
import codecs
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import string
import random

startup_extensions = ['gifs', 'executer', 'emoji', 'bdcommands', 'games', 'query', 'fun','reminder']
owner = [343395225571426304, 402829897514352641]  
bot = commands.Bot(command_prefix=commands.when_mentioned_or('-', 'asuna ', 'Asuna ', 'Asuna, ', 'asuna, '))
client = discord.Client()


class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

if __name__ == '__main__':
    for extension in startup_extensions: 
        try:
            bot.load_extension("cogs.{}".format(extension))
        except Exception as e:
            exe = '{}: {}'.format(type(e).__name__, e)  
            print('Failed to load extension {}\n{}'.format(extension, exe))

# async def purge_role(ctx, member, role):
#     try:
#         if role.name.lower() in ["lucky star","insane","chatterbox","water wave","unicorn","sparkling stars","cupcake","marshmallow","hello kitty","sparklers"]:
#             await member.remove_roles(role, reason='Cleaning up')
#             await ctx.send(f'\N{WHITE HEAVY CHECK MARK} Successfully removed {role} from {member}')
#     except Exception as ex:
#         await ctx.send(f'\N{CROSS MARK} Failed to remove {role} from {member} as {ex}')

@bot.event
async def on_ready():
    print('ready')
    print('I am running on ' + bot.user.name)
    print('With the ID: ' + bot.user.id)


#COMMANDS
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="-help"))
    print('status changing done')

@bot.event
async def on_message(message):
    if message.author.bot == True:
        return
    await bot.process_commands(message)

bot.remove_command('help')

@bot.event
async def on_command_error(ctx, err):
    if isinstance(err, commands.MissingPermissions):
        msg = await ctx.send('I am sorry {}, but it looks like... you dont have the required permissions !'.format(ctx.message.author.mention))
    # elif isinstance(err, commands.CommandInvokeError):
    #     print(err)
    #     msg = await ctx.send('I am sorry {}, but it looks like i dont have the required permissions !'.format(ctx.message.author.mention))
    elif isinstance(err, commands.MissingRequiredArgument):
        msg=await ctx.send('Umm you not gave proper information. Retry please !')
#     elif isinstance(err, commands.CommandNotFound):
#         await ctx.message.add_reaction('\N{CROSS MARK}')
#     else:
#         embed=discord.Embed(title=str(type(err))[8:-2],description=str(err),colour=discord.Colour.from_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
#         await ctx.send("Command raised an error",embed=embed,delete_after=15)

@bot.command(pass_context=True)
async def help(ctx):
    cogs=["BDCOMMANDS","QUERY","FUN","GAMES","GIFS"]
    """Shows help about a command or the bot"""
    help1 = '\n:page_with_curl: | Help Message\n**General User/Server/Bot Info Commands:**\n• -info [@user]→ Provides some information about the user who invoked the command or of mentioned user.\n• -svrinfo → Provides some information about the server in which the command is invoked.\n• -pfp [@user] → Display avatar of yours or mentioned user.\n• -perms [@user] → Display user perms in that server.\n• -invite → Add Asuna to your guild.\n• -ping → Runs a connection test to Discord.\n• -help → Display this message.\n**General Query Commands:**\n• -google <query> → Searches Google for your query.\n• -wiki <query> → Searches Wikipedia for your query.\n• -yt <query> → Searches YouTube for your query.\n• -weather <location> → Displays weather of given location.\n• -pokemon <query> → Gives some data about queried pokemon.\n• -ud <word> → Searches Urban Dictionary for your word.\n• -define <word> → Searches Dictionary for your word.\n• -anime <query> → Searches for given anime details.\n• -manga <query> → Searches for given manga details.\n• -translate <query> → Translates your input text.'
    help2 = "\n**General Fun Commands:**\n• -quote → Display random motivational code to make your day.\n• -ask <question>→ Asuna helps you with your questions.\n• -emo <text>→ Emojifies the text.\n• -norris [@user] → Display random chuck norris joke.\n• -xkcd [number] → Searches xkcd for your comic else prints a random comic.\n• -sebi → Display a random SebiSauce.\n• -pat [@user]→ Pats somebody's head!.\n• -cuddle [@user]→Cuddle somebody with a picture!.\n• -slap [@user]→ Slap the baka.\n• -punch [@user]→ Give them what they deserve.\n• -hug [@user]→ Hug somebody with a picture!\n• -kiss [@user]→ Show some love.\n• -tickle [@user]→ Don't stop until they cry.\n• -sleepy [@user]→ Why not sleeping then?.\n• -cry [@user]→ Did someone hurt you?.\n• -nom [@user]→ Hungry? have something to eat.\n• -gaze [@user]→ Glare at someone.\n• -blush [@user]→ Aaawww,did someone make you feel flushed?.\n**General Emoji Commands:**\n• -emoji <shrug,sip,bang,wonder,yay,peek,dance,j,nom> → Appends that emoji in chat.\n• -blob <blush,weary,sleepy,sad,cool,wink,winkf,teeth,unamused,kiss,grr,sob,toj,owo> → Appends your favorite Google blob stickers in chat."
    help3 = '\n**General Games Commands:**\n• -bj → Play classic old card game blackjack.\n• -ecard <emperor/slave> → Play the game ECard from anime Kaiji.\n**Arguments in [] are optional but arguments in <> are necessary for given function to work**\n'
    # list1=["yo","this is","test"]
    # await paginate(bot,ctx,cogs,"Help","Shows you the commands contained in a cog")
    # help3 = '\n**General Music Commands:**\n• -join <query> → Make the bot join a voice channel.\n• -play <query> → Name of the song/url you want to play.\n• -playing → Shows info about the currently played songself.\n• -volume <value> → Sets the volume of the currently playing song.\n• -skip → Vote to skip a song. The song requester can automatically skip.\n3 skip votes are needed for the song to be skipped.\n• -pause → Pauses the currently played song.\n• -resume → Resume the currently played song.\n• -leave → Stops playing audio and leaves the voice channel.\nThis also clears the queue.\n*Music commands not working atm*\n**Arguments in [] are optional but arguments in <> are necessary for given function to work**\n'
    await ctx.author.send(help1)
    await ctx.author.send(help2)
    await ctx.author.send(help3)
    await ctx.send(':inbox_tray: | The list of commands you have access to has been sent to your DMs.')
    print('help')

# @bot.command()
# async def purgeallroles(ctx):
#     futures = []
#     async with ctx.typing():
#         for member in ctx.guild.members:
#             for role in member.roles:
#                 futures.append(ctx.bot.loop.create_task(purge_role(ctx, member, role)))
#         await asyncio.gather(*futures)


bot.run('NDExNTY2NDczMzUwMjE3NzQ4.DWRS8A.U2VKbHmJAbktNhhgOhSNcpgwGt4')
