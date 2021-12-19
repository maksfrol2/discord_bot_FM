import discord
from discord.ext import commands
from music import Player
import token
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    '''При вызове функция выводит сообщение о готовности бота'''
    print(f"{bot.user.name} is ready")

async def setup():
    '''Начальная настройка'''
    await bot.wait_until_ready() 
    bot.add_cog(Player(bot)) 

token_file = open('token.txt', 'r')
token = token_file.read()

bot.loop.create_task(setup())
bot.run(str(token)) # в скобках указывается токен