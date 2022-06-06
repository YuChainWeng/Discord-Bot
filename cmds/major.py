import discord
from discord.ext import commands
from core.classes import Cog_Exension
import json
class major(Cog_Exension):
  
  @commands.command()
  async def ping(self,ctx):
    await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

  
def setup(bot):
    bot.add_cog(major(bot))
