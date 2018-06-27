from discord.ext import commands
import asyncio
import discord
import random

class GIFS:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True,name="pat",aliases=["pats"])
    async def pat(self,ctx,*, user: discord.Member=None):
        try:
            link=["https://media1.tenor.com/images/1e92c03121c0bd6688d17eef8d275ea7/tenor.gif","https://thumbs.gfycat.com/FoolhardyJoyousBear-max-1mb.gif","https://media1.tenor.com/images/f79a9ec48bde0e592e55447b17ecfbad/tenor.gif","https://cdn.weeb.sh/images/Sk2FyQHpZ.gif","https://cdn.weeb.sh/images/B1PnJJYP-.gif","https://cdn.weeb.sh/images/Sky1x1YwW.gif","https://cdn.weeb.sh/images/SktIxo20b.gif","https://cdn.weeb.sh/images/Sk2f7J39G.gif","https://cdn.weeb.sh/images/B1TQcTNCZ.gif","https://cdn.weeb.sh/images/SJLaWWRSG.gif"]
            p=link[random.randint(0,len(link)-1)]
            if user!=None:
                embed=discord.Embed(description="{} gently pats {} <a:patgif:447681206155214859>".format(ctx.message.author.name,user.name),color=0xf7d28c)
            else:
                embed=discord.Embed(description="There there, i will pat you {} <a:patgif:447681206155214859>".format(ctx.message.author.name),color=0xf7d28c)
            embed.set_image(url=p)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True,name="cuddle",aliases=["cuddles"])
    async def cuddle(self,ctx,*, user: discord.Member=None):
        try:
            link= ["https://cdn.weeb.sh/images/BywGX8caZ.gif", "https://cdn.weeb.sh/images/BkTe8U7v-.gif", "https://cdn.weeb.sh/images/ryfyLL7D-.gif",  "https://cdn.weeb.sh/images/SJbGLUQwZ.gif","https://cdn.weeb.sh/images/SJLkLImPb.gif","https://cdn.weeb.sh/images/BJCCd_7Pb.gif","https://cdn.weeb.sh/images/B1SzeshCW.gif","https://cdn.weeb.sh/images/r1Q0HImPZ.gif","https://cdn.weeb.sh/images/r17lwymiZ.gif","https://cdn.weeb.sh/images/By03IkXsZ.gif","https://cdn.weeb.sh/images/S1T91Att-.gif","https://cdn.weeb.sh/images/r1s9RqB7G.gif","https://cdn.weeb.sh/images/SJceIU7wZ.gif","https://cdn.weeb.sh/images/Hyxo1CFtb.gif"]
            p=link[random.randint(0,len(link)-1)]
            if user!=None:
                    embed=discord.Embed(description="{} cuddles {} <a:cuddlegif:447689079979769856>".format(ctx.message.author.name,user.name),color=0xf7d28c)
            else:
                    embed=discord.Embed(description="Here {} have some cuddles <a:cuddlegif:447689079979769856>".format(ctx.message.author.name),color=0xf7d28c)
            embed.set_image(url=p)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(e)


    @commands.command(pass_context=True,name="hug",aliases=["hugs"])
    async def hug(self,ctx,*, user: discord.Member=None):
        try:
            link= ["https://cdn.weeb.sh/images/HyNJIaVCb.gif","https://cdn.weeb.sh/images/HkfgF_QvW.gif","https://cdn.weeb.sh/images/BkZngAYtb.gif","https://cdn.weeb.sh/images/SJebhd1Ob.gif","https://cdn.weeb.sh/images/BJF5_uXvZ.gif","https://cdn.weeb.sh/images/ryPix0Ft-.gif","https://cdn.weeb.sh/images/ByPGRkFVz.gif","https://cdn.weeb.sh/images/SyQ0_umD-.gif","https://cdn.weeb.sh/images/BkuUhO1OW.gif","https://cdn.weeb.sh/images/B10Tfknqf.gif","https://cdn.weeb.sh/images/SJZ-Qy35f.gif","https://cdn.weeb.sh/images/B11CDkhqM.gif","https://cdn.weeb.sh/images/HytoudXwW.gif","https://cdn.weeb.sh/images/Sk2gmRZZG.gif","https://cdn.weeb.sh/images/S14ju_7Pb.gif","https://cdn.weeb.sh/images/r1v2_uXP-.gif"]
            p=link[random.randint(0,len(link)-1)]
            if user!=None:
                    embed=discord.Embed(description="{} tightly hugs {} <:hug:436520609980219415>".format(ctx.message.author.name,user.name),color=0xf7d28c)
            else:
                    embed=discord.Embed(description="There you go {} hugs <:hug:436520609980219415>".format(ctx.message.author.name),color=0xf7d28c)
            embed.set_image(url=p)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True,name="slap",aliases=["slaps"])
    async def slap(self,ctx,*, user: discord.Member=None):
        try:
            link= ["https://cdn.weeb.sh/images/ByTR7kFwW.gif","https://cdn.weeb.sh/images/HkK2mkYPZ.gif","https://cdn.weeb.sh/images/SJ-CQytvW.gif","https://cdn.weeb.sh/images/BJLCX1Kw-.gif","https://cdn.weeb.sh/images/ry2tWxcyf.gif","https://cdn.weeb.sh/images/HyPjmytDW.gif","https://cdn.weeb.sh/images/HJKiX1tPW.gif","https://cdn.weeb.sh/images/HJfXM0KYZ.gif","https://cdn.weeb.sh/images/BJSpWec1M.gif","https://cdn.weeb.sh/images/HyV5mJtDb.gif","https://media.giphy.com/media/t1CsJ1o1sdOHm/giphy.gif","https://media.giphy.com/media/3eKfsCZKKb3c4/giphy.gif","https://m.popkey.co/d5f999/4Vv51_s-200x150.gif","https://m.popkey.co/1121ac/16jO8_s-200x150.gif","http://www.teampwnicorn.com/wp-content/uploads/2013/03/Joffrey-gets-slapped-5.gif"]
            p=link[random.randint(0,len(link)-1)]
            if user!=None:
                    embed=discord.Embed(description="{} slapped {}... Must have been a real baka :wave:".format(ctx.message.author.name,user.name),color=0xf7d28c)
            else:
                    embed=discord.Embed(description="Hmm {} is slapping themselves, what? :wave:".format(ctx.message.author.name),color=0xf7d28c)
            embed.set_image(url=p)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True,name="kiss",aliases=["kisses"])
    async def kiss(self,ctx,*, user: discord.Member=None):
        try:
            link=["https://cdn.weeb.sh/images/BydoCy9yG.gif","https://cdn.weeb.sh/images/BJSdQRtFZ.gif","https://cdn.weeb.sh/images/ryoW3T_vW.gif","https://cdn.weeb.sh/images/Sy6Ai6ODb.gif","https://cdn.weeb.sh/images/HklBtCvTZ.gif","https://cdn.weeb.sh/images/SkKL3adPb.gif","https://cdn.weeb.sh/images/SJ7b26_PW.gif","https://cdn.weeb.sh/images/HJ5khTOP-.gif","https://cdn.weeb.sh/images/Skc42pdv-.gif","https://cdn.weeb.sh/images/SJQRoTdDZ.gif","https://cdn.weeb.sh/images/BJv0o6uDZ.gif","https://cdn.weeb.sh/images/Sksk4l51z.gif","https://cdn.weeb.sh/images/Bkuk26uvb.gif","https://cdn.weeb.sh/images/r1cB3aOwW.gif","https://cdn.weeb.sh/images/ByTBhp_vZ.gif","https://cdn.weeb.sh/images/rJ_U2p_Pb.gif","https://cdn.weeb.sh/images/rJ6PWohA-.gif"]
            p=link[random.randint(0,len(link)-1)]
            if user!=None:
                    embed=discord.Embed(description="{} is kissing {}, they are so cute together <a:kissgif:447689034970562562>".format(ctx.message.author.name,user.name),color=0xf7d28c)
            else:
                    embed=discord.Embed(description="Kissing yourself {}? Sorry for that <a:kissgif:447689034970562562>".format(ctx.message.author.name),color=0xf7d28c)
            embed.set_image(url=p)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(e)

    commands.command(pass_context=True,name="tickle",aliases=["tickles"])
    async def tickle(self,ctx,*, user: discord.Member=None):
        try:
            link=["https://cdn.ram.moe/H1ChowIDx.gif","https://cdn.ram.moe/rJmioDLPl.gif","https://cdn.ram.moe/S1idjvIPx.gif","https://cdn.ram.moe/SJFisw8wx.gif","https://cdn.ram.moe/H1FqsDLPl.gif","https://cdn.ram.moe/rJQ2jvLDg.gif","https://cdn.weeb.sh/images/HyPyUymsb.gif","https://cdn.weeb.sh/images/HyjNLkXiZ.gif","https://cdn.weeb.sh/images/H1p0ByQo-.gif","https://cdn.weeb.sh/images/SyGQIk7i-.gif","https://cdn.weeb.sh/images/SyQHUy7oW.gif","https://cdn.weeb.sh/images/rkPzIyQi-.gif","https://cdn.weeb.sh/images/rybRByXjZ.gif"]
            p=link[random.randint(0,len(link)-1)]
            if user!=None:
                    embed=discord.Embed(description="{} is tickling {} <a:smile:447681122977972236>".format(ctx.message.author.name,user.name),color=0xf7d28c)
            else:
                    embed=discord.Embed(description="Tickles for you, {}! <a:smile:447681122977972236>".format(ctx.message.author.name),color=0xf7d28c)
            embed.set_image(url=p)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True,name="punch",aliases=["punches"])
    async def punch(self,ctx,*, user: discord.Member=None):
        try:
            link=["https://media1.tenor.com/images/6afcfbc435b698fa5ceb2ff019718e6d/tenor.gif","https://media1.tenor.com/images/c621075def6ca41785ef4aaea20cc3a2/tenor.gif","https://media1.tenor.com/images/6d77cf1fdaa2e7c6a32c370240a7b77c/tenor.gif","https://media1.tenor.com/images/2487a7679b3d7d23cadcd51381635467/tenor.gif","https://media1.tenor.com/images/7d43687195b86c8ce2411484eb1951fc/tenor.gif","https://media1.tenor.com/images/b2db2a7fe0b9f68f2869b4e0d11a9490/tenor.gif","https://media1.tenor.com/images/892831a51c11f30b4efd726763c3babe/tenor.gif","https://media1.tenor.com/images/2fe2e31bd486f36dd552f4d6e2e5b602/tenor.gif","https://media1.tenor.com/images/cff010b188084e1faed2905c0f1634c2/tenor.gif","https://media1.tenor.com/images/7a9723858a49246426158ac3f2993e1a/tenor.gif","https://media1.tenor.com/images/ffb0334ce56be6bd880db1d7a02ac5db/tenor.gif","https://media1.tenor.com/images/1a82719c62e19ab0495e5d49ce0d0053/tenor.gif"]
            p=link[random.randint(0,len(link)-1)]
            if user!=None:
                    embed=discord.Embed(description="{} punched {}... Must have been a real baka :punch:".format(ctx.message.author.name,user.name),color=0xf7d28c)
            else:
                    embed=discord.Embed(description="Hmm {} is punching themselves, what? :punch:".format(ctx.message.author.name),color=0xf7d28c)
            embed.set_image(url=p)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True,name="sleep",aliases=["sleepy"])
    async def sleep(self,ctx,*, user: discord.Member=None):
        try:
            link=["https://cdn.weeb.sh/images/ryBb41Kvb.gif","https://cdn.weeb.sh/images/SJKW4kYvZ.gif","https://cdn.weeb.sh/images/HJAx4ktD-.gif","https://cdn.weeb.sh/images/H1_-U6--f.gif","https://cdn.weeb.sh/images/HkGZVkKDW.gif","https://cdn.weeb.sh/images/rkxkM41tPW.gif","https://cdn.weeb.sh/images/rJ7ZNyKDW.gif","https://cdn.weeb.sh/images/SJYxNJKDZ.gif","https://cdn.weeb.sh/images/r1yzV1tPZ.gif","https://cdn.weeb.sh/images/rk3-NkKDb.gif","https://cdn.weeb.sh/images/By5ZNktDW.gif"]
            p=link[random.randint(0,len(link)-1)]
            if user!=None:
                    embed=discord.Embed(description="{} it seems like {} is sleepy, why not help them? <:gn:433510143095734273>".format(user.name,ctx.message.author.name),color=0xf7d28c)
            else:
                    embed=discord.Embed(description="{} seems to be feeling sleepy, why not go sleep? <:gn:433510143095734273>".format(ctx.message.author.name),color=0xf7d28c)
            embed.set_image(url=p)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True,name="cry",aliases=["cries","cri"])
    async def cry(self,ctx,*, user: discord.Member=None):
        try:
            link=["https://cdn.weeb.sh/images/Sk5a01cyf.gif","https://cdn.weeb.sh/images/H16Wkl5yf.gif","https://cdn.weeb.sh/images/ByF7REgdf.gif","https://cdn.weeb.sh/images/r1WMmLQvW.gif","https://cdn.weeb.sh/images/HJIpry35M.gif","https://cdn.weeb.sh/images/rJ5IX8XPZ.gif","https://cdn.weeb.sh/images/Sy1EUa-Zz.gif","https://cdn.weeb.sh/images/SJHw6yFVf.gif","https://cdn.weeb.sh/images/rknUmIXD-.gif","https://cdn.weeb.sh/images/rk8DrJhcf.gif","https://cdn.weeb.sh/images/HyiGQUmPb.gif","https://cdn.weeb.sh/images/Hk6EmLmDZ.gif","https://cdn.weeb.sh/images/BJJPXLQPW.gif"]
            p=link[random.randint(0,len(link)-1)]
            if user!=None:
                    embed=discord.Embed(description="Awww look {}, you made {} sad <a:crygif:447681152044498964>".format(user.name,ctx.message.author.name),color=0xf7d28c)
            else:
                    embed=discord.Embed(description="{} seems to be sad <a:crygif:447681152044498964>".format(ctx.message.author.name),color=0xf7d28c)
            embed.set_image(url=p)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True,name="nom",aliases=["noms"])
    async def nom(self,ctx,*, user: discord.Member=None):
        try:
            link=link=["https://cdn.weeb.sh/images/SJu1y1FPZ.gif","https://cdn.weeb.sh/images/SyI7yJKw-.gif","https://cdn.weeb.sh/images/SJPgk1Ywb.gif","https://cdn.weeb.sh/images/HJKQkktP-.gif","https://cdn.weeb.sh/images/ryDX1JKwW.gif","https://cdn.weeb.sh/images/HJtZJJYvb.gif","https://cdn.weeb.sh/images/SJAEkkFwb.gif","https://cdn.weeb.sh/images/HkGGy1Yvb.gif","https://cdn.weeb.sh/images/ryQ0AR_D-.gif","https://cdn.weeb.sh/images/BJyCCROP-.gif","https://cdn.weeb.sh/images/SklByktD-.gif","https://cdn.weeb.sh/images/HyXleWRSz.gif","https://cdn.weeb.sh/images/SJS-K64R-.gif","https://cdn.weeb.sh/images/rJ46ITVRb.gif","https://cdn.weeb.sh/images/rJZikZCBM.gif","https://cdn.weeb.sh/images/S12ACAdPZ.gif","https://cdn.weeb.sh/images/HJ_RAAuvb.gif","https://cdn.weeb.sh/images/rk7f1yFDW.gif"]
            p=link[random.randint(0,len(link)-1)]
            if user!=None:
                    embed=discord.Embed(description="{} feeds {}... Must have been really hungry...<a:nom:456715700845674509>".format(ctx.message.author.name,user.name),color=0xf7d28c)
            else:
                    embed=discord.Embed(description=" {} here's some food for you,eat up <a:nom:456715700845674509>".format(ctx.message.author.name),color=0xf7d28c)
            embed.set_image(url=p)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True,name="blush",aliases=["blushes"])
    async def blush(self,ctx,*, user: discord.Member=None):
        try:
            link=["https://cdn.weeb.sh/images/ryhfGI7vZ.gif","https://cdn.weeb.sh/images/SJkffIXw-.gif","https://cdn.weeb.sh/images/r1U7G87vZ.gif%","https://cdn.weeb.sh/images/rJa-zUmv-.gif","https://cdn.weeb.sh/images/SyIbfImDb.gif","https://cdn.weeb.sh/images/r19GfI7vW.gif","https://cdn.weeb.sh/images/BkalMI7Db.gif","https://cdn.weeb.sh/images/S1X7GIXw-.gif","https://cdn.weeb.sh/images/SJ8lf8Xwb.gif","https://cdn.weeb.sh/images/rkXur1ncz.gif","https://cdn.weeb.sh/images/B1NWGUmvb.gif","https://cdn.weeb.sh/images/Hy-GGIXvb.gif","https://cdn.weeb.sh/images/HklJGIXPW.gif","https://cdn.weeb.sh/images/rkYmGIXPb.gif","https://cdn.weeb.sh/images/rkQMGLmvZ.gif","https://cdn.weeb.sh/images/Sy1-ML7vW.gif","https://cdn.weeb.sh/images/r1n7M87wW.gif"]
            p=link[random.randint(0,len(link)-1)]
            if user!=None:
                    embed=discord.Embed(description="Aaawww {} you made {} blush,its so kawaii <:ehehe:452892342178021376>".format(user.name,ctx.message.author.name),color=0xf7d28c)
            else:
                    embed=discord.Embed(description="{} seems to be blushing,wonder why :3 <:ehehe:452892342178021376>".format(ctx.message.author.name),color=0xf7d28c)
            embed.set_image(url=p)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True,name="gaze",aliases=["stare","stares"])
    async def gaze(self,ctx,*, user: discord.Member=None):
        try:
            link=["https://cdn.weeb.sh/images/HyYuG-CBf.gif","https://cdn.weeb.sh/images/BkkqI1YPZ.jpeg","https://cdn.weeb.sh/images/HyWnLyKPZ.gif","https://cdn.weeb.sh/images/SyzsU1twZ.gif","https://cdn.weeb.sh/images/BJ88vLvd-.gif","https://cdn.weeb.sh/images/Hk22hAo9M.gif","https://cdn.weeb.sh/images/Sk5BOdQIG.gif","https://cdn.weeb.sh/images/ry7KIJYD-.gif","https://cdn.weeb.sh/images/rJao8JKv-.gif","https://cdn.weeb.sh/images/H1P_LyFPb.gif","https://cdn.weeb.sh/images/SkH3Uytwb.gif","https://cdn.weeb.sh/images/Hk768JtP-.gif","https://cdn.weeb.sh/images/rk23UyYP-.gif","https://cdn.weeb.sh/images/SkPoLJKwZ.gif","https://cdn.weeb.sh/images/rk5tI1Yv-.gif","https://cdn.weeb.sh/images/ryc3I1tv-.gif","https://cdn.weeb.sh/images/B1WpLJKwW.gif","https://cdn.weeb.sh/images/B1xpnU1YPZ.gif"]
            p=link[random.randint(0,len(link)-1)]
            if user!=None:
                    embed=discord.Embed(description="{}, {} is staring at you,what did you do? <a:gaze:457228137856499714>".format(user.name,ctx.message.author.name),color=0xf7d28c)
            else:
                    embed=discord.Embed(description=" hmm.... :thinking: {} is staring at something,I wonder what it is <a:gaze:457228137856499714>".format(ctx.message.author.name),color=0xf7d28c)
            embed.set_image(url=p)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True,name="butterfly",aliases=["butterflies","butterfli","buterfly","buterfli"])
    async def butterfly(self,ctx,*, user: discord.Member=None):
        try:
            link=["https://media.giphy.com/media/7OM8aqLAr2xQ4/giphy.gif","https://media.giphy.com/media/ErZOqoVIdI7zW/giphy.gif","http://bestanimations.com/Animals/Insects/Butterflys/butterfly-animated-gif-45.gif","http://bestanimations.com/Animals/Insects/Butterflys/butterfly-animated.gif","https://media.giphy.com/media/26BkLyXww5BZoL13q/giphy.gif","https://media3.giphy.com/media/OreKkqmHu1m6Y/giphy-downsized.gif","http://bestanimations.com/Animals/Insects/Butterflys/butterfly-animated-gif-21.gif","https://zippy.gfycat.com/NeighboringCompleteBluegill.gif","https://i.pinimg.com/originals/af/7c/2e/af7c2eb4f863774e70565d471d775cdf.gif","https://img1.picmix.com/output/stamp/normal/8/7/3/6/856378_b6e78.gif","https://img1.picmix.com/output/stamp/normal/1/4/9/7/857941_9b2a0.gif","https://i.pinimg.com/originals/77/18/c9/7718c92df8735c423ea3c01009bcfa14.gif","http://www.dilsecomments.com/uploads/glitter/large_glitter_1514530989.gif","https://media.giphy.com/media/EH5IYP7DPyYeI/giphy.gif","https://78.media.tumblr.com/a3cb1cc41b991f6116b5c99544fee773/tumblr_osx6fcHQtJ1uzomqmo1_500.gif","http://www.animatedimages.org/data/media/291/animated-butterfly-image-0389.gif","https://i.pinimg.com/originals/cc/cd/f4/cccdf4420d21abdb313ca419fd0d8271.gif"]
            p=link[random.randint(0,len(link)-1)]
            if user!=None:
                    embed=discord.Embed(description="{} wants {} to enjoy butterflies together :butterfly:".format(ctx.message.author.name,user.name),color=0xf7d28c)
            else:
                    embed=discord.Embed(description="{} here are your butterflies :butterfly:".format(ctx.message.author.name),color=0xf7d28c)
            embed.set_image(url=p)
            await self.bot.say(embed=embed)
        except Exception as e:
            await self.bot.say(e)

def setup(bot):
    bot.add_cog(GIFS(bot))
    print("Gifs is loaded")