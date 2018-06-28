import asyncio
import discord
from discord.ext import commands
from discord import opus

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass

    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))


def __init__(self, bot):
        self.bot = bot

class VoiceEntry:
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

class VoiceState:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.play_next_song = asyncio.Event()
        self.songs = asyncio.Queue()
        self.skip_votes = set() # a set of user_ids that voted
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

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
            await self.bot.send_message(self.current.channel, 'Now playing' + str(self.current))
            self.current.player.start()
            await self.play_next_song.wait()
class Music:
    """Voice related commands.
    Works in multiple servers at once.
    """
    def __init__(self, bot):
        self.bot = bot
        self.voice_states = {}

    def get_voice_state(self, server):
        state = self.voice_states.get(server.id)
        if state is None:
            state = VoiceState(self.bot)
            self.voice_states[server.id] = state

        return state

    async def create_voice_client(self, channel):
        voice = await self.bot.join_voice_channel(channel)
        state = self.get_voice_state(channel.server)
        state.voice = voice

    def __unload(self):
        for state in self.voice_states.values():
            try:
                state.audio_player.cancel()
                if state.voice:
                    self.bot.loop.create_task(state.voice.disconnect())
            except:
                pass

    @commands.command(pass_context=True, no_pm=True)
    async def join(self, ctx, *, channel : discord.Channel):
        """Joins a voice channel."""
        try:
            await self.create_voice_client(channel)
        except discord.ClientException:
            embed=discord.Embed(description='Already in a voice channel...',color=0xf7d28c)
            await self.bot.say(embed=embed)
        except discord.InvalidArgument:
            embed=discord.Embed(description='This is not a voice channel...',color=0xf7d28c)
            await self.bot.say(embed=embed)
        else:
            embed=discord.Embed(description='Ready to play audio in **',color=0xf7d28c)
            await self.bot.say(emed=embed + channel.name)

    @commands.command(pass_context=True, no_pm=True)
    async def summon(self, ctx):
        """Summons the bot to join your voice channel."""
        summoned_channel = ctx.message.author.voice_channel
        if summoned_channel is None:
            embed=discord.Embed(description="Are you sure you are in a voice chaneel? :thinking:",color=0xf7d28c)
            await self.bot.say(embed=embed)
            return False

        state = self.get_voice_state(ctx.message.server)
        if state.voice is None:
            state.voice = await self.bot.join_voice_channel(summoned_channel)
        else:
            await state.voice.move_to(summoned_channel)

        return True

    @commands.command(pass_context=True, no_pm=True)
    async def play(self, ctx, *, song : str):
        """Plays a song.
        If there is a song currently in the queue, then it is
        queued until the next song is done playing.
        This command automatically searches as well from YouTube.
        The list of supported sites can be found here:
        https://rg3.github.io/youtube-dl/supportedsites.html
        """
        state = self.get_voice_state(ctx.message.server)
        opts = {
            'default_search': 'auto',
            'quiet': True,
        }

        if state.voice is None:
            success = await ctx.invoke(self.summon)
            embed=discord.Embed(description="Loading the song,please be patient...",color=0xf7d28c)
            await self.bot.say(embed=embed)
            if not success:
                return

        try:
            player = await state.voice.create_ytdl_player(song, ytdl_options=opts, after=state.toggle_next)
        except Exception as e:
            fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.send_message(ctx.message.channel, fmt.format(type(e).__name__, e))
        else:
            player.volume = 0.6
            entry = VoiceEntry(ctx.message, player)
            embed=discord.Embed(description='Enqueued ' + str(entry),color=0xf7d28c)
            await self.bot.say(embed=embed)
            await state.songs.put(entry)

    @commands.command(pass_context=True, no_pm=True)
    async def volume(self, ctx, value : int):
        """Sets the volume of the currently playing song."""

        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.volume = value / 100
            embed=discord.Embed(description='Set the volume to {:.0%}'.format(player.volume),color=0xf7d28c)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def resume(self, ctx):
        """Resumes the currently played song."""
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.resume()

    @commands.command(pass_context=True, no_pm=True)
    async def pause(self, ctx):
        """Pauses the currently played song."""
        state = self.get_voice_state(ctx.message.server)
        if state.is_playing():
            player = state.player
            player.pause()


    @commands.command(pass_context=True, no_pm=True)
    async def leave(self, ctx):
        """Stops playing audio and leaves the voice channel.
        This also clears the queue.
        """
        server = ctx.message.server
        state = self.get_voice_state(server)

        if state.is_playing():
            player = state.player
            player.stop()

        try:
            state.audio_player.cancel()
            del self.voice_states[server.id]
            await state.voice.disconnect()
            embed=discord.Embed(description="Cleared the queue and disconnected from voice channel ",color=0xf7d28c)
            await self.bot.say(embed=embed)
        except:
            pass


    @commands.command(pass_context=True, no_pm=True)
    async def repeat(self, ctx):
        """Repeats the currently playing song"""
        state = self.get_voice_state(ctx.message.server)
        voter = ctx.message.author
        if voter == state.current.requester:
            embed=discord.Embed(description='Repeating the song...',color=0xf7d28c)
            await self.bot.say(embed=embed)
            state.repeat()


    @commands.command(pass_context=True, no_pm=True)
    async def skip(self, ctx):
        """Vote to skip a song. The song requester can automatically skip.
        3 skip votes are needed for the song to be skipped.
        """

        state = self.get_voice_state(ctx.message.server)
        if not state.is_playing():
            embed=discord.Embed(description='Not playing any music right now...',color=0xf7d28c)
            await self.bot.say(embed=embed)
            return

        voter = ctx.message.author
        if voter == state.current.requester:
            embed=discord.Embed(description='Requester requested skipping song...',color=0xf7d28c)
            await self.bot.say(embed=embed)
            state.skip()
        elif voter.id not in state.skip_votes:
            state.skip_votes.add(voter.id)
            total_votes = len(state.skip_votes)
            if total_votes >= 3:
                embed=discord.Embed(description='Skip vote passed, skipping song...',color=0xf7d28c)
                await self.bot.say(embed=embed)
                state.skip()
            else:
                embed=discord.Embed(description='Skip vote added, currently at [{}/3]'.format(total_votes),color=0xf7d28c)
                await self.bot.say(embed=embed)
        else:
            embed=discord.Embed(description='You have already voted to skip this song.',color=0xf7d28c)
            await self.bot.say(embed=embed)

    @commands.command(pass_context=True, no_pm=True)
    async def playing(self, ctx):
        """Shows info about the currently played song."""
        state = self.get_voice_state(ctx.message.server)
        if state.current is None:

            embed=discord.Embed(description="Not playing anything",color=0xf7d28c)
            await self.bot.say(embed=embed)

        else:
             skip_count = len(state.skip_votes)
             embed=discord.Embed(description="Now playing {} [skips: {}/3]".format(state.current,skip_count),color=0xf7d28c)
             await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(Music(bot))
    print('Music is loaded')
