import discord
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.cog import Cog
import music
import pytest
import unittest.mock
import asyncio
import pytest_asyncio

@pytest.fixture
def player():
    import music
    return music.Player(commands.Cog)

@pytest.mark.asyncio
async def test_join():
    ctx = unittest.mock.Mock()
    player = music.Player
    player.join = unittest.mock.AsyncMock()
    await music.Player.join(player,ctx)
    assert ctx.voice_client.is_connected() == True

@pytest.mark.asyncio
async def test_leave(player):
    ctx = unittest.mock.Mock()
    player.leave = unittest.mock.AsyncMock()
    await player.leave(player,ctx)
    assert ctx.voice_client.is_connected() == False

@pytest.mark.asyncio
async def test_pause(player):
    ctx = unittest.mock.Mock()
    ctx.author.voice.channel.connect = unittest.mock.AsyncMock()
    await player.pause(player,ctx)
    assert ctx.voice_client.is_playing() is True

@pytest.mark.asyncio
async def test_commands():
    ctx = unittest.mock.Mock
    ctx.author.id = 5
    ctx.send = unittest.mock.AsyncMock()
    player = music.Player
    await player.commands(player,ctx)
    ctx.send.assert_called()
    a = ctx.send.call_args.args[0]
    assert a.embed.title =='Список команд'

if __name__ == '__main__':
    pytest.main()