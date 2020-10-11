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
    async def module_lvls(self, ctx, arg = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"]
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionlogschannels = db["logschannels"]
        if not arg:
            await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** вы не написали что хотите сделать, включить или выключить модуль!``=module_lvls on`` ``=module_lvls off`` """))
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
                collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": 0, "lvls": on, "rep": 0, "ticket": 1, "warns": 0, "logs": 0})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль уровней успешно включен!"""))
            
            else:
                num = ctx.author.guild.id
                num2 = '111'
                allnum = str(num) + str(num2)
                stat = collectionmodules.find_one({"_id": allnum})["lvls"]
                if stat == 'on':
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль уровней уже включен!"""))
                else:
                    num = ctx.author.guild.id
                    num2 = '111'
                    allnum = str(num) + str(num2)
                    on = 'on'
                    guild = collectionmodules.update_one({"_id": allnum}, {"$set": {"lvls": on}})
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль уровней успешно включен!"""))

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
                collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": 0, "lvls": off, "rep": 0, "ticket": 1, "warns": 0, "logs": 0})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль уровней успешно выключен!"""))
            else:
                stat = collectionmodules.find_one({"_id": allnum})["lvls"]
                if stat == 'off':
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль уровней уже выключен!"""))
                else:
                    num = ctx.author.guild.id
                    num2 = '111'
                    allnum = str(num) + str(num2)
                    off = 'off'
                    guild = collectionmodules.update_one({"_id": allnum}, {"$set": {"lvls": off}})
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль уровней выключен!"""))
        else:
            await ctx.send(f"На данном сервере не создана база данных, ее можно создать командой")


    
    
    @commands.Cog.listener()
    async def on_message(self, message ):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionlogschannels = db["logschannels"]
        num = message.guild.id
        num2 = '111'
        allnum4 = str(num) + str(num2)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["lvls"] == 'on':
                num = message.author.guild.id
                num2 = message.author.id
                allnum = num + num2
                if collection.count_documents({"_id": allnum}) == 0:
                    name = message.author.name
                    num = message.author.guild.id
                    num2 = message.author.id
                    allnum = num + num2
                    collection.insert_one({"_id": allnum, "name": name, "balance": 0, "lvl": 0, "rep": 0, "message": 0})
                    
                else:
                    num = message.author.guild.id
                    num2 = message.author.id
                    allnum = num + num2
                    message = collection.find_one({"_id": allnum})["message"]
                    msg = int(message) + int('1')
                    collection.update_one({"_id": allnum}, {"$set": {"message": msg}})
                    mes = collection.find_one({"_id": allnum})["message"]
                    if mes == 10:
                        collection.update_one({"_id": allnum}, {"$set": {"lvl": lvl + 1}})
                    elif mes == 20:
                        collection.update_one({"_id": allnum}, {"$set": {"lvl": lvl + 1}})
                    elif mes == 30:
                        collection.update_one({"_id": allnum}, {"$set": {"lvl": lvl + 1}})
                    elif mes == 40:
                        collection.update_one({"_id": allnum}, {"$set": {"lvl": lvl + 1}})
                    elif mes == 50:
                        collection.update_one({"_id": allnum}, {"$set": {"lvl": lvl + 1}})
                    elif mes == 60:
                        collection.update_one({"_id": allnum}, {"$set": {"lvl": lvl + 1}})
                    elif mes == 70:
                        collection.update_one({"_id": allnum}, {"$set": {"lvl": lvl + 1}})
                        


    @commands.command()
    async def message(self, ctx, Member: discord.Member = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionlogschannels = db["logschannels"]        
        num1 = ctx.author.guild.id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["lvls"] == 'on':
                
                if not Member:
                    num = ctx.author.guild.id
                    num2 = ctx.author.id
                    allnum = num + num2
                    if collection.count_documents({"_id": allnum}) == 0:
                        await ctx.send(f"Ваша учетная запись не создана, вы можете создать ее командой =economy")
                    else:
                        num = ctx.author.guild.id
                        num2 = ctx.author.id
                        allnum = num + num2
                        mes = collection.find_one({"_id": allnum})["message"]
                        await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** вы отправили **{mes}** сообщений"""))
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
                        mes = collection.find_one({"_id": allnum})["message"]
                        await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** данный пользователь отправил **{mes}** сообщений"""))

        else:
            await ctx.send(f"Модуль уровней на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")

    @commands.command()
    async def lvl(self, ctx, Member: discord.Member = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionlogschannels = db["logschannels"]        
        num1 = ctx.author.guild.id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["lvls"] == 'on':
                
                if not Member:
                    num = ctx.author.guild.id
                    num2 = ctx.author.id
                    allnum = num + num2
                    if collection.count_documents({"_id": allnum}) == 0:
                        await ctx.send(f"Ваша учетная запись не создана, вы можете создать ее командой =economy")
                    else:
                        num = ctx.author.guild.id
                        num2 = ctx.author.id
                        allnum = num + num2
                        lvl = collection.find_one({"_id": allnum})["lvl"]
                        await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** ваш уровень **{lvl}**"""))
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
                        lvl = collection.find_one({"_id": allnum})["lvl"]
                        await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** уровень данного пользователя **{lvl}**"""))

        else:
            await ctx.send(f"Модуль уровней на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")


def setup(client):
    client.add_cog(user(client))
