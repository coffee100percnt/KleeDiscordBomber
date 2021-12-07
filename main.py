import discord
from discord.ext import commands
import time

token = 'a token'
bot = commands.Bot(command_prefix='%')
guild = discord.Guild

@bot.command()
async def boom(ctx, arg=10):
    await ctx.message.delete()
    
    for i in range(0, arg):
        await ctx.send('BOOM! ||@everyone||')
        time.sleep(0.5)

@bot.command()
async def bang_roles(ctx, arg=10):
    await ctx.message.delete()

    for i in range(0, arg):
        await guild.create_role(name='BOOM!')
        time.sleep(0.5)

@bot.command()
async def bang_channels(ctx, arg=10):
    await ctx.message.delete()
    for i in range(0, arg):
        await guild.create_text_channel(name="BOOM!")
        time.sleep(0.5)


@bot.command()
async def bigbang(ctx):
    await ctx.message.delete()
    for i in range(0, 250):
        await ctx.guild.create_text_channel(name="BOOM!")
        await ctx.send("@everyone")
        await ctx.guild.create_role(name="BOOM!")
        time.sleep(0.5)

bot.run(token)
