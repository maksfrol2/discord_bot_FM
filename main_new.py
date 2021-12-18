import discord
from discord.ext import commands
from music_new import Player

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

bot.loop.create_task(setup())
bot.run('OTE3NDg2MjczOTkwNjUxOTE0.Ya5ZrQ.M7adMTwuoCdWh-9Jb_CqPymN8cc') # в скобках указывается токен