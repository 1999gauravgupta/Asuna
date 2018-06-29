from discord.ext import commands
import asyncio
import discord
import requests
import json
import string


class GAMES():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bj', aliases=['blackjack'])
    async def bj(self, ctx):
        d_valuea = []
        fc = ['KING', 'QUEEN', 'JACK']
        def check(m):
            return m.author.id == ctx.author.id and m.channel == ctx.channel
        r = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
        r = json.loads(r.content.decode('utf-8'))
        deck = r['deck_id']
        draw = requests.get('https://deckofcardsapi.com/api/deck/{}/draw/?count=2'.format(deck))
        draw = json.loads(draw.content.decode('utf-8'))
        u_value = 0
        u_cards = []
        d_cards = []
        for j in range(2):
            if draw['cards'][j]['value'] in fc:
                u_value += 10
            elif draw['cards'][j]['value'] == 'ACE':
                u_value += 11
            else:
                u_value += int(draw['cards'][j]['value'])
            u_cards.append(draw['cards'][j]['code'])
        d_value = 0
        draw = requests.get('https://deckofcardsapi.com/api/deck/{}/draw/?count=1'.format(deck))
        draw = json.loads(draw.content.decode('utf-8'))
        if draw['cards'][0]['value'] in fc:
            d_value += 10
        elif draw['cards'][0]['value'] == 'ACE':
            d_value += 11
        else:
            d_value += int(draw['cards'][0]['value'])
        d_cards.append(draw['cards'][0]['code'])
        d_valuea.append(d_value)
        q = ''
        w = ''
        for a in u_cards:
            q += a + ' '
        for b in d_cards:
            w += b + ' '
        embed = discord.Embed(title='Blackjack', color=16241292)
        embed.add_field(name='User Cards', value=q)
        embed.add_field(name='Dealer Cards', value=w)
        embed.add_field(name='User Cards value', value=u_value)
        embed.add_field(name='Dealer Cards value', value=d_value, inline=True)
        embed.add_field(name='\u200b', value='Hit/Stand/Double Down')
        await ctx.send(embed=embed)  # print(u_value,d_value)
        def check(m):
            return m.author.id == ctx.author.id and m.channel == ctx.channel
        option = await self.bot.wait_for('message', check = check)
        option = str(option.content)
        if option.lower() == 'hit':
            draw = requests.get('https://deckofcardsapi.com/api/deck/{}/draw/?count=1'.format(deck))
            draw = json.loads(draw.content.decode('utf-8'))
            if draw['cards'][0]['value'] in fc:
                u_value += 10
            elif draw['cards'][0]['value'] == 'ACE':
                u_value += 11
            else:
                u_value += int(draw['cards'][0]['value'])
            u_cards.append(draw['cards'][0]['code'])
        elif option.lower() == 'double down':
            draw = requests.get('https://deckofcardsapi.com/api/deck/{}/draw/?count=1'.format(deck))
            draw = json.loads(draw.content.decode('utf-8'))
            if draw['cards'][0]['value'] in fc:
                u_value += 10
            elif draw['cards'][0]['value'] == 'ACE':
                u_value += 11
            else:
                u_value += int(draw['cards'][0]['value'])
            u_cards.append(draw['cards'][0]['code'])
        else:
            pass
        draw = requests.get('https://deckofcardsapi.com/api/deck/{}/draw/?count=2'.format(deck))
        draw = json.loads(draw.content.decode('utf-8'))
        for k in range(2):
            if draw['cards'][k]['value'] in fc:
                d_value += 10
            elif draw['cards'][k]['value'] == 'ACE':
                d_value += 11
            else:
                d_value += int(draw['cards'][k]['value'])
            d_valuea.append(d_value)
            d_cards.append(draw['cards'][k]['code'])
        for i in d_valuea:
            if i <= 21:
                d_value = i
        try:
            await ctx.message.delete()
        except Exception:
            pass
        if u_value > 21: 
            q = ''
            w = ''
            for a in u_cards:
                q += a + ' '
            for b in d_cards:
                w += b + ' '
            embed = discord.Embed(title='Blackjack', color=15875132)
            embed.add_field(name='User Cards', value=q)
            embed.add_field(name='Dealer Cards', value=w)
            embed.add_field(name='User Cards value', value=u_value)
            embed.add_field(name='Dealer Cards value', value=d_value, inline=True)
            await ctx.send(embed=embed)
        elif (u_value <= 21) and (u_value >= d_value):
            q = ''
            w = ''
            for a in u_cards:
                q += a + ' '
            for b in d_cards:
                w += b + ' '
            embed = discord.Embed(title='Blackjack', color=3994233)
            embed.add_field(name='User Cards', value=q)
            embed.add_field(name='Dealer Cards', value=w)
            embed.add_field(name='User Cards value', value=u_value)
            embed.add_field(name='Dealer Cards value', value=d_value, inline=True)
            await ctx.send(embed=embed)
        else:
            q = ''
            w = ''
            for a in u_cards:
                q += a + ' '
            for b in d_cards:
                w += b + ' '
            embed = discord.Embed(title='Blackjack', color=15875132)
            embed.add_field(name='User Cards', value=q)
            embed.add_field(name='Dealer Cards', value=w)
            embed.add_field(name='User Cards value', value=u_value)
            embed.add_field(name='Dealer Cards value', value=d_value, inline=True)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(GAMES(bot))
    print('Games is loaded')
