import discord
from discord.ext import commands
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name='Smart Realm Official Bot'))

    @bot.command()
    async def ping(ctx):
        await ctx.send('Pong!')

        bot.run(os.getenv('DISCORD_TOKEN'))
