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
    async def helphelp(self, ctx ):
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
        embw = discord.Embed( title = '**Other**', colour = discord.Color.green())
        embw.add_field( name = 'Commands',value = '**=num** - num рандомная цифра от 1 до 100\n**=wordnum** - wordnum (text)\n**=slapperson** - slapperson @user\n**=emoji_random** - emoji_random\n**=math** - math (arg) (+-*/) (arg)\n**=covid** - covid\n**=ball** - ball\n**=link** - link (url)\n**=kiss** - kiss @user' )
        await ctx.author.send( embed = embw )

        
    @commands.command(pass_context = True)
    async def help(self, ctx):
        await ctx.channel.purge(limit = 1)
        emb = discord.Embed( 
            title = 'Навигация по командам :clipboard:',
            color = 0x7aa13d
         )

        emb.add_field( name = '__**Moderation**__', value = '''
            **=clear** - clear (количество) или clear (пользователь)(количество)
            **=ban** - ban @user 
            **=unban** - unban @user
            **=kick** - kick @user
            **=emoji** - emoji (message id) (emoji)
            **-tempban** - tempban @user *s* or *m* or *h* or *d*
            **=temp_add_role** - temp_add_role (time) @user @role
            **=add_role** - add_role @user @role
            **=channel_create** - channel_create (name)
            **=voice_create** - voice_create (name)
            **=suggest** - suggest (text)
            **=changing_name** - changing_name @user
            **=text** - text (arg)
            **=image** - image (image)
             
            ''' )
        emb.add_field( name = '__**Info**__', value = '''
            **=userinfo** - userinfo @user
            **=botinfo**
            **=serverinfo**
            **=avatar** - avatar или avatar @user
            **=ping** - ping
            **=user_boost** - user_ boost @user
            **=info_emoji** - info_emoji (emoji)
            ''' )
        emb.add_field( name = '__**Search**__', value = '''
            **=search** - search (запрос)
            **=youtube_search** - youtube_search (запрос)
            **=yandex** - yandex (запрос)
            **=wiki** - wiki (запрос)
            **=google** - google (запрос)
            ''' )
        emb.add_field( name = '__**Games**__', value = '''
            **=rps** - rps (камень, ножницы или бумага)
            **=угадайка** - угадайка
            **=coinflip** - coinflip
            **=knb** - knb @user\n
            ''' )
        emb.add_field( name = '__**Other**__', value = '''
            **=num** - num рандомная цифра от 1 до 100
            **=wordnum** - wordnum (text)
            **=slapperson** - slapperson @user
            **=emoji_random** - emoji_random
            **=math** - math (arg) (+-*/) (arg)
            **=covid** - covid
            **=ball** - ball
            **=link** - link (url)
            **=kiss** - kiss @user
            **=reverse** - reverse (text)
            ''' )
        await ctx.author.send(embed = emb)        
        
      
    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
	embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**A new role was created**\n{role.mention}')
	embed.set_author(name=role.guild.name, icon_url=str(role.guild.icon_url))
	embed.set_footer(text=f"Role ID: {role.id}")
	await ctx.send(embed=embed)    
			
    @commands.command()
    @commands.has_permissions( administrator = True )
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
    


  


            
def setup(client):
    client.add_cog(user(client))
