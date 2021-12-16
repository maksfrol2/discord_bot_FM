
import discord
from discord.ext.commands.core import command
import pafy
from discord.ext import commands

class Player(commands.Cog): #инициализация класса
    def __init__(self, bot):
        self.bot = bot 

    async def play_song(self, ctx, song):
        url = pafy.new(song).getbestaudio().url
        ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)))
        ctx.voice_client.source.volume = 1

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None: 
            return await ctx.send("Nope")
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
            return await ctx.send("Nope")

        await ctx.author.voice.channel.connect()    

        await self.play_song(ctx, song)
        await ctx.send("playing")

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send('paused')

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send('resumed')