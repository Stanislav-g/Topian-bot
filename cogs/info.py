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

    

    #ip_info
   @commands.command()
    async def ip_info(self, ctx, arg ):
        await ctx.channel.purge(limit = 1)
        response = requests.get( f'http://ipinfo.io/{ arg }/json' )
        user_ip = response.json()[ 'ip' ]
        user_city = response.json()[ 'city' ]
        user_region = response.json()[ 'region' ]
        user_country = response.json()[ 'country' ]
        user_location = response.json()[ 'loc' ]
        user_org = response.json()[ 'org' ]
        user_timezone = response.json()[ 'timezone' ]
        global all_info
        all_info = f'```\n<INFO>\nIP : { user_ip }\nCity : { user_city }\nRegion : { user_region }\nCountry : { user_country }\nLocation : { user_location }\nOrganization : { user_org }\nTime zone : { user_timezone }```'
        await ctx.author.send( all_info )
        await ctx.send( '``` Информация отправлена в личные сообщения!```' )

    @commands.command()
    async def serverinfo(self, ctx):
        await ctx.channel.purge( limit = 1 )
        members = ctx.guild.members
        online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
        offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
        idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
        dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
        allchannels = len(ctx.guild.channels)
        allvoice = len(ctx.guild.voice_channels)
        alltext = len(ctx.guild.text_channels)
        allroles = len(ctx.guild.roles)
        embed = discord.Embed(title=f"{ctx.guild.name}", color=0xff0000, timestamp=ctx.message.created_at)
        embed.description=(
            f":timer: Сервер создали **{ctx.guild.created_at.strftime('%A, %b %#d %Y')}**\n\n"
            f":flag_white: Регион **{ctx.guild.region}\n\nГлава сервера **{ctx.guild.owner}**\n\n"
            f":tools: Ботов на сервере: **{len([m for m in members if m.bot])}**\n\n"
            f":green_circle: Онлайн: **{online}**\n\n"
            f":black_circle: Оффлайн: **{offline}**\n\n"
            f":yellow_circle: Отошли: **{idle}**\n\n"
            f":red_circle: Не трогать: **{dnd}**\n\n"
            f":shield: Уровень верификации: **{ctx.guild.verification_level}**\n\n"
            f":musical_keyboard: Всего каналов: **{allchannels}**\n\n"
            f":loud_sound: Голосовых каналов: **{allvoice}**\n\n"
            f":keyboard: Текстовых каналов: **{alltext}**\n\n"
            f":briefcase: Всего ролей: **{allroles}**\n\n"
            f":slight_smile: Людей на сервере **{ctx.guild.member_count}\n\n"
        )

        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f"ID: {ctx.guild.id}")
        embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
        await ctx.send(embed=embed)
    # userinfo
    @commands.command()
    async def userinfo(self, ctx, Member: discord.Member = None ):
        await ctx.channel.purge( limit = 1 )
        if not Member:
            Member = ctx.author
        roles = (role for role in Member.roles )
        emb = discord.Embed(title='Информация о пользователе.'.format(Member.name), description=f"Участник зашёл на сервер: {Member.joined_at.strftime('%b %#d, %Y')}\n\n "
                                                                                          f"Имя: {Member.name}\n\n"
                                                                                          f"Никнейм: {Member.nick}\n\n"
                                                                                          f"Статус: {Member.status}\n\n"
                                                                                          f"ID: {Member.id}\n\n"
                                                                                          f"Высшая роль: {Member.top_role}\n\n"
                                                                                          f"Аккаунт создан: {Member.created_at.strftime('%b %#d, %Y')}", 
                                                                                          color=0xff0000, timestamp=ctx.message.created_at)

        emb.set_thumbnail(url= Member.avatar_url)
        emb.set_footer(icon_url= Member.avatar_url)
        emb.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)    
    
    
    #avatar
    @commands.command()
    async def avatar(self, ctx, member : discord.Member = None):
        user = ctx.message.author if (member == None) else member
        embed = discord.Embed(title=f'Аватар пользователя {user}', color= 0x0c0c0c)
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)

        
    #botinfo
    @commands.command( pass_context = True )
    async def botinfo(self, ctx ):
        await ctx.channel.purge( limit = 1 )
        emt = discord.Embed(title=f"{ctx.guild.name}", description="Информация о боте **NITAGAS bot**.\n  подробнее о командах  -help\n По вопросам обращатся на сервер https://discord.gg/NfTf9JD", color = 000000)
        emt.add_field(name=f'**Меня создал:**', value="Stanislav", inline=True)  # Создает строку
        emt.add_field(name=f'**Помощь в создании:**', value="", inline=True)  # Создает строку
        emt.add_field(name=f'**Лицензия:**', value="Nitagas", inline=True)  # Создает строку
        emt.add_field(name=f'**Я написан на:**', value="Discord.py", inline=True)  # Создает строку
        emt.add_field(name=f'**Версия:**', value="1.0", inline=True)  # Создает строку
        emt.add_field(name=f'**Патч:**', value="1.0", inline=True)  # Создает строку
        emt.set_footer(text=f"© Copyright 2020 Stanislav | Все права защищены")  # создаение футера
        await ctx.send(embed=emt)
    
def setup(client):
    client.add_cog(user(client))
