import discord
from discord.ext import commands
import os
import json
import keep_alive

bot = commands.Bot(command_prefix='/$')

@bot.event
async def on_ready():
  print('We have log in as {0.user}'.format(bot))



@bot.command()
async def load(ctx,extension):
  bot.load_extension(f'cmds.{extension}')
  await ctx.send(f'loded {extension} done.')


@bot.command()
async def unload(ctx,extension):
  bot.unload_extension(f'cmds.{extension}')
  await ctx.send(f'unloded {extension} done.')


@bot.command()
async def reload(ctx,extension):
  bot.reload_extension(f'cmds.{extension}')
  await ctx.send(f'reloded {extension} done.')
  
for filesname in os.listdir('./cmds'):
  if filesname.endswith('.py'):
    bot.load_extension(f'cmds.{filesname[:-3]}')


if __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run(os.getenv('Key'))


