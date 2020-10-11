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
    async def module_reaction(self, ctx, arg = None):
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
                collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": 0, "lvls": on, "rep": 0, "ticket": 1, "warns": 0, "logs": 0, "reaction": 0})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль уровней успешно включен!"""))
            
            else:
                num = ctx.author.guild.id
                num2 = '111'
                allnum = str(num) + str(num2)
                stat = collectionmodules.find_one({"_id": allnum})["reaction"]
                if stat == 'on':
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль уровней уже включен!"""))
                else:
                    num = ctx.author.guild.id
                    num2 = '111'
                    allnum = str(num) + str(num2)
                    on = 'on'
                    guild = collectionmodules.update_one({"_id": allnum}, {"$set": {"reaction": on}})
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
                collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": 0, "lvls": off, "rep": 0, "ticket": 1, "warns": 0, "logs": 0, "reaction": 0})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль уровней успешно выключен!"""))
            else:
                stat = collectionmodules.find_one({"_id": allnum})["reaction"]
                if stat == 'off':
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль уровней уже выключен!"""))
                else:
                    num = ctx.author.guild.id
                    num2 = '111'
                    allnum = str(num) + str(num2)
                    off = 'off'
                    guild = collectionmodules.update_one({"_id": allnum}, {"$set": {"reaction": off}})
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль уровней выключен!"""))
        else:
            await ctx.send(f"На данном сервере не создана база данных, ее можно создать командой")


    @commands.command()
    async def reaction_channel(self, ctx, arg = None):
        client = commands.Bot( command_prefix = '=')
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionlogschannels = db["logschannels"]
        collectionreaction = db["reaction"]
        name = 'economy'
        num = ctx.author.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        if collectionmodules.count_documents({"_id": allnum}) == 1:
            num = ctx.author.guild.id
            num2 = '111'
            allnum = str(num) + str(num2)
            stat = collectionmodules.find_one({"_id": allnum})["reaction"]
            if stat == 'on':
                for channel in ctx.guild.text_channels:
                    ch = int(channel.id)
                    argg = int(arg)
                    if argg == ch:
                        guild = ctx.guild.id
                        if collectionreaction.count_documents({"_id": guild}) == 0:
                            collectionlogschannels.insert_one({"_id": guild, "reactionchannel": argg})
                            await ctx.send("Канал авто-реакций установлен!")
                            break
                        else:
                            collectionlogschannels.update_one({"_id": guild}, {"$set": {"reactionchannel": argg}})
                            await ctx.send("Канал авто-реакций обновлен!")
                            
                    else:
                        pass
                    
            else:
                await ctx.send(f"Модуль реакций на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")
        else:
            await ctx.send(f"Модуль реакций на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")           


    
    
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
            if collectionmodules.find_one({"_id": allnum4})["reaction"] == 'on':
                num = message.author.guild.id
                if collectionlogschannels.count_documents({"_id": num}) == 0:
                    pass
                    
                else:
                    stat = collectionlogschannels.find_one({"_id": num})["reaction"]
                    if stat != '0':
                        await message.add_reaction('✅')
                        await message.add_reaction('❌') 

                        


def setup(client):
    client.add_cog(user(client))
