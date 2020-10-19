import discord
from discord.ext import commands
from pymongo import MongoClient
from random import randint, choice, choices
import datetime
from discord.utils import find
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
import requests

class user(commands.Cog):

    def __init__(self, client):
        self.client = client




    clu= os.environ.get('MONGODB_URI')
    cluster = MongoClient(clu)
    db = cluster["topianbot"]
    collection = db["money"]
    collectionmodules = db["modules"]
    collectionshop = db["shop"]
    collectionticket = db["ticket"]


    @commands.command()
    async def ticket_create(self, ctx, arg = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"]
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        num1 = ctx.author.guild.id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["ticket"] == 'on':
                num = ctx.author.guild.id
                num2 = ctx.author.id
                t = 'ticket'
                allnumni = str(num) + str(num2) + str(t)
                if collectionticket.count_documents({"_id": allnumni}) == 0:
                    num = ctx.author.guild.id
                    num2 = ctx.author.id
                    t = 'ticket'
                    allnumn = str(num) + str(num2) + str(t)
                    member = ctx.author
                    collectionticket.insert_one({"_id": allnumn, "ticket": 1, "channel": 0})
                    overwrites = {
                        ctx.author: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                        ctx.author.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_channels=True, manage_roles=True),
                        ctx.author.guild.default_role: discord.PermissionOverwrite(
                        read_messages=False)
                    }

                    ticket = await ctx.author.guild.create_text_channel(
                        name=member.name,
                        overwrites=overwrites,
                        topic=f'Ticket created by {member} ({member.id})',
                            eason=f'Ticket created by {member} ({member.id})'
                    )

                    await ctx.send(embed = discord.Embed(description = f'**Тикет успешно создан!**', color=0x0c0c0c))
                    embed = discord.Embed(
                        title=f'Ticket opened by {member}\nТема тикета: {arg}\nЧтобы закрыть тикет, напишите команду: =ticket_delete',
                        timestamp=datetime.datetime.now(datetime.timezone.utc),
                        color=member.color
                    )
                    text = await ticket.send(embed=embed)
                    chantext = text.channel.id
                    collectionticket.update_one({"_id": allnumn}, {"$set": {"channel": chantext}})
                    await text.add_reaction('✅') 

                else:
                    await ctx.send(f"Вы уже создали тикет!")
            else:
                await ctx.send(f"Модуль тикетов на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")

        else:
            await ctx.send(f"Модуль тикетов на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")
            
    @commands.has_permissions(administrator = True)         
    @commands.command()
    async def ticket_del(self, ctx, member: discord.Member = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"]
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        num1 = ctx.author.guild.id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["ticket"] == 'on':
                if not member:
                    await ctx.send(f"Правильное использование команды: =ticket_del @user")
                num = ctx.author.guild.id
                num2 = member.id
                t = 'ticket'
                allnumni = str(num) + str(num2) + str(t)
                if collectionticket.count_documents({"_id": allnumni}) == 0:
                    await ctx.send(f"Данный пользователь еще не создал тикет!")
                else:
                    num = ctx.author.guild.id
                    num2 = member.id
                    t = 'ticket'
                    allnumn = str(num) + str(num2) + str(t)
                    chan = collectionticket.find_one({"_id": allnumn})["channel"]
                    if chan == ctx.channel.id:
                        collectionticket.delete_one({"_id": allnumn})
                        c = ctx.channel
                        await c.delete()
                    else:
                        await ctx.send(f"Напишите эту команду в тикете данного пользователя!")
                        
            else:
                await ctx.send(f"Модуль тикетов на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")

        else:
            await ctx.send(f"Модуль тикетов на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")
            
            
    @commands.command()
    async def ticket_delete(self, ctx, arg = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"]
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        num1 = ctx.author.guild.id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["ticket"] == 'on':
                
                num = ctx.author.guild.id
                num2 = ctx.author.id
                t = 'ticket'
                allnumni = str(num) + str(num2) + str(t)
                if collectionticket.count_documents({"_id": allnumni}) == 0:
                    await ctx.send(f"Вы еще не создали тикет!")
                else:
                    num = ctx.author.guild.id
                    num2 = ctx.author.id
                    t = 'ticket'
                    allnumn = str(num) + str(num2) + str(t)
                    chan = collectionticket.find_one({"_id": allnumn})["channel"]
                    if chan == ctx.channel.id:
                        collectionticket.delete_one({"_id": allnumn})
                        c = ctx.channel
                        await c.delete()
                    else:
                        await ctx.send(f"Напишите эту команду в вашем тикете!")
                        
            else:
                await ctx.send(f"Модуль тикетов на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")

        else:
            await ctx.send(f"Модуль тикетов на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")

    @commands.has_permissions(administrator = True)     
    @commands.command()
    async def module_ticket(self, ctx, arg = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"]
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        if not arg:
            await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** вы не написали что хотите сделать, включить или выключить модуль!``=module_ticket on````=module_ticket off`` """))
        elif arg == 'on':
            name = 'economy'
            num = ctx.author.guild.id
            num2 = '111'
            allnum = str(num) + str(num2)
            if collectionmodules.count_documents({"_id": allnum}) == 0:
                num = ctx.author.guild.id
                name = 'economy'
                num2 = '111'
                allnum = str(num) + str(num2)
                on = 'on'
                collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": 0, "lvls": 0, "rep": 0, "ticket": on, "warns": 0, "logs": 0, "reaction": 0, "roles": 0})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль тикетов успешно включен!"""))
            
            else:
                num = ctx.author.guild.id
                num2 = '111'
                allnum = str(num) + str(num2)
                stat = collectionmodules.find_one({"_id": allnum})["lvls"]
                if stat == 'on':
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль тикетов  уже включен!"""))
                else:
                    num = ctx.author.guild.id
                    num2 = '111'
                    allnum = str(num) + str(num2)
                    on = 'on'
                    guild = collectionmodules.update_one({"_id": allnum}, {"$set": {"ticket": on}})
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль тикетов  успешно включен!"""))

        elif arg == 'off':
            name = 'economy'
            num = ctx.author.guild.id
            num2 = '111'
            allnum = str(num) + str(num2)
            if collectionmodules.count_documents({"_id": allnum}) == 0:
                num = ctx.author.guild.id
                name = 'economy'
                num2 = '111'
                allnum = str(num) + str(num2)
                off = 'off'
                collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": 0, "lvls": 0, "rep": 0, "ticket": off, "warns": 0, "logs": 0, "reaction": 0, "roles": 0})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль тикетов  успешно выключен!"""))
            else:
                num = ctx.author.guild.id
                num2 = '111'
                allnum = str(num) + str(num2)
                off = 'off'
                guild = collectionmodules.update_one({"_id": allnum}, {"$set": {"ticket": off}})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль тикетов  успешно выключен!"""))
        else:
            await ctx.send(f"На данном сервере не создана база данных, ее можно создать командой")

def setup(client):
    client.add_cog(user(client))
