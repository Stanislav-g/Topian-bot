import discord
from discord.ext import commands
import datetime
from discord.utils import get
import asyncio
from time import sleep
from colorsys import hls_to_rgb
import os
import random
from random import randint, choice, choices
import io
import sqlite3
import random as r

class user(commands.Cog):

    def __init__(self, client):
        self.client = client
            
    #join to channel
    @commands.command()
    async def join(self, ctx):
        global voise
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            await ctx.send(f'Бот присоеденился к каналу: {channel}')

    #leave from channel
    @commands.command()
    async def leave(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
        else:
            voice = await channel.connect()
            await ctx.send(f'Бот отключился от канала: {channel}')



def setup(client):
    client.add_cog(user(client))
