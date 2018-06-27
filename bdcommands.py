from discord.ext import commands
import asyncio
import discord
import string
import random

class BDCOMMANDS:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self):
        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        tim = (after-before)*1000
        await self.bot.say("**Pong 🏓, took {0:.0f}ms**".format(tim))
        print("ping")

    @commands.command(pass_context=True,name="info",aliases=["user","userinfo"])
    async def info(self,ctx,*, user: discord.Member=None):
        if user is None:
            user = ctx.message.author
        try:
            embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0xf7d28c)
            embed.add_field(name="Name", value=user.name)
            embed.add_field(name="ID", value=user.id)
            embed.add_field(name="Status", value=user.status)
            embed.add_field(name="Highest role", value=user.top_role)
            embed.add_field(name="Joined", value=user.joined_at)
            embed.add_field(name="Created",value=user.created_at)
            embed.set_thumbnail(url=user.avatar_url)
            await self.bot.say(embed=embed)
            print("User Info")
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True)
    async def svrinfo(self,ctx,name="svrinfo",aliases=["serverinfo"]):
        try:
            server = ctx.message.server
            role = [x.name for x in server.role_hierarchy]
            roles=""
            for i in role:
                roles+=(str(i)+", ")
            channelz = str(len(server.channels))
            time = str(server.created_at); time = time.split(' '); time= time[0]
            embed = discord.Embed(title= (ctx.message.server.name+" info"), description="Here's what I could find.", color=0xf7d28c)
            embed.add_field(name="Name", value=ctx.message.server.name)
            embed.add_field(name="ID", value=ctx.message.server.id)
            embed.add_field(name="Owner",value=ctx.message.server.owner.name)
            embed.add_field(name="Channels",value=channelz)
            embed.add_field(name="Emojis",value=len(ctx.message.server.emojis))
            embed.add_field(name="Members", value=len(ctx.message.server.members))
            embed.add_field(name="Roles", value=len(ctx.message.server.roles))
            embed.add_field(name="Server roles",value=roles)
            embed.set_thumbnail(url=ctx.message.server.icon_url)
            await self.bot.say(embed=embed)
            print("Server Info")
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True)
    async def say(self,ctx,*,something=None):
        owner=["343395225571426304","402829897514352641"]
        if ctx.message.author.id in owner:
            if something is None:
                await self.bot.say("What would you like me to say? :thinking:")
            else:
                await self.bot.say(something)
        else:
            await self.bot.say("I only listen to my owner")
        await self.bot.delete_message(ctx.message)
        print("Say")

    @commands.command(pass_context=True)
    async def spam(self,ctx,no=1,*,something=None):
        owner=["343395225571426304","402829897514352641"]
        if ctx.message.author.id in owner :
            if something is None:
                await self.bot.say("What would you like me to say? :thinking:")
            else:
                for i in range(no):
                    await self.bot.say(something)
        else:
            await self.bot.say("I only listen to my owner")
        await self.bot.delete_message(ctx.message)
        print("Spam")

    @commands.command(pass_context=True,name="pfp",aliases=["dp","avatar"])
    async def pfp(self,ctx,*,user:discord.Member=None):
        if user is None:
            user = ctx.message.author
        try:
            embed=discord.Embed(title="{}'s avatar".format(user.name),color=0xf7d28c)
            embed.set_image(url=user.avatar_url)
            await self.bot.say(embed=embed)
            print("Avatar")
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context=True)
    async def code(self,ctx,*,something=None):
        owner=["343395225571426304","402829897514352641"]
        if ctx.message.author.id in owner:
            try:
                if something is None:
                    await self.bot.say("What would you like me to say? :thinking:")
                else:
                    await self.bot.say("```"+inspect.getsource(bot.get_command(something).callback)+"```")
            except Exception as e:
                await self.bot.say("Code may be over word limit")
                print(e)
        else:
            await self.bot.say("I only listen to my owner")
        print("code")

    @commands.command(pass_context=True)
    async def invite(self,ctx):
        try:
            member = discord.utils
            Asuna = discord.utils.get(ctx.message.server.members, id="411566473350217748")
            embed=discord.Embed(title="Asuna's Invite Link",value="Add Asuna to your guild",color=0xf7d28c)
            embed.add_field(name="Name",value="Asuna")
            embed.add_field(name="Prefix",value="-, Asuna , asuna")
            embed.add_field(name="Link",value="https://discordapp.com/api/oauth2/authorize?client_id=411566473350217748&permissions=8&scope=bot")
            embed.set_footer(text="Feel free to uncheck some permissions")
            embed.set_thumbnail(url=Asuna.avatar_url)
            await self.bot.say(embed=embed)
            print("invite")
        except Exception as e:
            await self.bot.say(e)

    @commands.command(pass_context = True,name="purge",aliases=["prune"])
    async def purge(self,ctx, number=2,):
        if ctx.message.author.server_permissions.manage_messages:
            mgs = []
            number = int(number)
            if number<2:
                number=2
            if number<=100:
                async for x in bot.logs_from(ctx.message.channel, limit = number):
                    mgs.append(x)
                await self.bot.delete_messages(mgs)
            else:
                temp=0
                while temp!=number:
                    async for x in bot.logs_from(ctx.message.channel, limit = 100):
                        mgs.append(x)
                        temp=temp+1
                        if temp>number:
                            break
                    await self.bot.delete_messages(mgs)
                print(temp)
        else:
            await self.bot.say("You do not have required permissions")
        print("purge")

    @commands.command(pass_context=True,name="perms",aliases=["permissions","permission"])
    async def perms(self,ctx,*, user: discord.Member=None):
        if user==None:
            user=ctx.message.author
        var=dict(user.server_permissions)
        str1=""
        for i in var:
            j=i.replace("_"," ")
            if var[i]==True:
                str1+=":small_blue_diamond:"+j.title()+"\n"
            else:
                str1+=":small_orange_diamond:"+j.title()+"\n"
        embed=discord.Embed(title=" Permissions for {} in this server".format(user.name),description=str1,color=0xf7d28c)
        await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(BDCOMMANDS(bot))
    print("Basic Discord Commands is loaded")