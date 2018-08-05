from discord.ext import commands
import asyncio
import discord
import json
import requests
import string
import lyricwikia
import spice_api as spice
import urbandictionary as udd
import random


class QUERY():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ud', aliases=['urban'])
    async def ud(self, ctx, *, query=None):
        if query != None:
            try:
                defs = udd.define(query)
                for d in range(1):
                    definition = defs[d].definition
                    word = defs[d].word
                    example = defs[d].example
                    upvotes = defs[d].upvotes
                    downvotes = defs[d].downvotes
                embed = discord.Embed(title=word, description="Here's what I could find.", color=random.randint(0, 16777215))
                embed.add_field(name='Defintion', value=definition, inline=False)
                embed.add_field(name='Example', value=example if example else '\u200b', inline=False)
                embed.add_field(name='Upvotes', value=str(upvotes) + '👍', inline=True)
                embed.add_field(name='Downvotes', value=str(downvotes) + '👎', inline=True)
                await ctx.send(embed=embed)
            except Exception:
                await ctx.send('Dear User, I could not find a definition for this word in Urban Dictionary')
        print('ud')

    @commands.command(name='google', aliases=['g', 'search'])
    async def google(self, ctx, *, query=None):
        if query != None:
            try:
                query = '-'.join(query.split())
                response = requests.get('http://api.tanvis.xyz/search/{}'.format(query))
                response = json.loads(response.content.decode('utf-8'))
                await ctx.send(response[0]['link'])
            except Exception:
                await ctx.send('Service unavailable atm')
        print('google')

    @commands.command(name='wiki', aliases=['wikipedia'])
    async def wiki(self, ctx, *, query=None):
        if query != None:
            try:
                response = requests.get('http://api.tanvis.xyz/search/{}'.format("wikipedia "+query))
                response = json.loads(response.content.decode('utf-8'))
                await ctx.send(response[0]['link'])
            except Exception:
                await ctx.send('Service unavailable atm')

    @commands.command(name='translate', aliases=['trans'])
    async def translate(self, ctx, lg="en",*, query=None,):
        if query != None:
            query = '%20'.join(query.split())
            response = requests.get('http://api.tanvis.xyz/translate/{}?&to={}'.format(query,lg))
            response = json.loads(response.content.decode('utf-8'))
            await ctx.send(response['to']['text'])
            await ctx.send('The input text language is ' + response['from']['lang'])

    @commands.command()
    async def weather(self, ctx, *, location=None):
        if location != None:
            try:
                location = '-'.join(location.split())
                response = requests.get('http://api.tanvis.xyz/weather/{}'.format(location))
                response = json.loads(response.content.decode('utf-8'))
                namee = response['name']
                celsiuse = response['celsius']
                farenheite = response['fahrenheit']
                weathere = response['weather']
                link = response['icon']
                windspeede = response['windSpeed']
                embed = discord.Embed(tile='Weather', description="Here's what i could find: ", color=random.randint(0, 16777215))
                embed.add_field(name='Location', value=namee)
                embed.add_field(name='Temp in Celsius', value=celsiuse)
                embed.add_field(name='Temp in Fahrenheit', value=farenheite)
                embed.add_field(name='Weather', value=weathere)
                embed.add_field(name='Wind Speed', value=windspeede)
                embed.set_thumbnail(url=link)
                await ctx.send(embed=embed)
                print('weather')
            except Exception:
                await ctx.send('Given location not found')

    @commands.command(name='pokemon', aliases=['poke'])
    async def pokemon(self, ctx, pokemon=None):
        if pokemon != None:
            try:
                response = requests.get('http://api.tanvis.xyz/pokedex/{}'.format(pokemon))
                response = json.loads(response.content.decode('utf-8'))
                name = response['name']
                num = response['number']
                image = response['image']
                species = response['species']
                height = response['height']
                weight = response['weight']
                check1 = response['types']
                types = ''
                for t in check1:
                    types += t + ' '
                types = ','.join(types.split())
                check2 = response['abilities']
                abilities = ''
                for t in check2:
                    abilities += t + ' '
                abilities = ','.join(abilities.split())
                des = response['description']
                ts = response['baseStats']['total']
                hp = response['baseStats']['hp']
                attack = response['baseStats']['attack']
                defense = response['baseStats']['defense']
                spAttack = response['baseStats']['spAttack']
                spDefense = response['baseStats']['spDefense']
                speed = response['baseStats']['speed']
                embed = discord.Embed(
                    title="{}'s info".format(name), desciption="Here's what i could find: ", color=random.randint(0, 16777215))
                embed.add_field(name='Pokedex Number', value=num)
                embed.add_field(name='Species', value=species)
                embed.add_field(name='Height', value=height)
                embed.add_field(name='Weight', value=weight)
                embed.add_field(name='Types', value=types)
                embed.add_field(name='Abilities', value=abilities)
                embed.add_field(name='Description', value=des)
                embed.add_field(name='Total Stats', value=ts)
                embed.add_field(name='Attack', value=attack)
                embed.add_field(name='Defense', value=defense)
                embed.add_field(name='Special Attack', value=spAttack)
                embed.add_field(name='Special Defense', value=spDefense)
                embed.add_field(name='Speed', value=speed)
                embed.set_image(url=image)
                await ctx.send(embed=embed)
            except Exception:
                await ctx.send('Given pokemon not found')
            print('pokemon')

    @commands.command(name='yt', aliases=['youtube', 'Youtube'])
    async def yt(self, ctx, *, query=None):
        if query != None:
            try:
                query = '-'.join(query.split())
                response = requests.get('http://api.tanvis.xyz/youtube/{}'.format(query))
                response = json.loads(response.content.decode('utf-8'))
                name1 = response[0]['name']
                image = response[0]['thumbnail']
                link1 = response[0]['link']
                name2 = response[1]['name']
                name3 = response[2]['name']
                link2 = response[1]['link']
                link3 = response[2]['link']
                embed = discord.Embed(title='YouTube', description="Here's what i could find", color=random.randint(0, 16777215))
                embed.add_field(name=name1, value=link1)
                embed.set_thumbnail(url=image)
                embed.add_field(name=name2, value=link2)
                embed.add_field(name=name3, value=link3)
                await ctx.send(embed=embed)
                print('yt')
            except Exception as e:
                await ctx.send(e)

    @commands.command(name='define', aliases=['def', 'dict', 'dictionary'])
    async def define(self, ctx, *, word=None):
        if word != None:
            try:
                r = requests.get('http://api.tanvis.xyz/dictionary/{}'.format(word))
                r = json.loads(r.content.decode('utf-8'))
                list1 = r['noun']
                embed = discord.Embed(title=word.title(), color=random.randint(0, 16777215))
                for i in range(len(list1)):
                    embed.add_field(name='\u200b', value=((str(i + 1) + '. ') + list1[i].title()) + '.')
                await ctx.send(embed=embed)
            except Exception:
                await ctx.send('Dear User, I could not find a definition for this word.')

    @commands.command()
    async def anime(self, ctx, *, query):
        try:
            creds = spice.init_auth('gauravgupta', 'gj111999@')
            test = spice.search(query, spice.get_medium('anime'), creds)
            list1 = ''
            count = 1
            for i in test:
                list1 += ((str(count) + '. ') + i.title) + '\n'
                count += 1
            if list1 != '':
                await ctx.send(('```\n' + list1) + '\n```')
                def check(p):
                    return p.author.id == ctx.author.id and p.channel == ctx.channel
                m = await self.bot.wait_for('message', check = check)
                m = int(m.content)
                m = m - 1
                try:
                    await ctx.channel.purge(limit=2)
                except Exception:
                    pass
                ids = test[m].id
                title = test[m].title
                episode = test[m].episodes
                score = float(test[m].score)
                typea = test[m].anime_type
                status = test[m].status
                date = test[m].dates
                date = list(date)
                syno1 = test[m].synopsis
                syno2 = syno1.replace('<br />', '')
                syno3 = syno2.replace('[Written by MAL Rewrite]', '')
                syno4 = syno3.replace('[i]', '')
                syno5 = syno4.replace('[/i]', '')
                syno = syno5.replace('&#039;', "'")
                link = test[m].image_url
                if (score >= 0) and (score < 2):
                    emoji = ':disappointed:'
                elif (score >= 2) and (score < 4):
                    emoji = ':grimacing:'
                elif (score >= 4) and (score < 6):
                    emoji = ':neutral_face:'
                elif (score >= 6) and (score < 9):
                    emoji = ':smiley:'
                elif score >= 9:
                    emoji = ':heart_eyes:'
                if status == 'Currently Airing':
                    embed = discord.Embed(title='{}'.format(title), color=random.randint(0, 16777215))
                    embed.add_field(name='Synopsis', value=syno)
                    embed.add_field(name='Type', value=typea)
                    embed.add_field(name='Episodes', value=episode, inline=True)
                    embed.add_field(name='Status', value=status)
                    embed.add_field(name='Started', value=date[0])
                    embed.add_field(name='Score', value=(str(score) + ' ') + emoji)
                    embed.set_thumbnail(url=link)
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title='{}'.format(title), color=random.randint(0, 16777215))
                    embed.add_field(name='Synopsis', value=syno)
                    embed.add_field(name='Type', value=typea)
                    embed.add_field(name='Episodes', value=episode, inline=True)
                    embed.add_field(name='Status', value=status)
                    embed.add_field(name='Started', value=date[0])
                    embed.add_field(name='Finished', value=date[1])
                    embed.add_field(name='Score', value=(str(score) + ' ') + emoji)
                    embed.set_thumbnail(url=link)
                    await ctx.send(embed=embed)
            else:
                await ctx.send('Given Anime not found')
        except Exception as e:
            await ctx.send('Service unavailable atm')
            print(e)

    @commands.command()
    async def manga(self, ctx, *, query):
        try:
            creds = spice.init_auth('gauravgupta', 'gj111999@')
            test = spice.search(query, spice.get_medium('manga'), creds)
            list1 = ''
            count = 1
            for i in test:
                list1 += ((str(count) + '. ') + i.title) + '\n'
                count += 1
            if list1 != '':
                await ctx.send(('```\n' + list1) + '\n```')
                def check(p):
                    return p.author.id == ctx.author.id and p.channel == ctx.channel
                m = await self.bot.wait_for('message', check = check)
                m = int(m.content)
                m = m - 1
                try:
                    await ctx.channel.purge(limit=2)
                except Exception:
                    pass
                ids = test[m].id
                title = test[m].title
                episode = test[m].chapters
                score = float(test[m].score)
                typea = test[m].manga_type
                status = test[m].status
                syno1 = test[m].synopsis
                syno2 = syno1.replace('<br />', '')
                syno3 = syno2.replace('[Written by MAL Rewrite]', '')
                syno4 = syno3.replace('[i]', '')
                syno5 = syno4.replace('[/i]', '')
                syno = syno5.replace('&#039;', "'")
                link = test[m].image_url
                if (score >= 0) and (score < 2):
                    emoji = ':disappointed:'
                elif (score >= 2) and (score < 4):
                    emoji = ':grimacing:'
                elif (score >= 4) and (score < 6):
                    emoji = ':neutral_face:'
                elif (score >= 6) and (score < 9):
                    emoji = ':smiley:'
                else:
                    emoji = ':heart_eyes:'
                embed = discord.Embed(title='{}'.format(title), color=random.randint(0, 16777215))
                embed.add_field(name='Synopsis', value=syno)
                embed.add_field(name='Type', value=typea)
                embed.add_field(name='Chapters', value=episode, inline=True)
                embed.add_field(name='Status', value=status)
                embed.add_field(name='Score', value=(str(score) + ' ') + emoji)
                embed.set_thumbnail(url=link)
                await ctx.send(embed=embed)
            else:
                await ctx.send('Given Manga not found')
        except Exception as e:
            await ctx.send('Service unavailable atm')
            print(e)

    @commands.command(name='lyrics', aliases=['lyric', 'lines'])
    async def lyrics(self, ctx, *, song):
        try:
            await ctx.send(':mag: Singer Name') 
            def check(m):
                return m.author.id == ctx.author.id and m.channel == ctx.channel
            singer = await self.bot.wait_for('message', check = check)
            singer = str(singer.content) 
            print(song, singer)  
            l = lyricwikia.get_lyrics(singer, song) 
            str1 = ''  
            ls = l.split('\n\n')  
            embed = discord.Embed(
                title='{}'.format(song.title()), color=random.randint(0, 16777215)
            ) 
            for a in ls:  
                embed.add_field(name='\u200b', value=a + '\n') 
            await ctx.send(embed=embed) 
        except Exception as e:  
            await ctx.send('Lyrics not available for this song. Are you sure you entered correct details?')
            print(e) 
def setup(bot):  
    bot.add_cog(QUERY(bot))
    print('Query is loaded') 
