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
import typing 

class user(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def example(self,ctx):
        await ctx.send("work")
    
    

    
    @commands.command(aliases = ['clear', 'c'])
    @commands.has_permissions(manage_messages = True)
    async def __clear(self, ctx, member: typing.Optional[discord.Member], amount : int):
                await ctx.message.delete()

                if member == None:
                    await ctx.channel.purge(limit = amount)
                elif member != None and member in ctx.guild.members:
                    number = 0
                    def predicate(message):
                        return message.author == member
                    async for elem in ctx.channel.history().filter(predicate):
                        await elem.delete()
                        number += 1
                        if number >= amount:
                            break


def setup(client):
    client.add_cog(user(client))
