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

            global start_ev
            if str(payload.emoji) == '🟥': # Emoji для реакций
                start_ev = '2'
            else:
                start_ev = '0'     


def setup(client):
    client.add_cog(user(client))
