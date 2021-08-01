import discord
import discord
from discord.ext import commands
from asyncio import sleep
from discord.utils import get

token = 'a token'
bot = commands.Bot(command_prefix='%')
client = discord.Client()

@bot.command()
async def boom(ctx, arg):
    ctx.message.delete()
    booms = 0
    while arg >= int(booms):
        ctx.send('BOOM BOOM BAKUDAN! ||@everyone||')
        booms += 1
