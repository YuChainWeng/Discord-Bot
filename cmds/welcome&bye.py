import discord
from discord.ext import commands
from core.classes import Cog_Exension

class welcome(Cog_Exension):
  
  @commands.Cog.listener()
  async def on_member_join(self,member):
    channel = self.bot.get_chennel(977561547075379232)
    await channel.send(f'{member} join')


  @commands.Cog.listener()
  async def on_member_remove(self,member):
    channel = self.bot.get_chennel(977561547075379232)
    await channel.send(f'{member} leave :cry:')

def setup(bot):
  bot.add_cog(welcome(bot))