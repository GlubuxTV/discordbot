import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Der Bot ist bereit!')

@bot.command()
async def hallo(ctx):
    await ctx.send('Hallo!')

bot.run('MTA3NjU0MTUyMDI3NjExNTU0Ng.GeTiUi.jpXbC35NRlprxwNchvCEpWDIxVLFTfNOrpKr5s')
