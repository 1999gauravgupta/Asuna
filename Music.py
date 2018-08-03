import asyncio
import discord
from discord.ext import commands
from discord import opus
import random


opus_libs = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


if opus.is_loaded():
    pass
for opus_lib in opus_libs:
    try:
        opus.load_opus(opus_lib)
    except OSError as e:
        print(e)

# or libopus.so on linux in the current directory
def __init__(self, bot):  # you should replace this with the location the
    self.bot = bot  # opus library is located in and with the proper filename.


# note that on windows this DLL is automatically provided for you
class VoiceEntry():
    def __init__(self, message, player):
        self.requester = message.author
        self.channel = message.channel
        self.player = player

    def __str__(self):
        fmt = ' {0.title} uploaded by {0.uploader} and requested by {1.display_name}'
        duration = self.player.duration
        if duration:
            fmt = fmt + ' [length: {0[0]}m {0[1]}s]'.format(divmod(duration, 60))
        return fmt.format(self.player, self.requester)


class VoiceState():
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.skip_votes = set()
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):  # a set of user_ids that voted
        if (self.voice is None) or (self.current is None):
            return False
        player = self.current.player
        return (not player.is_done())

    @property
    def player(self):
        return self.current.player

    def skip(self):
        self.skip_votes.clear()
        if self.is_playing():
            self.player.stop()

    def repeat(self):
        if self.is_playing():
            self.player.repeat()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.songs.get()
            await self.current.channel.send('Now playing' + str(self.current))
            self.current.player.start()
            await self.play_next_song.wait()


class Music():
    'Voice related commands.\n    Works in multiple servers at once.\n    '

    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, guild):
        state = self.voice_states.get(guild.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[guild.id] = state
        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.guild)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(no_pm=True)
    async def join(self, ctx, *, channel: discord.Channel):
        'Joins a voice channel.'
        try:
            await self.create_voice_client(channel)
        except discord.ClientException:
            embed = discord.Embed(description='Already in a voice channel...', color=16241292)
            await ctx.send(embed=embed)
        except discord.InvalidArgument:
            embed = discord.Embed(description='This is not a voice channel...', color=16241292)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description='Ready to play audio in **', color=16241292)
            await ctx.send(emed=embed + channel.name)

    @commands.command(no_pm=True)
    async def summon(self, ctx):
        'Summons the bot to join your voice channel.'
        summoned_channel = ctx.author.voice_channel
        if summoned_channel is None:
            embed = discord.Embed(description='Are you sure you are in a voice chaneel? :thinking:', color=16241292)
            await ctx.send(embed=embed)
            return False
        state = self.get_voice_state(ctx.guild)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(summoned_channel)
        else:
            await state.voice.move_to(summoned_channel)
        return True

    @commands.command(no_pm=True)
    async def play(self, ctx, *, song: str):
        'Plays a song.\n        If there is a song currently in the queue, then it is\n        queued until the next song is done playing.\n        This command automatically searches as well from YouTube.\n        The list of supported sites can be found here:\n        https://rg3.github.io/youtube-dl/supportedsites.html\n        '
        state = self.get_voice_state(ctx.guild)
        opts = {
            'default_search': 'auto',
            'quiet': True,
        }
        if state.voice is None:
            success = await ctx.invoke(self.summon)
            embed = discord.Embed(description='Loading the song,please be patient...', color=16241292)
            await ctx.send(embed=embed)
            if (not success):
                return
        try:
            player = await state.voice.create_ytdl_player(song, ytdl_options=opts, after=state.toggle_next)
        except Exception as e:
            fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
            await ctx.channel.send(fmt.format(type(e).__name__, e))
        else:
            player.volume = 0.6
            entry = VoiceEntry(ctx.message, player)
            embed = discord.Embed(description='Enqueued ' + str(entry), color=16241292)
            await ctx.send(embed=embed)
            await state.songs.put(entry)

    @commands.command(no_pm=True)
    async def volume(self, ctx, value: int):
        'Sets the volume of the currently playing song.'
        state = self.get_voice_state(ctx.guild)
        if state.is_playing():
            player = state.player
            player.volume = value / 100
            embed = discord.Embed(description='Set the volume to {:.0%}'.format(player.volume), color=16241292)
            await ctx.send(embed=embed)

    @commands.command(no_pm=True)
    async def resume(self, ctx):
        'Resumes the currently played song.'
        state = self.get_voice_state(ctx.guild)
        if state.is_playing():
            player = state.player
            player.resume()

    @commands.command(no_pm=True)
    async def pause(self, ctx):
        'Pauses the currently played song.'
        state = self.get_voice_state(ctx.guild)
        if state.is_playing():
            player = state.player
            player.pause()

    @commands.command(no_pm=True)
    async def leave(self, ctx):
        'Stops playing audio and leaves the voice channel.\n        This also clears the queue.\n        '
        guild = ctx.guild
        state = self.get_voice_state(guild)
        if state.is_playing():
            player = state.player
            player.stop()
        try:
            state.audio_player.cancel()
            del self.voice_states[guild.id]
            await state.voice.disconnect()
            embed = discord.Embed(description='Cleared the queue and disconnected from voice channel ', color=16241292)
            await ctx.send(embed=embed)
        except:
            pass

    @commands.command(no_pm=True)
    async def repeat(self, ctx):
        'Repeats the currently playing song'
        state = self.get_voice_state(ctx.guild)
        voter = ctx.author
        if voter == state.current.requester:
            embed = discord.Embed(description='Repeating the song...', color=16241292)
            await ctx.send(embed=embed)
            state.repeat()

    @commands.command(no_pm=True)
    async def skip(self, ctx):
        'Vote to skip a song. The song requester can automatically skip.\n        3 skip votes are needed for the song to be skipped.\n        '
        state = self.get_voice_state(ctx.guild)
        if (not state.is_playing()):
            embed = discord.Embed(description='Not playing any music right now...', color=16241292)
            await ctx.send(embed=embed)
            return
        voter = ctx.author
        if voter == state.current.requester:
            embed = discord.Embed(description='Requester requested skipping song...', color=16241292)
            await ctx.send(embed=embed)
            state.skip()
        elif voter.id not in state.skip_votes:
            state.skip_votes.add(voter.id)
            total_votes = len(state.skip_votes)
            if total_votes >= 3:
                embed = discord.Embed(description='Skip vote passed, skipping song...', color=16241292)
                await ctx.send(embed=embed)
                state.skip()
            else:
                embed = discord.Embed(
                    description='Skip vote added, currently at [{}/3]'.format(total_votes), color=16241292)
                await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description='You have already voted to skip this song.', color=16241292)
            await ctx.send(embed=embed)

    @commands.command(no_pm=True)
    async def playing(self, ctx):
        'Shows info about the currently played song.'
        state = self.get_voice_state(ctx.guild)
        if state.current is None:
            embed = discord.Embed(description='Not playing anything', color=16241292)
            await ctx.send(embed=embed)
        else:
            skip_count = len(state.skip_votes)
            embed = discord.Embed(
                description='Now playing {} [skips: {}/3]'.format(state.current, skip_count), color=16241292)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Music(bot))
    print('Music is loaded')