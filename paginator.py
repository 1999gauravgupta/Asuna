from discord.ext import commands
import asyncio
import discord
import random

async def paginate(bot,ctx,pages,title=None,description=None):
    color=random.randint(0, 16777215)
    valid=["\N{BLACK LEFT-POINTING TRIANGLE}","\N{BLACK RIGHT-POINTING TRIANGLE}"]
    length=len(pages)-1
    counter=0
    while True:
        cog=list(bot.get_cog_commands(name=pages[counter]))
        embed=discord.Embed(title=title if title else "\u200b",description=pages[counter],color=color)
        for i in cog:
            embed.add_field(name="\u200b",value=i.name,inline=False)
        final=await ctx.send(embed=embed)  
        await final.add_reaction("\N{BLACK LEFT-POINTING TRIANGLE}")
        await final.add_reaction("\N{BLACK RIGHT-POINTING TRIANGLE}")          
        reaction, user = await bot.wait_for('reaction_add', check=lambda r, u: u == ctx.author and r.emoji in valid and r.message.id == final.id)   
        if reaction.emoji=="\N{BLACK RIGHT-POINTING TRIANGLE}":
            await final.delete()
            counter+=1
            if counter>length:              
                await ctx.send("You reached end")
                break         
        elif reaction.emoji=="\N{BLACK LEFT-POINTING TRIANGLE}":
            await final.delete()
            counter-=1
            if counter<0:
                await ctx.send("Nothing to show there")
                break
           
            
