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
    collectionlogschannels = db["logschannels"]

    #__________________________________logs_______________



    @commands.has_permissions(administrator = True)     
    @commands.command()
    async def module_logs(self, ctx, arg = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"]
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionlogschannels = db["logschannels"]
        if not arg:
            await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** вы не написали что хотите сделать, включить или выключить модуль!``=module_logs on`` ``=module_logs off`` """))

        elif arg == 'help':
            await ctx.send(embed = discord.Embed(description = f"""                
                **=module_logs** - модуль логов.
                ``=log_channel`` - добавить канал логов. =log_channel (айди канала)‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍        ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍
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
                collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": 0, "lvls": 0, "rep": 0, "ticket": 1, "warns": 0, "logs": on, "reaction": 0, "roles": 0})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль логов успешно включен!"""))
            
            else:
                num = ctx.author.guild.id
                num2 = '111'
                allnum = str(num) + str(num2)
                stat = collectionmodules.find_one({"_id": allnum})["logs"]
                if stat == 'on':
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль логов уже включен!"""))
                else:
                    num = ctx.author.guild.id
                    num2 = '111'
                    allnum = str(num) + str(num2)
                    on = 'on'
                    guild = collectionmodules.update_one({"_id": allnum}, {"$set": {"logs": on}})
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль логов успешно включен!"""))

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
                collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": 0, "lvls": 0, "rep": 0, "ticket": 1, "warns": 0, "logs": off, "reaction": 0, "roles": 0})
                await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль логов успешно выключен!"""))
            else:
                stat = collectionmodules.find_one({"_id": allnum})["logs"]
                if stat == 'off':
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль логов уже выключен!"""))
                else:
                    num = ctx.author.guild.id
                    num2 = '111'
                    allnum = str(num) + str(num2)
                    off = 'off'
                    guild = collectionmodules.update_one({"_id": allnum}, {"$set": {"logs": off}})
                    await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** модуль логов выключен!"""))
        else:
            await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** вы не написали что хотите сделать, включить или выключить модуль!``=module_logs on`` ``=module_logs off`` """))
                
    @commands.command()
    async def log_channel(self, ctx, arg = None):
        client = commands.Bot( command_prefix = '=')
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionlogschannels = db["logschannels"]
        name = 'economy'
        num = ctx.author.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        if '<' or '@' or '>' in arg:
            await ctx.send("Введите айди канала!")
        else:
            if collectionmodules.count_documents({"_id": allnum}) == 1:
                num = ctx.author.guild.id
                num2 = '111'
                allnum = str(num) + str(num2)
                stat = collectionmodules.find_one({"_id": allnum})["logs"]
                if stat == 'on':
                    for channel in ctx.guild.text_channels:
                        ch = int(channel.id)
                        argg = int(arg)
                        if argg == ch:
                            guild = ctx.guild.id
                            if collectionlogschannels.count_documents({"_id": guild}) == 0:
                                collectionlogschannels.insert_one({"_id": guild, "logchannel": argg})
                                await ctx.send("Канал логов установлен!")
                                break
                            else:
                                collectionlogschannels.update_one({"_id": guild}, {"$set": {"logchannel": argg}})
                                await ctx.send("Канал логов обновлен!")
                                
                        else:
                            pass
                        
            else:
                await ctx.send(f"Модуль логов на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")
                







    @commands.Cog.listener()
    async def on_message_delete(self, message ):
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
        allnum = str(num) + str(num2)
        if collectionmodules.count_documents({"_id": allnum}) == 1:
            stat = collectionmodules.find_one({"_id": allnum})["logs"]
            if stat == 'on':
                guildd = message.guild.id
                if collectionlogschannels.count_documents({"_id": guildd}) == 1:
                    cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
                    channell = self.client.get_channel(cha)
                    embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**The message was deleted:**\n ``` {message.content} ``` \nAuthor: {message.author.mention}\nChannel: {message.channel.mention}')
                    embed.set_footer(text=f"Message ID: {message.id}")
                    await channell.send(embed=embed)

            
            
    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionlogschannels = db["logschannels"]
        num = guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        if collectionmodules.count_documents({"_id": allnum}) == 1:
            stat = collectionmodules.find_one({"_id": allnum})["logs"]
            if stat == 'on':
                guildd = guild.id
                if collectionlogschannels.count_documents({"_id": guildd}) == 1:
                    cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
                    channel = self.client.get_channel(cha)
                    embed = discord.Embed(color=member.color if member.color != discord.Color.default() else discord.Color.red(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**{member.mention} was banned**')
                    embed.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
                    embed.set_footer(text=f"Member ID: {member.id}")
                    await channel.send(embed=embed)

                    embe = discord.Embed(color=member.color if member.color != discord.Color.default() else discord.Color.red(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**{member.mention}, вы забанены**')
                    embe.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
                    embe.set_footer(text=f"Guild name: {guild.name}")
                    await member.send(embed=embe)


	                            
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        client = commands.Bot( command_prefix = '=')
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionlogschannels = db["logschannels"]
        num = channel.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        if collectionmodules.count_documents({"_id": allnum}) == 1:
            stat = collectionmodules.find_one({"_id": allnum})["logs"]
            if stat == 'on':
                guildd = channel.guild.id
                if collectionlogschannels.count_documents({"_id": guildd}) == 1:
                    cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
                    channell = self.client.get_channel(cha)
                    embed = discord.Embed(color=discord.Color.red(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**Channel {channel.name} was deleted!**')
                    embed.set_footer(text=f"channel.id: {channel.id}")
                    await channell.send(embed=embed)
            
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        client = commands.Bot( command_prefix = '=')
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionlogschannels = db["logschannels"]
        num = channel.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        if collectionmodules.count_documents({"_id": allnum}) == 1:
            stat = collectionmodules.find_one({"_id": allnum})["logs"]
            if stat == 'on':
                guildd = channel.guild.id
                if collectionlogschannels.count_documents({"_id": guildd}) == 1:
                    cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
                    channell = self.client.get_channel(cha)
                    embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**Channel {channel.mention} was created!**')
                    embed.set_footer(text=f"channel.id: {channel.id}")
                    await channell.send(embed=embed)




    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        client = commands.Bot( command_prefix = '=')
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionlogschannels = db["logschannels"]
        num = role.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        if collectionmodules.count_documents({"_id": allnum}) == 1:
            stat = collectionmodules.find_one({"_id": allnum})["logs"]
            if stat == 'on':
                guildd = role.guild.id
                if collectionlogschannels.count_documents({"_id": guildd}) == 1:
                    cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
                    channell = self.client.get_channel(cha)
                    embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**Role was created: {role.mention}**')
                    embed.set_footer(text=f"Role id: {role.id}")
                    await channell.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        client = commands.Bot( command_prefix = '=')
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionlogschannels = db["logschannels"]
        num = role.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        if collectionmodules.count_documents({"_id": allnum}) == 1:
            stat = collectionmodules.find_one({"_id": allnum})["logs"]
            if stat == 'on':
                guildd = role.guild.id
                if collectionlogschannels.count_documents({"_id": guildd}) == 1:
                    cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
                    channell = self.client.get_channel(cha)
                    embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**Role was deleted: {role.name}**')
                    embed.set_footer(text=f"Role id: {role.id}")
                    await channell.send(embed=embed)


    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        client = commands.Bot( command_prefix = '=')
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionlogschannels = db["logschannels"]
        num = guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        if collectionmodules.count_documents({"_id": allnum}) == 1:
            stat = collectionmodules.find_one({"_id": allnum})["logs"]
            if stat == 'on':
                guildd = guild.id
                if collectionlogschannels.count_documents({"_id": guildd}) == 1:
                    cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
                    channel = self.client.get_channel(cha)
                    embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**{member} was unbanned**')
                    embed.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
                    embed.set_footer(text=f"Member ID: {member.id}")
                    await channel.send(embed=embed)

                    embe = discord.Embed(color=member.color if member.color != discord.Color.default() else discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**{member.mention}, вы разбанены**')
                    embe.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
                    embe.set_footer(text=f"Guild name: {guild.name}")
                    await member.send(embed=embe)


    @commands.Cog.listener()
    async def on_invite_create(self, invite: discord.Invite):
        client = commands.Bot( command_prefix = '=')
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"] 
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionlogschannels = db["logschannels"]
        num = invite.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        if collectionmodules.count_documents({"_id": allnum}) == 1:
            stat = collectionmodules.find_one({"_id": allnum})["logs"]
            if stat == 'on':
                guildd = invite.guild.id
                if collectionlogschannels.count_documents({"_id": guildd}) == 1:
                    cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
                    channel = self.client.get_channel(cha)
                    embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**An invite was created**')
                    embed.add_field(name='Invite Code', value=invite.code, inline=False)
                    embed.add_field(name='Max Uses', value=invite.max_uses, inline=False)
                    embed.add_field(name='Temporary', value=invite.temporary, inline=False)

                    await channel.send(embed=embed)

            

def setup(client):
    client.add_cog(user(client))
