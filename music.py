from discord.ext import commands
import asyncio
import discord
import youtube_dl

players={}

class MUSIC():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def join(self,ctx):
        channel=ctx.message.author.voice.voice_channel
        await client.join_voice_channel(channel)

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
    bot.add_cog(Music(bot))
    print('Music is loaded')