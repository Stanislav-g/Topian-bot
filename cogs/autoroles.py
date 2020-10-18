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
    collectionroles = db["roles"]


    @commands.command()
    async def module_roles(self, ctx, arg = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"]
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionroles = db["roles"]
        if not arg:
            await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** вы не написали что хотите сделать, включить или выключить модуль!``=module_roles on````=module_roles off`` """))
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
                collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": 0, "lvls": 0, "rep": 0, "ticket": 0, "warns": 0, "logs": 0, "reaction": 0, "roles": on})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль авто выдачи ролей успешно включен!"""))
            
            else:
                num = ctx.author.guild.id
                num2 = '111'
                allnum = str(num) + str(num2)
                stat = collectionmodules.find_one({"_id": allnum})["roles"]
                if stat == 'on':
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль авто выдачи ролей уже включен!"""))
                else:
                    num = ctx.author.guild.id
                    num2 = '111'
                    allnum = str(num) + str(num2)
                    on = 'on'
                    guild = collectionmodules.update_one({"_id": allnum}, {"$set": {"roles": on}})
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль авто выдачи ролей успешно включен!"""))

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
                collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": 0, "lvls": 0, "rep": 0, "ticket": 0, "warns": 0, "logs": 0, "reaction": 0, "roles": on})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль авто выдачи ролей успешно выключен!"""))
            else:
                num = ctx.author.guild.id
                num2 = '111'
                allnum = str(num) + str(num2)
                off = 'off'
                guild = collectionmodules.update_one({"_id": allnum}, {"$set": {"roles": off}})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль авто выдачи ролей успешно выключен!"""))
        else:
            await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** вы не написали что хотите сделать, включить или выключить модуль!``=module_roles on````=module_roles off`` """))








    @commands.command()
    async def auto_role(self, ctx, message:int = None, role = None, reaction:str = None):  
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"]
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionroles = db["roles"]
        num1 = ctx.author.guild.id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if message == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'autoroe',value = '**autorole** = autorole (id сообщения) (id роли) (эмодзи)')
            await ctx.send( embed = embw )
        elif role == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'autoroe',value = '**autorole** = autorole (id сообщения) (id роли) (эмодзи)')
            await ctx.send( embed = embw )
        elif reaction == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'autoroe',value = '**autorole** = autorole (id сообщения) (id роли) (эмодзи)')
            await ctx.send( embed = embw )
        else:
            if collectionmodules.count_documents({"_id": allnum4}) == 1: 
                if collectionmodules.find_one({"_id": allnum4})["roles"] == 'on':
                    rea = reaction
                    alln = str(message) + str(rea)
                    
                    
                    await ctx.message.add_reaction('✅')
                    m = await ctx.message.channel.fetch_message(message)
                    await m.add_reaction(reaction)
                    if collectionroles.count_documents({"_id": alln}) == 0:
                        collectionroles.insert_one({"_id": alln, "role": role, "reaction": reaction, "message": message})
                        await ctx.send("Авто выдача роли по реакции добавлена!")
                    else:
                        await ctx.send(f"Данного сообщения не существует или данной авто выдачи ролей не существует!")
                else:
                    await ctx.send(f"Модуль авто выдачи ролей на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")
                
            else:
                await ctx.send(f"Модуль авто выдачи ролей на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")
            



       
    @commands.command()
    async def delete_auto_role(self, ctx, message = None, reaction = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"]
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionroles = db["roles"]
        num1 = ctx.author.guild.id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if message == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'delete_autoreaction',value = '**delete_autoreaction** = delete_autoreaction (id сообщения) (эмодзи)')
            await ctx.send( embed = embw )
        elif reaction == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'delete_autoreaction',value = '**delete_autoreaction* = delete_autoreaction (id сообщения) (эмодзи)')
            await ctx.send( embed = embw )
        else:
            if collectionmodules.count_documents({"_id": allnum4}) == 1: 
                if collectionmodules.find_one({"_id": allnum4})["roles"] == 'on':
                    rea = reaction
                    alln = str(message) + str(rea)
                    if collectionroles.count_documents({"_id": alln}) == 1:
                        collectionroles.delete_one({"_id": alln})
                        await ctx.send("Авто выдача роли по реакции удалена!")
                    else:
                        await ctx.send(f"Данного сообщения не существует или данной авто выдачи ролей не существует!")
                else:
                    await ctx.send(f"Модуль авто выдачи ролей на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")
                
            else:
                await ctx.send(f"Модуль авто выдачи ролей на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")
            


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"]
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionroles = db["roles"]
        num1 = payload.guild_id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["roles"] == 'on':
                y = payload.message_id
                i = payload.emoji
                alln = str(y) + str(i)
                if collectionroles.count_documents({"_id": alln}) == 1:
                    rolee = collectionroles.find_one({"_id": alln})["role"]
                    reactionn = collectionroles.find_one({"_id": alln})["reaction"]
                    messagee = collectionroles.find_one({"_id": alln})["message"]
                    m = int(messagee)
                    if payload.message_id == m: # ID Сообщения
                        guild = self.client.get_guild(payload.guild_id)
                        role = None
                        
                        if str(payload.emoji) == reactionn: # Emoji для реакций
                            role = guild.get_role(int(rolee)) # ID Ролей для в
                            
                            if role:
                                member = guild.get_member(payload.user_id)
                                if member:
                                    await member.add_roles(role)



    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"]
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionroles = db["roles"]
        num1 = payload.guild_id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["roles"] == 'on':
                y = payload.message_id
                i = payload.emoji
                alln = str(y) + str(i)
                if collectionroles.count_documents({"_id": alln}) == 1:
                    rolee = collectionroles.find_one({"_id": alln})["role"]
                    reactionn = collectionroles.find_one({"_id": alln})["reaction"]
                    messagee = collectionroles.find_one({"_id": alln})["message"]
                    m = int(messagee)
                    if payload.message_id == m: # ID Сообщения
                        guild = self.client.get_guild(payload.guild_id)
                        role = None
                        
                        if str(payload.emoji) == reactionn: # Emoji для реакций
                            role = guild.get_role(int(rolee)) # ID Ролей для в
                            
                            if role:
                                member = guild.get_member(payload.user_id)
                                if member:
                                    await member.remove_roles(role)

def setup(client):
    client.add_cog(user(client))
