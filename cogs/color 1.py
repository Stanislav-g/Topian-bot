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

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        
        global ev_player
        if str(payload.emoji) == '🟧': # Emoji для реакций
            ev_player = '2'
        else:
            ev_player = '0'



def setup(client):
    client.add_cog(user(client))
