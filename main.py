import discord
import discord
from discord.ext import commands
from asyncio import sleep
from discord.utils import get

token = 'a token'
bot = commands.Bot(command_prefix='%')
guild = discord.Guild

@bot.command()
async def boom(ctx, arg=10):
    await ctx.message.delete()
    booms = 0
    while booms <= int(arg):
        await ctx.send('BOOM BOOM BAKUDAN! ||@everyone||')
        booms += 1
    booms = 0

@bot.command()
async def bang_roles(ctx, arg=10):
    await ctx.message.delete()
    bangs = 0
    while bangs <= int(arg):
        await guild.add_role(name='Boing, boing, boom!')
        bangs += 1
    bangs = 0

@bot.command()
async def bang_channels(ctx, arg=10):
    await ctx.message.delete()
    bangs = 0
    while bangs <= int(arg):
        await guild.add_channel(name="Sparks \'n\'Splash!")
        bangs += 1
bangs = 0

@bot.command()
async def bigbang(ctx):
    await ctx.message.delete()
    bigbangs = 0
    while 400 >= bigbangs:
        await guild.create_text_channel(name="BOOM!")
        await ctx.send("@everyone")
        await guild.create_role(name="BOOM!")
        bigbangs += 1
    bigbangs = 0

bot.run(token)
