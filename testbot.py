import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import random

#for loading music.py
startup_extensions = ["Music"]

bot = commands.Bot("-")

@bot.event
async def on_ready():
    print("ready")

#for music command class
class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("pong")





        #for Music extension
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exe = '{}: {}'.format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(extension, exe))


bot.run("NDExNTY2NDczMzUwMjE3NzQ4.DWRS8A.U2VKbHmJAbktNhhgOhSNcpgwGt4")
