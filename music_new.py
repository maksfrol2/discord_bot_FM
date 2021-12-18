
import discord
from discord import message
from discord.ext.commands.core import command
import pafy
import random
from discord.ext import commands

class Player(commands.Cog): #инициализация класса
    def __init__(self, bot):
        self.bot = bot 

    async def play_song(self, ctx, song:str):
        url = pafy.new(song).getbestaudio().url
        ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url))) #Проигрывает аудио
        ctx.voice_client.source.volume = 1 #Громкость воспроизведения произведения

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None: #Проверяет, находится ли автор команды в голосовом канале
            return await ctx.send("Вы не находитесь в голосовом канале!")
        elif ctx.voice_client is not None: 
            await ctx.voice_client.disconnect()
        await ctx.author.voice.channel.connect()
        
    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client is not None: 
            await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, song):
        if ctx.author.voice is None: 
            return await ctx.send("Вы не находитесь в голосовом канале!")   
        await self.play_song(ctx, song)
        await ctx.send("Воспроизвожу")

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send('Музыка поставлена на паузу')

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send('Музыка снова проигрывается')

    @commands.command()
    async def rr(self,ctx):
        if ctx.author.voice is None: 
            return await ctx.send("Вы не находитесь в голосовом канале!")
        if random.randrange(6) == 1:  
            await self.play_song(ctx, 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            await ctx.send("Воспроизвожу")
        else:
            await ctx.send("Повезло, повезло")

    @commands.command()
    async def commands(self,ctx):
        embed=discord.Embed(title='Список команд')
        embed.add_field(name = '!play', value="Воспроизведение музыки по ссылке, укажите ссылку через пробел после команды", inline = True)
        embed.add_field(name = '!pause', value = "Пауза",inline=False)
        embed.add_field(name = '!resume', value = "Повторное воспроизведение", inline=False)
        embed.add_field(name = '!join', value = "Подключение к голосовому каналу", inline =False)
        embed.add_field(name = '!leave', value= "Отключение от голосового канала", inline = False)
        await ctx.send(embed=embed)