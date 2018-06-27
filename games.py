from discord.ext import commands
import asyncio
import discord
import requests
import json
import string

class GAMES:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True,name="bj",aliases=["blackjack"])
    async def bj(self,ctx,bat,user: discord.Member=None):
        if user==None:
            user=ctx.message.author
        bal=int(bat)
        d_valuea=[]
        fc=["KING","QUEEN","JACK"]
        for i in range(3):
            if bal<0:
                await self.bot.say("The game terminated because your balance dipped below zero")
                break
            await self.bot.say("Round {}".format(i+1))
            await self.bot.say("Betting Amount: ")
            bet =await self.bot.wait_for_message(author=ctx.message.author)
            bet=int(bet.content)
            if bet>bal:
                await self.bot.say("You cannot bet more than {} so resetting your bet value to {}".format(bal,bal))
                bet=startf
            r=requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
            r= json.loads(r.content.decode('utf-8'))
            deck=r["deck_id"]
            draw=requests.get("https://deckofcardsapi.com/api/deck/{}/draw/?count=2".format(deck))
            draw= json.loads(draw.content.decode('utf-8'))
            u_value=0
            u_cards=[]
            d_cards=[]
            for j in range(2):
                if draw["cards"][j]["value"] in fc:
                    u_value+=10
                elif draw["cards"][j]["value"]=="ACE":
                    u_value+=11
                else:
                    u_value+=int(draw["cards"][j]["value"])
                u_cards.append(draw["cards"][j]["code"])
            d_value=0
            draw=requests.get("https://deckofcardsapi.com/api/deck/{}/draw/?count=1".format(deck))
            draw= json.loads(draw.content.decode('utf-8'))
            if draw["cards"][0]["value"] in fc:
                d_value+=10
            elif draw["cards"][0]["value"]=="ACE":
                d_value+=11
            else:
                d_value+=int(draw["cards"][0]["value"])
            d_cards.append(draw["cards"][0]["code"])
            d_valuea.append(d_value) 
            q=""
            w=""
            for a in u_cards:
                q+=(a+" ")
            for b in d_cards:
                w+=(b+" ")
            embed=discord.Embed(title="Blackjack",color=0xf7d28c)  
            embed.add_field(name="Betting Amount",value=bet)
            embed.add_field (name="User Cards",value=q)
            embed.add_field(name="Dealer Cards",value=w)
            embed.add_field(name="User Cards value",value=u_value)
            embed.add_field(name="Dealer Cards value",value=d_value,inline=True)
            embed.add_field(name="\u200b",value="Hit/Stand/Double Down")
            await self.bot.say(embed=embed)
            # print(u_value,d_value)
            option =await self.bot.wait_for_message(author=ctx.message.author)
            option=str(option.content)
            if option.lower()=="hit":
                draw=requests.get("https://deckofcardsapi.com/api/deck/{}/draw/?count=1".format(deck))
                draw= json.loads(draw.content.decode('utf-8'))
                if draw["cards"][0]["value"] in fc:
                    u_value+=10
                elif draw["cards"][0]["value"]=="ACE":
                    u_value+=11
                else:
                    u_value+=int(draw["cards"][0]["value"])
                u_cards.append(draw["cards"][0]["code"])
            elif option.lower()=="double down":
                bet=bet*2
                draw=requests.get("https://deckofcardsapi.com/api/deck/{}/draw/?count=1".format(deck))
                draw= json.loads(draw.content.decode('utf-8'))
                if draw["cards"][0]["value"] in fc:
                    u_value+=10
                elif draw["cards"][0]["value"]=="ACE":
                    u_value+=11
                else:
                    u_value+=int(draw["cards"][0]["value"])
                u_cards.append(draw["cards"][0]["code"])
            else:
                bet=bet
            draw=requests.get("https://deckofcardsapi.com/api/deck/{}/draw/?count=2".format(deck))
            draw= json.loads(draw.content.decode('utf-8'))
            for k in range(2):
                if draw["cards"][k]["value"] in fc:
                    d_value+=10
                elif draw["cards"][k]["value"]=="ACE":
                    d_value+=11
                else:
                    d_value+=int(draw["cards"][k]["value"])
                d_valuea.append(d_value)
                d_cards.append(draw["cards"][k]["code"])
            for i in d_valuea:
                if i<=21:
                    d_value=i
            try:
                mgs = []
                async for x in self.bot.logs_from(ctx.message.channel, limit = 2):
                    mgs.append(x)
                await self.bot.delete_messages(mgs)
            except:
                pass
        # print(u_value,d_value)
            if u_value>21:
                bal=bal-bet
                q=""
                w=""
                for a in u_cards:
                    q+=(a+" ")
                for b in d_cards:
                    w+=(b+" ")
                embed=discord.Embed(title="Blackjack",color=0xf23c3c)  
                embed.add_field(name="Betting Amount",value=bet)
                embed.add_field (name="User Cards",value=q)
                embed.add_field(name="Dealer Cards",value=w)
                embed.add_field(name="\u200b",value="Bust of {}".format(bet))
                await self.bot.say(embed=embed)
            elif u_value<=21 and u_value>=d_value:
                bal+=bet*2
                q=""
                w=""
                for a in u_cards:
                    q+=(a+" ")
                for b in d_cards:
                    w+=(b+" ")
                embed=discord.Embed(title="Blackjack",color=0x3cf279)  
                embed.add_field(name="Betting Amount",value=bet)
                embed.add_field (name="User Cards",value=q)
                embed.add_field(name="Dealer Cards",value=w)
                embed.add_field(name="\u200b",value="You won {}".format(bet*2))
                await self.bot.say(embed=embed)
            else:
                bal=bal-bet
                q=""
                w=""
                for a in u_cards:
                    q+=(a+" ")
                for b in d_cards:
                    w+=(b+" ")
                embed=discord.Embed(title="Blackjack",color=0xf23c3c)  
                embed.add_field(name="Betting Amount",value=bet)
                embed.add_field (name="User Cards",value=q)
                embed.add_field(name="Dealer Cards",value=w)
                embed.add_field(name="\u200b",value="Bust of {}".format(bet))
                await self.bot.say(embed=embed)
            if i>0:
                try:
                    mgs = []
                    async for x in self.bot.logs_from(ctx.message.channel, limit = 2):
                        mgs.append(x)
                    await self.bot.delete_messages(mgs)
                except:
                    pass
        embed=discord.Embed(title="Blackjack",color=0xf7d28c)  
        embed.add_field(name="\u200b",value="Credits at end of game: {}".format(bal-int(bat)*1.5))
        await self.bot.say(embed=embed)
        with open("bjlb.txt", "a") as f1:
            f1.write("\n"+str(user)+" "+str(bal-int(bat)*1.5)+"\n")

    @commands.command(pass_context=True,name="lb",aliases=["leaderboard"])
    async def lb(self,ctx):
        with open("bjlb.txt", "r") as f1:
            list1=f1.readlines()
            if len(list1>10):
                limit=11
            else:
                limit=len(list1)+1
            p="```"
            for i in range(1,limit):
                a=f1.readline()
                p+=a+"\n"
            p+="```"
            await self.bot.say(p)   
        
def setup(bot):
    bot.add_cog(GAMES(bot))
    print("Games is loaded")
