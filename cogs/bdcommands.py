from discord.ext import commands
import asyncio
import discord
import string
import random
import inspect
import time
import re

class BDCOMMANDS():
    def __init__(self, bot):
        self.bot = bot

    async def user_fetcher(self,ctx,user):
        try:
            if user is None:
                return ctx.message.author
            elif len(ctx.message.mentions)>0:
                return ctx.message.mentions[0]
            elif re.search(r'\d{17,21}',str(user))!=None:
                return (await self.bot.get_user_info(user))
            else:
                results = []
                for i in ctx.message.guild.members:
                    if user.lower() in i.name.lower() or user.lower() in i.display_name.lower():
                        results.append(i)
                if len(results)>0:
                    if len(results)==1:
                        return results[0]
                    else:
                        stri=""
                        counter=1
                        await ctx.send("Multiple members found. Please choose one of the following, or type cancel.")
                        for i in results:
                            stri+=str(counter)+". "+"``"+str(i)+"``"+"\n"
                            counter+=1
                        await ctx.send(stri)
                        def check(p):
                            return p.author.id == ctx.author.id and p.channel == ctx.channel
                        m =await self.bot.wait_for('message', check = check)
                        def check2(p):
                            return p.author.id in [ctx.author.id,self.bot.user.id] and p.channel == ctx.channel
                        if m.content.lower()=="cancel":
                            await ctx.channel.purge(limit=4,check=check2)
                            await ctx.send(":x: Command Cancelled.")
                            return "cancel"
                        else:
                            await ctx.channel.purge(limit=4,check=check2)
                            m=int(m.content)-1
                            return results[m]
                else:
                    return None
        except Exception as e:
            print(e)
            return None
    
    async def role_fetcher(self,ctx,role):
        try:
            roles = [x.name for x in ctx.guild.role_hierarchy]
            roles_matched=[]
            for i in roles:
                if role.lower() in i.lower():
                    roles_matched.append(discord.utils.get(ctx.message.guild.roles, name=i))
            if len(roles_matched)>0:
                if len(roles_matched)==1:
                    return roles_matched[0]
                else:
                    await ctx.send("Multiple roles found. Please choose one of the following, or type cancel.")
                    stri=""
                    counter=1
                    for i in roles_matched:
                        stri+=str(counter)+". "+"``"+str(i)+"``"+"\n"
                        counter+=1
                    await ctx.send(stri)
                    def check(p):
                        return p.author.id == ctx.author.id and p.channel == ctx.channel
                    m =await self.bot.wait_for('message', check = check)
                    def check2(p):
                        return p.author.id in [ctx.author.id,self.bot.user.id] and p.channel == ctx.channel
                    if m.content.lower()=="cancel":
                        await ctx.channel.purge(limit=4,check=check2)
                        await ctx.send(":x: Command Cancelled.")
                        return "cancel"
                    else:
                        await ctx.channel.purge(limit=4,check=check2)
                        m=int(m.content)-1
                        return roles_matched[m]
            else:
                return None
        except Exception as e:
            print(e)
            return None

    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        await (await self.bot.ws.ping())
        after = time.monotonic()
        tim = (after - before) * 1000
        await ctx.send('**Pong 🏓, took {0:.0f}ms**'.format(tim))
        print('ping')

    @commands.command(name="user",aliases=["userinfo","info"])
    async def user(self, ctx, *, user=None):
        try:
            user=await self.user_fetcher(ctx,user)
            if user=="cancel":
                return
            if user is None:
                await ctx.send("Dear {},the user you typed does not seem to exist. Please make sure you provided correct details.".format(ctx.message.author.mention))
                return
            if str(user.status)=="online":
                img="<:online:468084069305942036>"
            elif str(user.status)=="idle":
                img="<:idle:468084104664186915>"
            elif str(user.status)=="dnd":
                img="<:dnd:468084139195629588>"
            elif str(user.status)=="offline":
                img="<:offline:468084174767521792>"
            list1=[]
            for member in ctx.message.guild.members:
                list1.append(member.joined_at)
            list1.sort()
            p=list1.index(user.joined_at)       
            embed=discord.Embed(title=str(user),description=user.id, color=random.randint(0, 16777215))
            embed.add_field(name="\u200b",value=img+str(user.mention),inline=False)
            embed.add_field(name='Joined At:', value=str(user.joined_at)[0:16],inline=False)
            embed.add_field(name='Created At:', value=str(user.created_at)[0:16],inline=False)
            embed.add_field(name="Member Number:",value=str(p+1),inline=False)
            embed.add_field(name='Highest role:', value= (user.top_role.mention),inline=False)
            embed.add_field(name="Game:",value=(user.activity),inline=False)
            embed.set_thumbnail(url=(user.avatar_url))
            await ctx.send(embed=embed)
        except Exception as e:
            print(e)
            await ctx.send("Dear {},the user you typed does not seem to exist. Please make sure you provided correct details.".format(ctx.message.author.mention))
        print("UserInfo")

    @commands.command(name="server",aliases=["serverinfo","svrinfo"])
    async def server(self,ctx):
        '''Gives details about our lovely Spark'''
        guild=ctx.message.guild
        user_count=0
        bot_count=0
        total_count=0
        online_count=0
        idle_count=0
        dnd_count=0
        offline_count=0
        ban_count=0
        created=str(guild.created_at)[0:16]
        for member in guild.members:
            if member.bot==True:
                bot_count+=1
            elif member.bot==False:
                user_count+=1
            if str(member.status)=="online":
                online_count+=1
            elif str(member.status)=="idle":
                idle_count+=1
            elif str(member.status)=="dnd":
                dnd_count+=1
            elif str(member.status)=="offline":
                offline_count+=1
            total_count+=1
        
        embed = discord.Embed(title=guild.name, description=guild.id, color=random.randint(0, 16777215))
        embed.add_field(name='Owner:', value=guild.owner,inline=False)
        embed.add_field(name="Users:",value="{} Users[{} Humans|{} Bots] \n <:online:468084069305942036> {} \n <:idle:468084104664186915> {} \n <:dnd:468084139195629588> {} \n <:offline:468084174767521792> {}".format(str(total_count),str(user_count),str(bot_count),str(online_count),str(idle_count),str(dnd_count),str(offline_count)),inline=False)
        embed.add_field(name='Roles:', value=len(guild.roles),inline=False)
        embed.add_field(name='Emojis:', value=len(guild.emojis),inline=False)
        embed.add_field(name="Created [YYYY-MM-DD HH:MM]:",value=created,inline=False)
        embed.add_field(name="Channels:",value="{} Channels[{} Text Channels|{} Voice Channels]".format(str(len(guild.text_channels)+len(guild.voice_channels)),str(len(guild.text_channels)),str(len(guild.voice_channels))),inline=False)
        embed.add_field(name="Region:",value=guild.region,inline=False)
        embed.add_field(name="Ban Count:",value=len(await guild.bans()),inline=False)
        embed.add_field(name="Verification Level:",value=guild.verification_level,inline=False)
        embed.set_thumbnail(url=guild.icon_url)
        await ctx.send(embed=embed)
        print("ServerInfo")

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

    @commands.command(name='avatar', aliases=['dp', 'pfp'])
    async def avatar(self, ctx, *, user=None):
        try:
            if user=="server":
                embed = discord.Embed(title=ctx.guild.name.title(), color=random.randint(0, 16777215))
                embed.set_image(url=ctx.message.guild.icon_url)
                await ctx.send(embed=embed) 
                return
            user=await self.user_fetcher(ctx,user)
            if user=="cancel":
                return
            if user is None:
                await ctx.send("Dear {},the user you typed does not seem to exist. Please make sure you provided correct details.".format(ctx.message.author.mention))
                return
            else:
                embed = discord.Embed(title=str(user), color=random.randint(0, 16777215))
                embed.set_image(url=user.avatar_url)
                await ctx.send(embed=embed)       
        except Exception as e:
            print(e)
            await ctx.send("Dear {},the user you typed does not seem to exist. Please make sure you provided correct details.".format(ctx.message.author.mention))         
        print("avatar")

    @commands.command()
    async def code(self, ctx, *, something=None):
        owner = [343395225571426304, 402829897514352641]
        if ctx.author.id in owner:
            try:
                if something is None:
                    await ctx.send('What would you like me to say? :thinking:')
                else:
                    await ctx.send(('```py\n' + str(inspect.getsource(self.bot.get_command(something).callback)) + '```'))
            except Exception as e:
                await ctx.send('Code may be over word limit')
                print(e)
        else:
            await ctx.send('I only listen to my owner')
        print('code')

    @commands.command()
    async def invite(self, ctx):
        try:
            embed = discord.Embed(title="Asuna's Invite Link", value='Add Asuna to your guild', color=random.randint(0, 16777215))
            embed.add_field(name='Name', value='Asuna')
            embed.add_field(name='Prefix', value='-, Asuna , asuna')
            embed.add_field(
                name='Link',
                value='https://discordapp.com/api/oauth2/authorize?client_id=411566473350217748&permissions=8&scope=bot'
            )
            embed.set_footer(text='Feel free to uncheck some permissions')
            embed.set_thumbnail(url=self.bot.user.avatar_url)
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
    async def perms(self, ctx, *, user= None):
        try:
            user=await self.user_fetcher(ctx,user)
            if user=="cancel":
                return
            if user is None:
                await ctx.send("Dear {},the user you typed does not seem to exist. Please make sure you provided correct details.".format(ctx.message.author.mention))
                return
            var = dict(user.guild_permissions)
            str1 = ''
            for i in var:
                j = i.replace('_', ' ')
                if var[i] == True:
                    str1 += ('<:online:468084069305942036>' + j.title()) + '\n'
                else:
                    str1 += ('<:dnd:468084139195629588>' + j.title()) + '\n'
            embed = discord.Embed(
                title=' Permissions for {} in this server'.format(user.name), description=str1, color=random.randint(0, 16777215))
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send("Dear {},the user you typed does not seem to exist. Please make sure you provided correct details.".format(ctx.message.author.mention))
        print("permissions")

    @commands.command(name="role",aliases=["roles","roleinfo"])
    async def role(self,ctx,*,role=None):
        try:
            if role is None:
                role = [x.name for x in ctx.guild.role_hierarchy]
                l=len(role)
                role=",".join(role)
                embed=discord.Embed(title="Server Roles",description="Here is a list of all server roles",color=random.randint(0, 16777215))
                embed.add_field(name="\u200b",value=role)
                embed.add_field(name="Number of roles: ",value=l)
                await ctx.send(embed=embed)
            else:
                role =await self.role_fetcher(ctx,role)
                if role=="cancel":
                    return
                if role is None:
                    await ctx.send("Dear {},the role you typed does not seem to exist. Please make sure you provided correct details.".format(ctx.message.author.mention))
                    return
                p=str(role.color)
                l=p.replace("0x","#")
                embed=discord.Embed(title="{}".format(role.name),description=role.id,color=role.color)
                embed.add_field(name="Color:",value=l)
                embed.add_field(name="Created At:",value=str(role.created_at)[0:16],inline=False)
                embed.add_field(name="Members:",value=len(role.members),inline=False)
                embed.add_field(name="Position from top:",value=([x.name for x in ctx.message.guild.role_hierarchy].index(str(role.name))+1),inline=False)
                embed.add_field(name="Mention:",value=role.mention,inline=False)
                embed.add_field(name="Mentionable:",value=role.mentionable,inline=False)
                embed.add_field(name="Hoisted:",value=role.hoist,inline=False)
                embed.add_field(name="Managed:",value=role.managed,inline=False)
                await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send("Dear {},the role you typed does not seem to exist. Please make sure you provided correct details.".format(ctx.message.author.mention))
            print(e)
        print("role")


def setup(bot):
    bot.add_cog(BDCOMMANDS(bot))
    print('Basic Discord Commands is loaded')
