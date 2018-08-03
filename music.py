from discord.ext import commands
import asyncio
import discord
import youtube_dl
import os
import random

players={}
opus_libs = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


if opus.is_loaded():
    pass
for opus_lib in opus_libs:
    try:
        opus.load_opus(opus_lib)
    except OSError as e:
        print(e)

class MUSIC():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def join(self,ctx):
        channel=ctx.message.author.voice.voice_channel
        await ctx.join_voice_channel(channel)

    @commands.command()
    async def leave(self,ctx):
        server=ctx.message.guild
        voice_client=ctx.voice_client_in(server)
        await voice_client.discnnect()

    @commands.command()
    async def play(self,ctx,url):
        server=ctx.message.guild
        voice_client=ctx.voice_client_in(server)
        player=await voice_client.create_ytdl_player(url)
        players[server.id]=player
        player.start()
         
def setup(bot):
    bot.add_cog(MUSIC(bot))
    print('Music is loaded')
