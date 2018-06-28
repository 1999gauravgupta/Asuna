from discord.ext import commands
import asyncio
import discord
import string
import random
import inspect
import time


class BDCOMMANDS():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        tim = (after - before) * 1000
        await ctx.send('**Pong 🏓, took {0:.0f}ms**'.format(tim))
        print('ping')

    @commands.command(name='info', aliases=['user', 'userinfo'])
    async def info(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.author
        try:
            embed = discord.Embed(
                title="{}'s info".format(user.name), description="Here's what I could find.", color=16241292)
            embed.add_field(name='Name', value=user.name)
            embed.add_field(name='ID', value=user.id)
            embed.add_field(name='Status', value=user.status)
            embed.add_field(name='Highest role', value=user.top_role)
            embed.add_field(name='Joined', value=user.joined_at)
            embed.add_field(name='Created', value=user.created_at)
            embed.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=embed)
            print('User Info')
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    async def svrinfo(self, ctx, name='svrinfo', aliases=['serverinfo']):
        try:
            guild = ctx.guild
            role = [x.name for x in guild.role_hierarchy]
            roles = ''
            for i in role:
                roles += str(i) + ', '
            channelz = str(len(guild.channels))
            time = str(guild.created_at)
            time = time.split(' ')
            time = time[0]
            embed = discord.Embed(
                title=ctx.message.guild.name + ' info', description="Here's what I could find.", color=16241292)
            embed.add_field(name='Name', value=ctx.message.guild.name)
            embed.add_field(name='ID', value=ctx.message.guild.id)
            embed.add_field(name='Owner', value=ctx.message.guild.owner.name)
            embed.add_field(name='Channels', value=channelz)
            embed.add_field(name='Emojis', value=len(ctx.message.guild.emojis))
            embed.add_field(name='Members', value=len(ctx.message.guild.members))
            embed.add_field(name='Roles', value=len(ctx.message.guild.roles))
            embed.add_field(name='Server roles', value=roles)
            embed.set_thumbnail(url=ctx.message.guild.icon_url)
            await ctx.send(embed=embed)
            print('Server Info')
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    async def say(self, ctx, *, something=None):
        owner = [343395225571426304, 402829897514352641]
        if ctx.author.id in owner:
            if something is None:
                await ctx.send('What would you like me to say? :thinking:')
            else:
                await ctx.send(something)
        else:
            await ctx.send('I only listen to my owner')
        await ctx.message.delete()
        print('Say')

    @commands.command()
    async def spam(self, ctx, no=1, *, something=None):
        owner = [343395225571426304, 402829897514352641]
        if ctx.author.id in owner:
            if something is None:
                await ctx.send('What would you like me to say? :thinking:')
            else:
                for i in range(no):
                    await ctx.send(something)
        else:
            await ctx.send('I only listen to my owner')
        await ctx.message.delete()
        print('Spam')

    @commands.command(name='pfp', aliases=['dp', 'avatar'])
    async def pfp(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.author
        try:
            embed = discord.Embed(title="{}'s avatar".format(user.name), color=16241292)
            embed.set_image(url=user.avatar_url)
            await ctx.send(embed=embed)
            print('Avatar')
        except Exception as e:
            await ctx.send(e)

    @commands.command()
    async def code(self, ctx, *, something=None):
        owner = [343395225571426304, 402829897514352641]
        if ctx.author.id in owner:
            try:
                if something is None:
                    await ctx.send('What would you like me to say? :thinking:')
                else:
                    await ctx.send(('```' + inspect.getsource(self.bot.get_command(something).callback)) + '```')
            except Exception as e:
                await ctx.send('Code may be over word limit')
                print(e)
        else:
            await ctx.send('I only listen to my owner')
        print('code')

    @commands.command()
    async def invite(self, ctx,user: discord.Member = Asuna):
        try:
            embed = discord.Embed(title="Asuna's Invite Link", value='Add Asuna to your guild', color=16241292)
            embed.add_field(name='Name', value='Asuna')
            embed.add_field(name='Prefix', value='-, Asuna , asuna')
            embed.add_field(
                name='Link',
                value='https://discordapp.com/api/oauth2/authorize?client_id=411566473350217748&permissions=8&scope=bot'
            )
            embed.set_footer(text='Feel free to uncheck some permissions')
            embed.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=embed)
            print('invite')
        except Exception as e:
            await ctx.send(e)

    @commands.command(name='purge', aliases=['prune'])
    async def purge(self, ctx, number=2):
        if ctx.author.guild_permissions.manage_messages:
            mgs = []
            number = int(number)
            if number < 2:
                number = 2
            if number<=100:
                try:
                    await ctx.channel.purge(limit=number)
                except Exception:
                    pass
            if number>100:
                while number>0:
                    try:
                        await ctx.channel.purge(limit=100)
                    except Exception:
                        pass
                    number-=100
        else:
            await ctx.send('You do not have required permissions')
        print('purge')

    @commands.command(name='perms', aliases=['permissions', 'permission'])
    async def perms(self, ctx, *, user: discord.Member = None):
        if user == None:
            user = ctx.author
        var = dict(user.guild_permissions)
        str1 = ''
        for i in var:
            j = i.replace('_', ' ')
            if var[i] == True:
                str1 += (':small_blue_diamond:' + j.title()) + '\n'
            else:
                str1 += (':small_orange_diamond:' + j.title()) + '\n'
        embed = discord.Embed(
            title=' Permissions for {} in this server'.format(user.name), description=str1, color=16241292)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BDCOMMANDS(bot))
    print('Basic Discord Commands is loaded')