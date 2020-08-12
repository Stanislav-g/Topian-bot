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

    
    #search
    @commands.command()
    async def search(ctx, *, question = None): 
        # сам сайт
        if question == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Search',value = '**=search** - search (text)')
            await ctx.send( embed = embw )
        url = 'https://www.bing.com/search?q=' + str(question).replace(' ', '+')
        await ctx.send(f'Кое кто не умеет пользоваться поисковиками , я сделал это за него.\n{url}')

    #youtube_search
    @commands.command()
    async def youtube_search(ctx, *, question = None): 
        # сам сайт
        if question == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'YouTube',value = '**=youtube_search** - youtube_search (text)')
            await ctx.send( embed = embw )
        url = 'https://www.youtube.com/results?search_query=' + str(question).replace(' ', '+')
        await ctx.send(f'Так как кое кто не умеет ютубить , я сделал это за него.\n{url}')

    #yandex
    @commands.command()
    async def yandex(ctx, *, question):  # пояндексить
        # сам сайт
        if question == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Yandex',value = '**=yandex** - yandex (text)')
            await ctx.send( embed = embw )
        url = 'https://yandex.ua/search/?lr=142&text=' + str(question).replace(' ', '%20')
        await ctx.send(f'Так как кое кто не умеет яндексить , я сделал это за него.\n{url}')

 

    #wiki
   @commands.command(pass_context = True,aliases=['вики']) #!!wiki  !!вики
    async def wiki( ctx,*, amount: str):

        if amount == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'WIKI',value = '**=wiki** - wiki (text)')
            await ctx.send( embed = embw )
        a = '_'.join(amount.split())
        await ctx.send(f'https://ru.wikipedia.org/wiki/{a}')


  
    #google
    @commands.command()
    async def google(ctx, *, question):  # погуглить
        # сам сайт
        if question == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Google',value = '**=google** - google (text)')
            await ctx.send( embed = embw )
        url = 'https://google.gik-team.com/?q=' + str(question).replace(' ', '+')
        await ctx.send(f'Так как кое кто не умеет гуглить , я сделал это за него.\n{url}')




def setup(client):
client.add_cog(user(client))
