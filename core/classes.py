import discord
import os
from discord.ext import commands



class Cog_Exension(commands.Cog):
  def __init__(self,bot):
    self.bot = bot