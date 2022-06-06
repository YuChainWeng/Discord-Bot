import discord
import os
from discord.ext import commands
from core.classes import Cog_Exension
import json

class onreaction(Cog_Exension):
  
  @commands.Cog.listener()
  async def on_raw_reaction_add(self,data):
    if data.channel_id != 977554852886499378:
      return
  
    if str(data.emoji) == '🎮':
      guild = self.bot.get_guild(903580391737294868) #給定sever id for 505
      role = guild.get_role(977552448631763006)    #給定role id
      await data.member.add_roles(role)

def setup(bot):
  bot.add_cog(onreaction(bot))