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
        await ctx.send(":tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::tasokuva::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_: :2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_::2_:")            

    @commands.command()
    async def mine_tk(self, ctx):
        t = (":tasokuva:")
        k = (":2_:")
        await ctx.send(t , k)


def setup(client):
    client.add_cog(user(client))
