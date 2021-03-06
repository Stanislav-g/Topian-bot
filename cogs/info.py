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
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from pymongo import MongoClient

class user(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command( pass_context = True )
    async def stats(self, ctx):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"]
        collection = db["money"]
        collectionmodules = db["modules"]
        
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionroles = db["roles"]
        user = int(550061958938886175)
        author = int(ctx.author.id)
        if author == user:
            client = commands.Bot( command_prefix = '=')
            a = collection.find().count()
            b = collectionmodules.find().count()
            c = collectionticket.find().count()
            d = collectionshop.find().count()
            e = collectionroles.find().count()
            mem = len(set(self.client.get_all_members()))
            #mem = len(self.client.guilds.member_count)
            gui = len(self.client.guilds)
            embed = discord.Embed(title=f"Статистика бота", color = 0x00FF00)
            embed.description=(
                f"**Пинг бота:** {self.client.ws.latency * 1000:.0f} ms.\n\n"
                f"**Я есть на:** {gui} серверах.\n\n"
                f"**Пользователи бота:** {mem}\n\n"
                f"© Copyright 2020 Stanislav | Все права защищены"
            )
            msg = await ctx.send(embed=embed)
            while True:
                client = commands.Bot( command_prefix = '=')

                a = collection.find().count()
                b = collectionmodules.find().count()
                c = collectionticket.find().count()
                d = collectionshop.find().count()
                e = collectionroles.find().count()
                mem = len(set(self.client.get_all_members()))
                #mem = len(self.client.guilds.member_count)
                gui = len(self.client.guilds)
                embed = discord.Embed(title=f"Статистика бота", color = 0x00FF00)
                embed.description=(
                    f"**Пинг бота:** {self.client.ws.latency * 1000:.0f} ms.\n\n"
                    f"**Я есть на:** {gui} серверах.\n\n"
                    f"**Пользователей в базе данных:** {a}\n\n"
                    f"**Серверов в базе данных:** {b}\n\n"
                    f"**Тикетов в базе данных:** {c}\n\n"
                    f"**Магазинов в базе данных:** {d}\n\n"
                    f"**Ролей в базе данных:** {e}\n\n"
                    f"© Copyright 2020 Stanislav | Все права защищены"
                ) 
                await asyncio.sleep(1)
                await msg.edit(content= None, embed=embed)




    @commands.command()
    async def roleinfo(self, ctx, role: discord.Role = None):
        members = len(role.members)
        embed = discord.Embed(title=f"{role.name}\nРоль создали {role.created_at.strftime('%A, %b %#d %Y')}", color=0x00FF00, timestamp=ctx.message.created_at)
        emb = discord.Embed( 
            title = 'Server info',
            color = 0x7aa13d
         )

        embed.add_field( name = '__**Роль**__', value = 
            f":flag_white: Название: **{role.name}**\n\n"
            f":id: ID: **{role.id}**\n\n"
            f":flag_white: Гильдия: **{role.guild}**\n\n"
            f":art: Цвет: **{role.colour}**\n\n"            
            f":arrow_up: Позиция роли: **{role.position}**\n\n"
             )
        embed.add_field( name = '__**Сервер**__', value = 
            f":arrow_up_down: Участники с этой ролью показываются отдельно: **{role.hoist}**\n\n"            
            f":arrow_up_down: Можно упоминать роль: **{role.mentionable}**\n\n"
            f":briefcase: Управляется ли роль гильдией: **{role.managed}**\n\n"           
            f":billed_cap: Права: **{role.permissions}**\n\n"
            f":smiley: Всего людей с этой ролью: **{members}**\n\n"
             )
                              
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f"ID: {role.id}")
        embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
        await ctx.send(embed=embed)             
                              
    @commands.command()
    async def serverinfo(self, ctx):
        members = ctx.guild.members
        online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
        offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
        idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
        dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
        allchannels = len(ctx.guild.channels)
        allvoice = len(ctx.guild.voice_channels)
        alltext = len(ctx.guild.text_channels)
        allroles = len(ctx.guild.roles)
        cat = len(ctx.guild.categories)
        embed = discord.Embed(title=f"{ctx.guild.name}\nСервер создали {ctx.guild.created_at.strftime('%A, %b %#d %Y')}", color=0x00FF00, timestamp=ctx.message.created_at)
        emb = discord.Embed( 
            title = 'Server info',
            color = 0x7aa13d
         )

        embed.add_field( name = '__**Сервер**__', value = 
            f":flag_white: Регион **{ctx.guild.region}**\n\n"
            f":crown: Глава сервера **{ctx.guild.owner}**\n\n"
            f":shield: Уровень верификации: **{ctx.guild.verification_level}**\n\n"
            f":arrow_up: Большая гильдия **{ctx.guild.large}**\n\n"
            f":clown: Лимит эмодзи **{ctx.guild.emoji_limit}**\n\n"
            f":briefcase: Всего ролей: **{allroles}**\n\n"
             )
        embed.add_field( name = '__**Участники**__', value = 
            f":tools: Ботов на сервере: **{len([m for m in members if m.bot])}**\n\n"
            f":green_circle: Онлайн: **{online}**\n\n"
            f":black_circle: Оффлайн: **{offline}**\n\n"
            f":yellow_circle: Отошли: **{idle}**\n\n"
            f":red_circle: Не трогать: **{dnd}**\n\n"
            f":slight_smile: Людей на сервере **{ctx.guild.member_count}**\n\n"
            f":gem: Бустеры сервера **{ctx.guild.premium_subscribers}**\n\n"
             )
        embed.add_field( name = '__**Каналы**__', value = 
            f":musical_keyboard: Всего каналов: **{allchannels}**\n\n"
            f":loud_sound: Голосовых каналов: **{allvoice}**\n\n"
            f":keyboard: Текстовых каналов: **{alltext}**\n\n"
            f":card_box: Категории сервера: **{cat}**\n\n"
             )
        
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f"ID: {ctx.guild.id}")
        embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
        await ctx.send(embed=embed)   
                          
    #botinfo
    @commands.command( pass_context = True )
    async def botinfo(self, ctx):
        client = commands.Bot( command_prefix = '=')
        urll = 'https://discord.com/api/oauth2/authorize?client_id=742649758002315274&permissions=8&scope=bot'
        urltr = 'https://discord.gg/Vnb57MM'         
        
        
        gui = len(self.client.guilds)
        embed = discord.Embed(title=f"Информация о боте **Topian bot**.\n  чтобы узнать команды бота, пиши: =help", color = 0x00FF00)
        embed.description=(
            f"**Меня создал:** Stanislav#1022\n\n"
            f"**Помощь в создании:** Topian Team.\n\n"
            f"**Лицензия:** TSBot.\n\n"
            f"**Я написан на**: Discord.py\n\n"
            f"**Версия:** 3.0\n\n"
            f"**Патч:** 1.0\n\n"
            f"**Пинг бота:** {self.client.ws.latency * 1000:.0f} ms.\n\n"
            f"**Я есть на:** {gui} серверах.\n\n"
            f"**Сервер поддержки:** [clik](https://discord.gg/Vnb57MM)\n\n"
            f"**Добавить бота:** [clik](https://discord.com/api/oauth2/authorize?client_id=742649758002315274&permissions=8&scope=bot).\n\n"
            f"© Copyright 2020 Stanislav | Все права защищены"
        )
        await ctx.send(embed=embed) 
 
  
 
                     

                              
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
    async def server(self, ctx):
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
        embed = discord.Embed(title=f"{ctx.guild.name}", color=0x00FF00, timestamp=ctx.message.created_at)
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
    async def user(self, ctx, Member: discord.Member = None ):
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
                                                                                          color=0x00FF00, timestamp=ctx.message.created_at)

        emb.set_thumbnail(url= Member.avatar_url)
        emb.set_footer(icon_url= Member.avatar_url)
        emb.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)    
    

        
        # userinfo
    @commands.command()
    async def userinfo(self, ctx, Member: discord.Member = None ):
        if not Member:
            Member = ctx.author                       
        roles = (role for role in Member.roles )
        roleee = len(Member.roles)
        embed = discord.Embed(title=f":tools: Аккаунт создан: {Member.created_at.strftime('%b %#d, %Y')}", color=0x00FF00, timestamp=ctx.message.created_at)
        embed.add_field( name = '__**Пользователь**__', value = 
            f":smiley: Имя: {Member.name}#{Member.discriminator}\n\n"
            f":billed_cap: Никнейм: {Member.nick}\n\n"
            f":id: ID: {Member.id}\n\n"
            f":briefcase: Высшая роль: {Member.top_role}\n\n"
            f":briefcase: Всего ролей: {roleee}\n\n"             
            f":scroll: Статус: {Member.activity}\n\n"
            f"Представитель Discord: {Member.system}\n\n"
            f"Цвет ника: {Member.colour}\n\n" 
            f"Участник зашёл на сервер: {Member.joined_at.strftime('%b %#d, %Y')}\n\n"
            f"Фото профиля: {Member.avatar_url}"             
        )

        embed.set_thumbnail(url= Member.avatar_url)
        embed.set_footer(icon_url= Member.avatar_url)
        embed.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)   
                              
    #avatar
    @commands.command()
    async def avatar(self, ctx, member : discord.Member = None):
        user = ctx.message.author if (member == None) else member
        embed = discord.Embed(title=f'Аватар пользователя {user}', color= 0x00FF00)
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{self.client.ws.latency * 1000:.0f} ms')
              
    @commands.command()
    async def user_boost(self, ctx, member : discord.Member = None):
        if member == None:
            a = ctx.author.premium_since
            if a == None:
                await ctx.send("Вы не давали буст серверу!")
            else:
                await ctx.send(f"Буст: {ctx.author.premium_since}\n\n") 
        else:
            e = member.premium_since
            if e == None:
                await ctx.send("Данный пользователь не давал буст серверу!")
            else:
                await ctx.send(f"Буст: {member.premium_since}\n\n")  
        
    @commands.command()
    async def guild_emojis(self, ctx):
        await ctx.send(f"Гильдии: {ctx.guild.emojis}\n\n") 
        
        
def setup(client):
    client.add_cog(user(client))
