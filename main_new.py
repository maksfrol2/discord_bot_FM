import discord
from discord import player
from discord.ext import commands
from music_new import Player

intents = discord.Intents.default() #Устанавливает необходимый доступ
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents) #Задается командный префикс бота и права доступа

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready") #Сообщает об успешном запуске бота

async def setup(): #Первоначальная настройка
    await bot.wait_until_ready() 
    bot.add_cog(Player(bot)) 

bot.loop.create_task(setup())
bot.run('OTE3NDg2MjczOTkwNjUxOTE0.Ya5ZrQ.M7adMTwuoCdWh-9Jb_CqPymN8cc') #старт бота, в скобках указывается токен