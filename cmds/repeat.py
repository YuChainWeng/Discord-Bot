import discord
from discord.ext import commands
from core.classes import Cog_Exension
import json

class repeat(Cog_Exension):
  @commands.command()
  async def repeat(self,ctx,*,msg):
    await ctx.message.delete()
    await ctx.send(msg)
  @commands.command()
  async def clear(self,ctx,num:int):
    await ctx.channel.purge(limit=num+1)
  
def setup(bot):
    bot.add_cog(repeat(bot))
