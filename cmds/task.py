import discord
from discord.ext import commands
from core.classes import Cog_Exension
import asyncio,datetime
import json

class task(Cog_Exension):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    
    async def time_task():
      await self.bot.wait_until_ready()
      print(1)
      self.channel = self.bot.get_channel(977561547075379232)
      while not self.bot.is_closed():
        await self.channel.send("Hi i'm runing")
        await asyncio.sleep(3600)

    self.bg_task=self.bot.loop.create_task(time_task())
    
  @commands.command()
  async def set_channel(self,ctx,ch:int):
    self.channel = self.bot.get_channel(ch)
    await ctx.send(f'Set Channel:{self.channel.mention}')

  

def setup(bot):
  bot.add_cog(task(bot))