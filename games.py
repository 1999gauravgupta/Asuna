from discord.ext import commands
import asyncio
import discord
import requests
import json
import string
import random

class GAMES():
    def __init__(self, bot):
        self.bot = bot
 
    def card_drawer(self,deck):
        restrict=["QH","QS"]
        draw = requests.get('https://deckofcardsapi.com/api/deck/{}/draw/?count=1'.format(deck))
        draw = json.loads(draw.content.decode('utf-8'))
        if draw["cards"][0]["code"] in restrict:
            card_drawer(deck)
        else:
            return draw
    
    def card_to_emoji(self,card):       
        for a in self.bot.guilds:
            if a.id==461497700160897035:
                for emoji in a.emojis:
                    if emoji.name==card:
                        return "<:{}:{}>".format(emoji.name,emoji.id)

    @commands.command(name='bj', aliases=['blackjack'])
    async def bj(self, ctx):
        d_valuea = []
        u_cards = []
        d_cards = []
        u_value = 0
        d_value=0
        fc = ['KING', 'QUEEN', 'JACK']
        def check(m):
            return m.author.id == ctx.author.id and m.channel == ctx.channel
        r = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
        r = json.loads(r.content.decode('utf-8'))
        deck = r['deck_id']
        for j in range(2):
            draw=self.card_drawer(deck)
            if draw['cards'][0]['value'] in fc:
                u_value += 10
            elif draw['cards'][0]['value'] == 'ACE':
                u_value += 11
            else:
                u_value += int(draw['cards'][0]['value'])
            u_cards.append(draw['cards'][0]['code'])
        draw=self.card_drawer(deck)
        if draw['cards'][0]['value'] in fc:
            d_value += 10
        elif draw['cards'][0]['value'] == 'ACE':
            d_value += 11
        else:
            d_value += int(draw['cards'][0]['value'])
        d_cards.append(draw['cards'][0]['code'])
        d_valuea.append(d_value)
        q=""
        w=""
        for i in u_cards:
            a=self.card_to_emoji(i)
            q+=a+" "
        for i in d_cards:
            a=self.card_to_emoji(i)
            w+=a+" "
        embed = discord.Embed(title='Blackjack', color=16241292)
        embed.add_field(name='User Cards', value=q)
        embed.add_field(name='Dealer Cards', value=w)
        embed.add_field(name='User Cards value', value=u_value)
        embed.add_field(name='Dealer Cards value', value=d_value, inline=True)
        embed.add_field(name='\u200b', value='Hit/Stand/Double Down')
        await ctx.send(embed=embed)  

        option = await self.bot.wait_for('message', check = check)
        option = str(option.content)
        if option.lower() == 'stand':
            pass
        else:
            draw=self.card_drawer(deck)
            if draw['cards'][0]['value'] in fc:
                u_value += 10
            elif draw['cards'][0]['value'] == 'ACE':
                u_value += 11
            else:
                u_value += int(draw['cards'][0]['value'])
            u_cards.append(draw['cards'][0]['code'])
        for k in range(2):
            draw=self.card_drawer(deck)
            if draw['cards'][0]['value'] in fc:
                d_value += 10
            elif draw['cards'][0]['value'] == 'ACE':
                d_value += 11
            else:
                d_value += int(draw['cards'][0]['value'])
            d_valuea.append(d_value)
            if d_value<=21:
                d_cards.append(draw['cards'][0]['code'])
        d_value = d_valuea[len(d_cards)-1]
        q=""
        w=""
        for i in u_cards:
            a=self.card_to_emoji(i)
            q+=a+" "
        for i in d_cards:
            a=self.card_to_emoji(i)
            w+=a+" "

        if u_value > 21: 
            embed = discord.Embed(title='Blackjack', color=15875132)
            embed.add_field(name='User Cards', value=q)
            embed.add_field(name='Dealer Cards', value=w)
            embed.add_field(name='User Cards value', value=u_value)
            embed.add_field(name='Dealer Cards value', value=d_value, inline=True)
            await ctx.send(embed=embed)
        elif (u_value <= 21) and (u_value >= d_value):
            embed = discord.Embed(title='Blackjack', color=3994233)
            embed.add_field(name='User Cards', value=q)
            embed.add_field(name='Dealer Cards', value=w)
            embed.add_field(name='User Cards value', value=u_value)
            embed.add_field(name='Dealer Cards value', value=d_value, inline=True)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='Blackjack', color=15875132)
            embed.add_field(name='User Cards', value=q)
            embed.add_field(name='Dealer Cards', value=w)
            embed.add_field(name='User Cards value', value=u_value)
            embed.add_field(name='Dealer Cards value', value=d_value, inline=True)
            await ctx.send(embed=embed)

    def number_to_emoji(self,number):  
        if number==0:
            return "<:citizen:461123113606840333>"
        elif number==1:
            return "<:slave:461123128857460736>"
        else:
            return "<:emperor:461123147744149505>"
    @commands.command()
    async def ecard(self,ctx,choice="emperor"):
        u_cards=[]
        o_cards=[]
        flag=1
        if choice.lower()=="emperor":
            u_cards=[2,0,0,0,0]
            o_cards=[1,0,0,0,0]
        if choice.lower()=="slave":
            o_cards=[2,0,0,0,0]
            u_cards=[1,0,0,0,0]
        while flag==1:   
            uc=""
            for i in u_cards:
                j=self.number_to_emoji(i)
                uc+=j+" "
            oc=""
            for i in o_cards:
                j=self.number_to_emoji(i)
                oc+=j+" "
            embed=discord.Embed(title="ECard-Kaiji",color=16241292)
            embed.add_field(name="User Cards: ",value=uc)
            embed.add_field(name="Computer Cards: ",value=oc)
            await ctx.send(embed=embed)
            def check(m):
                return m.author.id == ctx.author.id and m.channel == ctx.channel
            await ctx.send("Pick ur card: ")
            pick1 = await self.bot.wait_for('message', check = check)
            pick1 = str(pick1.content).lower()
            if pick1=="c" or pick1=="citizen":
                pick1=0
                uc=self.number_to_emoji(pick1)
            elif pick1=="s" or pick1=="slave":
                pick1=1
                uc=self.number_to_emoji(pick1)
            else:
                pick1=2
                uc=self.number_to_emoji(pick1)
            u_cards.remove(pick1)
            pick2=o_cards[random.randint(0,len(o_cards)-1)]
            if pick2==0:
                oc=self.number_to_emoji(pick2)
            elif pick2==1:
                oc=self.number_to_emoji(pick2)
            else:
                oc=self.number_to_emoji(pick2)
            o_cards.remove(pick2)
            r=""
            if pick1==0 and pick2==0:
                r=("Round Draw")
            elif pick1==2 and (pick2==0 or pick2==1):
                r=("User Won")
                flag=0
            elif pick2==2 and (pick1==0 or pick2==1):
                r=("Computer Won")
                flag=0
            elif pick1==2 and pick2==1:
                r=("Computer Won")
                flag=0
            elif pick1==1 and pick2==2:
                r=("User Won")
                flag=0
            elif pick1==0 and pick2==1:
                r=("User Won")
                flag=0
            elif pick1==1 and pick2==0:
                r=("Computer Won")
                flag=0
            embed=discord.Embed(title="ECard-Kaiji",color=16241292)
            embed.add_field(name="User Cards: ",value=uc)
            embed.add_field(name="Computer Cards: ",value=oc)
            embed.add_field(name="Result: ",value=r)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(GAMES(bot))
    print('Games is loaded')