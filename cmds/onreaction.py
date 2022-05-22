import discord
import os
from discord.ext import commands
from core.classes import Cog_Exension

class onreaction(Cog_Exension):
  
  @commands.Cog.listener()
  async def on_raw_reaction_add(self,payload):
    print(1)
    if self.payload.channel_id != int(os.getenv('testchannel')):
      return
  
    if str(self.payload.emoji) == '🎮':
      guild = self.bot.get_guild(int(os.getenv('testguild'))) #給定sever id for 505
      role = guild.get_role(int(os.getenv('testrole')))    #給定role id
      await self.payload.member.add_roles(role)

def setup(bot):
  bot.add_cog(onreaction(bot))