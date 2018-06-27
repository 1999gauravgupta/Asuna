from discord.ext import commands
import asyncio
import discord

class EMOJI:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def big(self,emo):
        """Enlarge emoji"""
        emo = emo.split(':')[-1].replace('>' , '')
        await self.bot.say("https://discordapp.com/api/emojis/{}.png".format(emo))

    #blob commands
    @commands.group(pass_context=True)
    async def blob(self,ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say("Invalid blob command passed...")
    @blob.command(pass_context=True)
    async def blush(self,ctx):
        await self.bot.say("<a:blush:436934532587847681>")
        await self.bot.delete_message(ctx.message) 
    @blob.command(pass_context=True)
    async def weary(self,ctx):
        await self.bot.say("<a:weary:436934578415075331>")
        await self.bot.delete_message(ctx.message) 
    @blob.command(pass_context=True)
    async def sleepy(self,ctx):
        await self.bot.say("<a:sleepy:436934625164656659>")
        await self.bot.delete_message(ctx.message) 
    @blob.command(pass_context=True)
    async def sad(self,ctx):
        await self.bot.say("<a:sad:436934649563054090>")
        await self.bot.delete_message(ctx.message) 
    @blob.command(pass_context=True)
    async def cool(self,ctx):
        await self.bot.say("<a:cool:436934671117582356>")
        await self.bot.delete_message(ctx.message) 
    @blob.command(pass_context=True)
    async def wink(self,ctx):
        await self.bot.say("<a:wink:436934691141058561>")
        await self.bot.delete_message(ctx.message) 
    @blob.command(pass_context=True)
    async def winkf(self,ctx):
        await self.bot.say("<a:winkf:436934713077268480>")
        await self.bot.delete_message(ctx.message) 
    @blob.command(pass_context=True)
    async def teeth(self,ctx):
        await self.bot.say("<a:teeth:436934738771574797>")
        await self.bot.delete_message(ctx.message) 
    @blob.command(pass_context=True)
    async def unamused(self,ctx):
        await self.bot.say("<a:not_like:436934761962012702>")
        await self.bot.delete_message(ctx.message) 
    @blob.command(pass_context=True)        
    async def owo(self,ctx):
        await self.bot.say("<a:OwO:458251627443519488>")
        await self.bot.delete_message(ctx.message) 
    @blob.command(pass_context=True)
    async def kiss(self,ctx):
        await self.bot.say("<a:kiss:436934782803378187>")
        await self.bot.delete_message(ctx.message) 
    @blob.command(pass_context=True)
    async def grr(self,ctx):
        await self.bot.say("<a:grr:436934802331926529>")
        await self.bot.delete_message(ctx.message) 
    @blob.command(pass_context=True)
    async def sob(self,ctx):
        await self.bot.say("<a:sob:436934823492190210>")
        await self.bot.delete_message(ctx.message) 
    @blob.command(pass_context=True)
    async def toj(self,ctx):
        await self.bot.say("<a:tears_of_joy:436934851040378900>")
        await self.bot.delete_message(ctx.message) 
    @blob.command(pass_context=True)
    async def sweat(self,ctx):
        await self.bot.say("<a:blobsweat:435149054528454670>")
        await self.bot.delete_message(ctx.message) 

    #Emoji commands
    @commands.group(pass_context=True)
    async def emoji(self,ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid emoji command passed...')
    @emoji.command(pass_context=True)
    async def shrug(self,ctx):
        await self.bot.say("¯\_(ツ)_/¯")
        await self.bot.delete_message(ctx.message) 
    @emoji.command(pass_context=True)
    async def mikuyay(self,ctx):
        await self.bot.say("<a:mikuyay:434019400073347072>")
        await self.bot.delete_message(ctx.message) 
    @emoji.command(pass_context=True)
    async def sip(self,ctx):
        await self.bot.say("<a:sip:434254079246467075>")
        await self.bot.delete_message(ctx.message) 
    @emoji.command(pass_context=True)
    async def j(self,ctx):
        await self.bot.say("<a:j_:434254490745569282>")
        await self.bot.delete_message(ctx.message) 
    @emoji.command(pass_context=True)
    async def dance(self,ctx):
        await self.bot.say("<a:dance:434236128904609796>")
        await self.bot.delete_message(ctx.message) 
    @emoji.command(pass_context=True)
    async def peek(self,ctx):
        await self.bot.say("<a:peeking:435149270518333460>")
        await self.bot.delete_message(ctx.message) 
    @emoji.command(pass_context=True)
    async def bang(self,ctx):
        await self.bot.say("<a:bang:435149143577460752>")
        await self.bot.delete_message(ctx.message) 
    @emoji.command(pass_context=True)
    async def wonder(self,ctx):
        await self.bot.say("<a:wonder:435147959101947905>")
        await self.bot.delete_message(ctx.message) 
    @emoji.command(pass_context=True)
    async def nom(self,ctx):
        await self.bot.say("<a:nom:456715700845674509>")
        await self.bot.delete_message(ctx.message)      

def setup(bot):
    bot.add_cog(EMOJI(bot))
    print("Emoji is loaded")