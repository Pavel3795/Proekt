import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Всегда следи за природой, не загрязняй её и не позволяй это делать кому то))). 😉')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("MTEwOTg0NjkzMDY1NTI4OTM0NA.GKfiEu.EgOY7c5ofX6YP3V_qcMaFDsqoXMez4IoiJJX-Y")
