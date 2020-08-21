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

    #info
    @commands.command()
    async def help(self, ctx ):
        await ctx.channel.purge( limit = 1 )
        emb = discord.Embed( title = '**Moderation**', colour= 0x808080)
        emb.add_field( name = 'Commands',value = '**=clear** - clear (количество) или clear (пользователь)(количество)\n**=ban** - ban @user\n **=unban** - unban @user\n **=kick** - kick @user\n **=emoji** - emoji (message id) (emoji)\n**-tempban** - tempban @user *s* or *m* or *h* or *d*\n**=temp_add_role** - temp_add_role (time) @user @role\n **=add_role** - add_role @user @role\n**=channel_create** - channel_create (name)\n**=voice_create** - voice_create (name)\n**=suggest** - suggest (text)\n**=changing_name** - changing_name @user\n**=text** - text (arg)')
        await ctx.author.send( embed = emb )
        embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
        embw.add_field( name = 'Commands',value = '**=userinfo** - userinfo @user\n**=botinfo**\n**=serverinfo**\n**=avatar** - avatar или avatar @user\n**=ping** - ping\n**=user_boost** - user_ boost @user\n')
        await ctx.author.send( embed = embw )
        embw = discord.Embed( title = '**Search**', colour= 0x808080)
        embw.add_field( name = 'Commands',value = '**=search** - search (запрос)\n**=youtube_search** - youtube_search (запрос)\n**=yandex** - yandex (запрос)\n**=wiki** - wiki (запрос)\n**=google** - google (запрос)\n')
        await ctx.author.send( embed = embw )
        embw = discord.Embed( title = '**Games**', colour = discord.Color.green())
        embw.add_field( name = 'Commands',value = '**=rps** - rps (камень, ножницы или бумага)\n**=guess** - guess\n**=coinflip** - coinflip\n**=knb** - knb @user\n')
        await ctx.author.send( embed = embw )

    @commands.command()
    async def log(self, ctx, num : int = None, member: discord.Member = None ):
        guild = ctx.message.guild
        if member == None:
            async for entry in guild.audit_logs(limit= num):
                emb = discord.Embed( title = 'Logs', colour = discord.Color.red() )
                emb.add_field( name = 'logs',value = '**{0.user}** did {0.action} to **{0.target}** *{0.before}* to *{0.after}*'.format(entry))
                await ctx.send( embed = emb )
        else:
            entries = await guild.audit_logs(limit=None, user=guild.me).flatten()
            await ctx.send('I made {} moderation actions.'.format(len(entries)))
    

    text = ['']    
    @commands.command()
    @commands.has_permissions( administrator = True )
    async def rew(self, ctx , * , arg = None):
            global text
            await ctx.channel.purge( limit = 1 ) 
            text = text + arg
            await ctx.send(f" {arg} ") 
            await ctx.send(f"{text}")
            await ctx.message.add_reaction('👍')

    channell = ['']  
    @commands.command()
    async def start_emoji(self, ctx):
        global channell
        channell = client.get_channel(id)
        await ctx.send(channell)

    channell = ['']          
    @commands.Cog.listener
    async def on_message ( message ):
        global channell
        textchannel = client.get_channel(id)
        if textchannel == channell:
            emj = str('👍')
            await message.add_reaction(emj)
            emji = str('👎')
            await message.add_reaction(emji)

    @commands.Cog.listener
    async def on_guild_join( guild ):


        me = client.get_user(550061958938886175)

        emb = discord.Embed( title = f'Я пришел на новый сервер!' )
        for guild in client.guilds:
            category = guild.categories[0]
            try:
                channel = category.text_channels[0]
            except:
                channel = category.voice_channels[0]
            link = await channel.create_invite()
        emb.add_field( name = guild.name, value = f"Участников: {len(guild.members)}\nСсылка: {link}" )


        await me.send( embed = emb )
            
def setup(client):
    client.add_cog(user(client))
