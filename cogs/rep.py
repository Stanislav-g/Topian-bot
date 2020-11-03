import discord
from discord.ext import commands
from pymongo import MongoClient
from random import randint, choice, choices
import datetime
from discord.utils import find
from datetime import datetime
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


    #__________________________________REPS_______________
    @commands.command()
    async def hi(self, ctx):
        await ctx.send(f'Hi')
        
    @commands.has_permissions(administrator = True)     
    @commands.command()
    async def module_rep(self, ctx, arg = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"]
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        if not arg:
            await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** вы не написали что хотите сделать, включить или выключить модуль!``=module_rep on`` ``=module_rep off`` """))

        elif arg == 'help':
            await ctx.send(embed = discord.Embed(description = f"""                
                **=module_rep** - модуль репутаций.
                ``=rep`` - посмотреть репутацию пользователя.
                ``=rep_user`` - увеличить или уменьшить репутацию пользователя. =rep_user @user (- или +)  ‌‌‍‍        ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍
                """))
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
                collectionmodules = db["modules"]
                collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": on, "lvls": 0, "rep": on, "ticket": 1, "warns": 0, "logs": 0, "reaction": 0, "roles": 0})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль репутаций успешно включен!"""))
            
            else:
                num = ctx.author.guild.id
                num2 = '111'
                allnum = str(num) + str(num2)
                stat = collectionmodules.find_one({"_id": allnum})["rep"]
                if stat == 'on':
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль репутаций уже включен!"""))
                else:
                    num = ctx.author.guild.id
                    num2 = '111'
                    allnum = str(num) + str(num2)
                    on = 'on'
                    guild = collectionmodules.update_one({"_id": allnum}, {"$set": {"rep": on}})
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль репутаций успешно включен!"""))

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
                collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": off, "lvls": 0, "rep": off, "ticket": 1, "warns": 0, "logs": 0, "reaction": 0, "roles": 0})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль репутаций успешно выключен!"""))
            else:
                stat = collectionmodules.find_one({"_id": allnum})["rep"]
                if stat == 'off':
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль репутаций уже выключен!"""))
                else:
                    num = ctx.author.guild.id
                    num2 = '111'
                    allnum = str(num) + str(num2)
                    off = 'off'
                    guild = collectionmodules.update_one({"_id": allnum}, {"$set": {"rep": off}})
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль репутаций выключен!"""))
        else:
            await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** вы не написали что хотите сделать, включить или выключить модуль!``=module_rep on`` ``=module_rep off`` """))



    @commands.command()
    async def rep(self, ctx, Member: discord.Member = None):
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
            if collectionmodules.find_one({"_id": allnum4})["rep"] == 'on':
                
                if not Member:
                    num = ctx.author.guild.id
                    num2 = ctx.author.id
                    allnum = num + num2
                    if collection.count_documents({"_id": allnum}) == 0:
                        name = ctx.author.name
                        num = ctx.author.guild.id
                        num2 = ctx.author.id
                        allnum = num + num2
                        collection.insert_one({"_id": allnum, "name": name, "balance": 0, "lvl": 0, "rep": 0, "message": 0})
                        reps = collection.find_one({"_id": allnum})["rep"]  
                        await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** ваша репутация составляет: {reps}"""))
                    else:
                        reps = collection.find_one({"_id": allnum})["rep"]  
                        await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** ваша репутация составляет: {reps}"""))

                else:
                    num = ctx.author.guild.id
                    num2 = Member.id
                    allnum = num + num2
                    if collection.count_documents({"_id": allnum}) == 0:
                        name = Member.name
                        num = ctx.author.guild.id
                        num2 = Member.id
                        allnum = num + num2
                        collection.insert_one({"_id": allnum, "name": name, "balance": 0, "lvl": 0, "rep": 0, "message": 0})
                        reps = collection.find_one({"_id": allnum})["rep"]  
                        await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** репутация данного пользователя составляет: {reps}"""))
                    else:
                        reps = collection.find_one({"_id": allnum})["rep"]  
                        await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** репутация данного пользователя составляет: {reps}"""))
            else:
                await ctx.send(f"Модуль репутаций на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")

    rate = 1
    #per: the amount of seconds the cooldown lasts
    per = 3600

    @commands.cooldown(rate, per, commands.BucketType.user)
    @commands.command()
    async def rep_user(self, ctx, arg = None, Member: discord.Member = None):
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
            if collectionmodules.find_one({"_id": allnum4})["rep"] == 'on':
                if not arg:
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}**, правильное использования команды: =rep_user + @user или  =rep_user - @user!"""))
                if arg == '+':
                    
                    if not Member:
                        await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}**, укажите пользователя! Правильное использования команды: =rep_user + @user или  =rep_user - @user!"""))
                    elif Member == ctx.author:
                        await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}**, вы не можете сами себе выдавать репутацию!"""))
                    else:
                        num = ctx.author.guild.id
                        num2 = Member.id
                        allnum = num + num2
                        if collection.count_documents({"_id": allnum}) == 0:
                            await ctx.send(f"Учетная запись данного пользователя не создана")
                        else:
                            num = ctx.author.guild.id
                            num2 = Member.id
                            allnum = num + num2
                            reps = collection.find_one({"_id": allnum})["rep"]
                            repnum = int(reps) + int('1')
                            balance = collection.update_one({"_id": allnum}, {"$set": {"rep": repnum}})
                            await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}**, репутация данного пользователя увеличена на 1."""))

                elif arg == '-':
                    if not Member:
                            await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}**, укажите пользователя!"""))
                    elif Member == ctx.author:
                        await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}**, вы не можете убирать у себя репутацию!"""))
                    else:
                        num = ctx.author.guild.id
                        num2 = Member.id
                        allnum = num + num2
                        if collection.count_documents({"_id": allnum}) == 0:
                            await ctx.send(f"Учетная запись данного пользователя не создана")
                        else:
                            num = ctx.author.guild.id
                            num2 = Member.id
                            allnum = num + num2
                            reps = collection.find_one({"_id": allnum})["rep"]
                            repnum = int(reps) - int('1')
                            balance = collection.update_one({"_id": allnum}, {"$set": {"rep": repnum}})
                            await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}**, репутация данного пользователя уменьшена на 1."""))
                else:
                    await ctx.send(f"Введите правильно команду!") 
                    
            else:
                await ctx.send(f"Модуль репутаций на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")   
                


def setup(client):
    client.add_cog(user(client))
