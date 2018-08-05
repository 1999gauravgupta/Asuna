import discord
import codecs
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import string
import random
from paginator import HelpPaginator, CannotPaginate

startup_extensions = ['gifs', 'executer', 'emoji', 'bdcommands', 'games', 'query', 'fun']
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
    if message.author.bot == True:
        return
    await bot.process_commands(message)

bot.remove_command('help')

@bot.command(pass_context=True)
async def _help(self, ctx, *, command: str = None):
        """Shows help about a command or the bot"""

        try:
            if command is None:
                p = await HelpPaginator.from_bot(ctx)
            else:
                entity = bot.get_cog(command) or bot.get_command(command)

                if entity is None:
                    clean = command.replace('@', '@\u200b')
                    return await ctx.send(f'Command or category "{clean}" not found.')
                elif isinstance(entity, commands.Command):
                    p = await HelpPaginator.from_command(ctx, entity)
                else:
                    p = await HelpPaginator.from_cog(ctx, entity)

            await p.paginate()
        except Exception as e:
            await ctx.send(e)



bot.run('NDExNTY2NDczMzUwMjE3NzQ4.DWRS8A.U2VKbHmJAbktNhhgOhSNcpgwGt4')