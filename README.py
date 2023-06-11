import os
import discord
from discord.ext import commands
from random import choice

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def mem(ctx):
    image_name = choice(os.listdir('images'))
    with open(f'images/{image_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)


bot.run('MTEwOTg0NjkzMDY1NTI4OTM0NA.G_vz80.2njblC26JKFmOVdIBNjv6NeW2yzYn-6Cu9CIrI')
