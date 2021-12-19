import discord
from discord.ext.commands.core import command
import pafy
import random
from discord.ext import commands

class Player(commands.Cog):
    '''Класс, содержащий в себе все функции, необходимые для работы музыукального бота'''
    def __init__(self, bot):
        self.bot = bot 

    async def play_song(self, ctx: commands.Context, song:str):
        '''Функция ответственная за проигрывание музыки.
        Принимает на вход контекст и строку с url ссылкой'''
        url = pafy.new(song).getbestaudio().url
        ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)))
        ctx.voice_client.source.volume = 1 #Громкость воспроизведения

    @commands.command()
    async def join(self, ctx:commands.Context):
        '''При вызове подключает бота в голосовой канал к пользователю, который отправил команду.
        Принимает на вход контекст'''
        if ctx.author.voice is None:
            return await ctx.send("Вы не находитесь в голосовом канале!")
        elif ctx.voice_client is not None and ctx.voice_client.channel != ctx.author.voice.channel:
            await ctx.voice_client.disconnect()
        await ctx.author.voice.channel.connect()
        print(type(ctx.voice_client))
        
    @commands.command()
    async def leave(self, ctx:commands.Context):
        '''При вызове отключается от голосового канала
        Принимает на вход контекст'''
        if ctx.voice_client is not None: 
            await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx:commands.Context, song : str):
        '''При вызове начинает проигрывать музыку.
        Если бот заранее не был добавлен, то он подключится
        Принимает на вход контекст.'''
        if ctx.author.voice is None: 
            return await ctx.send("Вы не находитесь в голосовом канале!")
        if ctx.voice_client is not None and ctx.voice_client.channel == ctx.author.voice.channel:
            embed=discord.Embed(title='Воспроизведение')
            await ctx.send(embed=embed)
            await self.play_song(ctx, song)
        else:
            await ctx.author.voice.channel.connect()
            await self.play(ctx,song)

    @commands.command()
    async def reset(self, ctx:commands.Context):
        '''При вызове бот перезаходит в текущий голосовой канал.
        Принимает на вход контекст'''
        if ctx.author.voice is None:
            return await ctx.send("Вы не находитесь в голосовом канале!")
        elif ctx.voice_client is not None and ctx.voice_client.channel == ctx.author.voice.channel:
            await ctx.voice_client.disconnect()
            await ctx.author.voice.channel.connect()

    @commands.command()
    async def pause(self, ctx:commands.Context):
        '''Ставит на паузу. Вполне очевидно.
        Принимает на вход контекст
        '''
        embed=discord.Embed(title='Пауза')
        await ctx.send(embed=embed)
        await ctx.voice_client.pause()

    @commands.command()
    async def resume(self, ctx:commands.Context):
        '''Возобновляет воспроизведение.
        Принимает на вход контекст'''
        embed=discord.Embed(title='Воспроизведение')
        await ctx.send(embed=embed)
        await ctx.voice_client.resume()
        
    @commands.command()
    async def rr(self,ctx:commands.Context):
        '''При вызове с вероятностью 1 к 6 может начать проигрывать одну
        надоедливую песню из 1987 года.
        Принимает на вход контекст'''
        if ctx.author.voice is None: 
            return await ctx.send("Вы не находитесь в голосовом канале!")
        if random.randrange(6) == 1:  
            await self.play_song(ctx, 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            await ctx.send("Повезло, повезло")
        else:
            await ctx.send("Nope")

    @commands.command()
    async def commands(self,ctx:commands.Context):
        '''При вызове выдает список всех доступных команд
        Принимает на вход контекст'''
        embed=discord.Embed(title='Список команд')
        embed.add_field(name = '!play', value="Воспроизведение музыки по ссылке, укажите ссылку через пробел после команды", inline = True)
        embed.add_field(name = '!pause', value = "Пауза",inline=False)
        embed.add_field(name = '!resume', value = "Повторное воспроизведение", inline=False)
        embed.add_field(name = '!reset', value = "Сброс текущей песни", inline=False)
        embed.add_field(name = '!join', value = "Подключение к голосовому каналу", inline =False)
        embed.add_field(name = '!leave', value= "Отключение от голосового канала", inline = False)
        embed.add_field(name = '!rr', value = "Русская рулетка", inline =False)
        await ctx.send(embed=embed)