from discord.ext import commands
import asyncio
import discord
import random
import aiohttp

class EMOJI():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def big(self, ctx, emo):
        'Enlarge emoji'
        emo = emo.split(':')[(-1)].replace('>', '')
        await ctx.send('https://discordapp.com/api/emojis/{}.png'.format(emo))

#blob commands
    @commands.command()
    async def nitro(self, ctx, emo=None):
        await ctx.message.delete()
        if emo is None:
            await ctx.send("Duh! I need a emoji name to work")
            return
        emo = discord.utils.get(ctx.guild.emojis , name= emo)
        if emo is None:
            counter=1
            stri="This is the list of this server animated emojis. You can use anyone of them:\n"
            for i in ctx.guild.emojis:
                if i.animated==True:
                    stri+=str(counter)+". ``"+i.name+"`` \n"
                    counter+=1
            await ctx.author.send(stri)
        else:
            await ctx.send(e)

    # @commands.group()
    # async def blob(self, ctx):
    #     if ctx.invoked_subcommand is None:
    #         await ctx.send('Invalid blob command passed...')

    # @blob.command()
    # async def blush(self, ctx):
    #     await ctx.send('<a:blush:436934532587847681>')
    #     await ctx.message.delete()

    # @blob.command()
    # async def weary(self, ctx):
    #     await ctx.send('<a:weary:436934578415075331>')
    #     await ctx.message.delete()

    # @blob.command()
    # async def sleepy(self, ctx):
    #     await ctx.send('<a:sleepy:436934625164656659>')
    #     await ctx.message.delete()

    # @blob.command()
    # async def sad(self, ctx):
    #     await ctx.send('<a:sad:436934649563054090>')
    #     await ctx.message.delete()

    # @blob.command()
    # async def cool(self, ctx):
    #     await ctx.send('<a:cool:436934671117582356>')
    #     await ctx.message.delete()

    # @blob.command()
    # async def wink(self, ctx):
    #     await ctx.send('<a:wink:436934691141058561>')
    #     await ctx.message.delete()

    # @blob.command()
    # async def winkf(self, ctx):
    #     await ctx.send('<a:winkf:436934713077268480>')
    #     await ctx.message.delete()

    # @blob.command()
    # async def teeth(self, ctx):
    #     await ctx.send('<a:teeth:436934738771574797>')
    #     await ctx.message.delete()

    # @blob.command()
    # async def unamused(self, ctx):
    #     await ctx.send('<a:not_like:436934761962012702>')
    #     await ctx.message.delete()

    # @blob.command()
    # async def owo(self, ctx):
    #     await ctx.send('<a:OwO:458251627443519488>')
    #     await ctx.message.delete()

    # @blob.command()
    # async def kiss(self, ctx):
    #     await ctx.send('<a:kiss:436934782803378187>')
    #     await ctx.message.delete()

    # @blob.command()
    # async def grr(self, ctx):
    #     await ctx.send('<a:grr:436934802331926529>')
    #     await ctx.message.delete()

    # @blob.command()  #Emoji commands
    # async def sob(self, ctx):
    #     await ctx.send('<a:sob:436934823492190210>')
    #     await ctx.message.delete()

    # @blob.command()
    # async def toj(self, ctx):
    #     await ctx.send('<a:tears_of_joy:436934851040378900>')
    #     await ctx.message.delete()

    # @blob.command()
    # async def sweat(self, ctx):
    #     await ctx.send('<a:blobsweat:435149054528454670>')
    #     await ctx.message.delete()

    # @commands.group()
    # async def emoji(self, ctx):
    #     if ctx.invoked_subcommand is None:
    #         await ctx.send('Invalid emoji command passed...')

    # @emoji.command()
    # async def shrug(self, ctx):
    #     await ctx.send('¯\\_(ツ)_/¯')
    #     await ctx.message.delete()

    # @emoji.command()
    # async def mikuyay(self, ctx):
    #     await ctx.send('<a:mikuyay:434019400073347072>')
    #     await ctx.message.delete()

    # @emoji.command()
    # async def sip(self, ctx):
    #     await ctx.send('<a:sip:434254079246467075>')
    #     await ctx.message.delete()

    # @emoji.command()
    # async def j(self, ctx):
    #     await ctx.send('<a:j_:434254490745569282>')
    #     await ctx.message.delete()

    # @emoji.command()
    # async def dance(self, ctx):
    #     await ctx.send('<a:dance:434236128904609796>')
    #     await ctx.message.delete()

    # @emoji.command()
    # async def peek(self, ctx):
    #     await ctx.send('<a:peeking:435149270518333460>')
    #     await ctx.message.delete()

    # @emoji.command()
    # async def bang(self, ctx):
    #     await ctx.send('<a:bang:435149143577460752>')
    #     await ctx.message.delete()

    # @emoji.command()
    # async def wonder(self, ctx):
    #     await ctx.send('<a:wonder:435147959101947905>')
    #     await ctx.message.delete()

    # @emoji.command()
    # async def nom(self, ctx):
    #     await ctx.send('<a:nom:456715700845674509>')
    #     await ctx.message.delete()


def setup(bot):
    bot.add_cog(EMOJI(bot))
    print('Emoji is loaded')