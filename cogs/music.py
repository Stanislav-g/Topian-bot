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
                
    @commands.command()
    async def mine(self, ctx):
        await ctx.send("🟫\n🟫🟫\n🟫🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫\n🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️")            

    @commands.command()
    async def mine_tk(self, ctx):
        t = ("🟫")
        k = (":2_:")
        await ctx.send(t)
    @commands.command()
    async def message_edit(self, ctx , * , arg, id:int):
        message = await ctx.message.channel.fetch_message(id)
        await message.edit(arg)

def setup(client):
    client.add_cog(user(client))
