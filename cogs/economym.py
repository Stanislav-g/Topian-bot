import discord
from discord.ext import commands
from pymongo import MongoClient
import random
from random import randint, choice, choices
import os
import random
import asyncio
from discord.utils import get
import datetime
import smtplib
import socket
from discord.utils import find

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
    collectionlogschannels = db["logschannels"]


    @commands.has_permissions(administrator = True)            
    @commands.command()
    async def addrole_shop(self, ctx, role: discord.Role = None, cost: int = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        num1 = ctx.author.guild.id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["on_off"] == 'on':
                if role is None:
                    await ctx.send(f"**{ctx.author}**, укажите роль")
                if cost is None:
                    await ctx.send(f"**{ctx.author}**, укажите стоимость данной роли")

                elif cost < 0:
                    await ctx.send(f"**{ctx.author}**, стоимость роли не может быть отрицательной")
                else:
                    rolee = str(ctx.author.guild.id) + str(role.id)
                    if collectionshop.count_documents({"_id": rolee}) == 0:
                        collectionshop.insert_one({"_id": rolee, "name": role.mention, "cost": cost})
                        await ctx.send(f"**{ctx.author}**, роль добавлена в магазин!")
                        
                        
                    else:
                        await ctx.send(f"**{ctx.author}**, роль уже добавлена в магазин!")
                        
                        
            else:
                await ctx.send(f"Модуль экономики на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")
            
    @commands.has_permissions(administrator = True)            
    @commands.command()
    async def deleterole_shop(self, ctx, role: discord.Role = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]        
        num1 = ctx.author.guild.id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["on_off"] == 'on':
                idshop = str(ctx.author.guild.id) + str(role.id)
                if collectionshop.count_documents({"_id": idshop}) == 1:
                    collectionshop.delete_one({"_id": idshop})   
                    await ctx.send(f"**{ctx.author}**, роль удалена из магазина!")
            else:
                await ctx.send(f"Модуль экономики на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")

                
    @commands.command()
    async def shop(self, ctx):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]        
        num1 = ctx.author.guild.id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["on_off"] == 'on':
                for role in ctx.guild.roles:
                    
                    idshop = str(ctx.author.guild.id) + str(role.id)
                    if collectionshop.count_documents({"_id": idshop}) == 0:
                        pass

                    else:
                        guildid = str(ctx.author.guild.id) + str(role.id)
                        name = collectionshop.find_one({"_id": guildid})["name"]
                        cost = collectionshop.find_one({"_id": guildid})["cost"]
                        allinfo = str(name) + str(" - ") + str(cost) + str("$")
                        emt = discord.Embed(title=f"Информация об магазине.",description=f'{allinfo}', color = 0x00FF00)
                        await ctx.send(embed=emt)

            else:
                await ctx.send(f"Модуль экономики на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")


                    
    @commands.command()
    async def buyrole(self, ctx, role: discord.Role = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]        
        num1 = ctx.author.guild.id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["on_off"] == 'on':
                if role is None:
                    await ctx.send(f"**{ctx.author}**, укажите роль")
                if role in ctx.author.roles:
                    await ctx.send(f"**{ctx.author}**, у вас уже имеется данная роль")
                else:
                    idshop = str(ctx.author.guild.id) + str(role.id)
                    if collectionshop.count_documents({"_id": idshop}) == 0:
                        await ctx.send( f'{ctx.author.name}, данной роли нету в продаже!')
                    else:
                        idshop = str(ctx.author.guild.id) + str(role.id)
        
                        cost = collectionshop.find_one({"_id": idshop})["cost"]

                        
                        n = ctx.author.guild.id
                        nu = ctx.author.id
                        alln = n + nu
                        balance = collection.find_one({"_id": alln})["balance"]
                        if cost > balance:
                            await ctx.send(f"**{ctx.author}**, на вашем счету недостаточно средств")
                        else:
                            await ctx.author.add_roles(role)
                            balance = collection.update_one({"_id": alln}, {"$set": {"balance": balance - cost}})
                            await ctx.send( f'{ctx.author.name}, поздравляю вас! Вы купили роль **{role}**')
                        
                    
            else:
                await ctx.send(f"Модуль экономики на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")



    @commands.has_permissions(administrator = True)        
    @commands.command()
    async def module_economy(self, ctx, arg = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]        
        if not arg:
            emb = discord.Embed( 
            title = 'Чтобы включить модуль напишите ``=module_economy``, чтобы отключить модуль напишите ``=module_economy off``',
            color = 0x7aa13d
            )

            emb.add_field( name = '__**Команды**__', value = '''
            ``=balance`` - узнать баланс пользователя.
            ``=work`` - заработать деньги.
            ``=economy`` - создать профиль. 
            ``=shop`` - посмотреть магазин.
            ``=addshop`` - создать магазин.
            ``=addrole_shop`` - добавить роль в магазин. =addshop_role @role (цена)
            ``=deleteshop_role`` - нету
            ``=deleteshop`` - нету
                 
                 
            ''' )
            await ctx.send(embed = emb) 
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
                collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": on, "lvls": on, "rep": 0, "ticket": 0, "warns": 0, "logs": 0, "reaction": 0, "roles": 0})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}**, модуль экономики успешно включен!"""))
            
            else:
                stat = collectionmodules.find_one({"_id": allnum})["on_off"]
                if stat == 'on':
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}**, модуль экономики уже включен!"""))
                else:
                    num = ctx.author.guild.id
                    num2 = '111'
                    allnum = str(num) + str(num2)
                    on = 'on'
                    guild = collectionmodules.update_one({"_id": allnum}, {"$set": {"on_off": on}})
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}**, модуль экономики успешно включен!"""))

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
                guild = collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": off, "lvls": 0, "rep": 0, "ticket": 0, "warns": 0, "logs": 0, "reaction": 0, "roles": 0})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}**, модуль экономики успешно выключен!"""))
            else:
                stat = collectionmodules.find_one({"_id": allnum})["on_off"]
                if stat == 'off':
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}**, модуль экономики уже выключен!"""))
                else:
                    num = ctx.author.guild.id
                    num2 = '111'
                    allnum = str(num) + str(num2)
                    off = 'off'
                    guild = collectionmodules.update_one({"_id": allnum}, {"$set": {"on_off": off}})
                    
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}**, модуль экономики успешно выключен!"""))
        else:
            await ctx.send(f"На данном сервере не создана база данных, ее можно создать командой")


    @commands.command()
    async def balance(self, ctx, Member: discord.Member = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]        
        num1 = ctx.author.guild.id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["on_off"] == 'on':
                
                if not Member:
                    num = ctx.author.guild.id
                    num2 = ctx.author.id
                    allnum = num + num2
                    if collection.count_documents({"_id": allnum}) == 0:
                        await ctx.send(f"Ваша учетная запись не создана, вы можете создать ее командой -economy")
                    else:
                        num = ctx.author.guild.id
                        num2 = ctx.author.id
                        allnum = num + num2
                        balance = collection.find_one({"_id": allnum})["balance"]
                        await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}**, ваш баланс составляет **{balance}** :dollar:"""))
                else:
                    num = ctx.author.guild.id
                    num2 = Member.id
                    allnum = num + num2
                    if collection.count_documents({"_id": allnum}) == 0:
                        await ctx.send(f"Учетная запись данного пользователя не создана!")
                    else:
                        num = ctx.author.guild.id
                        num2 = Member.id
                        allnum = num + num2
                        balance = collection.find_one({"_id": allnum})["balance"]
                        await ctx.send(embed = discord.Embed(description = f"""Баланс пользователя **{Member}** **{balance}** :dollar:"""))

            else:
                await ctx.send(f"Модуль экономики на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")

            
    #rate: how many times the command can be used before triggering the cooldown
    rate = 1
    #per: the amount of seconds the cooldown lasts
    per = 3600


    @commands.cooldown(rate, per, commands.BucketType.user)
    @commands.command()
    async def work(self, ctx):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]        
        num1 = ctx.author.guild.id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["on_off"] == 'on':
                num = ctx.author.guild.id
                num2 = ctx.author.id
                allnum = num + num2
                if collection.count_documents({"_id": allnum}) == 0:
                    await ctx.send(f"Ваша учетная запись не создана, вы можете создать ее командой -economic")
                else:
                    numr = random.randint(1,100)
                    balancee = collection.find_one({"_id": allnum})["balance"]
                    
                    balance = collection.update_one({"_id": allnum}, {"$set": {"balance": balancee + numr}})
                    balanceee = collection.find_one({"_id": allnum})["balance"]
                    
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** вы заработали {numr} :dollar:, ваш баланс составляет **{balanceee}** :dollar:"""))
            else:
                await ctx.send(f"Модуль экономики на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")            








def setup(client):
    client.add_cog(user(client))
