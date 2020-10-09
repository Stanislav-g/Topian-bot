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





    cluster = MongoClient("mongodb+srv://eco:oHZsayafcqplUdWG@topianbot.zqukb.mongodb.net/topianbot?retryWrites=true&w=majority")
    db = cluster["topianbot"]
    collection = db["money"]
    collectionmodules = db["modules"]
    collectionshop = db["shop"]
    collectionticket = db["ticket"]
    collectionlogschannels = db["logschannels"]

    #__________________________________logs_______________

    @commands.has_permissions(administrator = True)     
    @client.command()
    async def module_logs(ctx, arg = None):
        if not arg:
            await ctx.send(embed = discord.Embed(description = f"""**{ctx.author}** вы не написали что хотите сделать, включить или выключить модуль!``=module_logs on`` ``=module_logs off`` """))
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
                collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": 0, "lvls": 0, "rep": 0, "ticket": 1, "warns": 0, "logs": on})
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
                collectionmodules.insert_one({"_id": allnum, "name": name, "on_off": 0, "lvls": 0, "rep": 0, "ticket": 1, "warns": 0, "logs": off})
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
            await ctx.send(f"На данном сервере не создана база данных, ее можно создать командой")

    @client.command()
    async def log_channel(ctx, arg = None):
        name = 'economy'
        num = ctx.author.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
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
            






    @client.event
    async def on_message_delete( message ):
        num = message.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        stat = collectionmodules.find_one({"_id": allnum})["logs"]
        if stat == 'on':
            guildd = message.guild.id
            cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
            channel = client.get_channel(cha)
            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**The message is delited:**\n ``` {message.content} ``` \nAuthor: {message.author.mention}\nChannel: {message.channel.mention}')
            embed.set_footer(text=f"Message ID: {message.id}")
            await channel.send(embed=embed)

            
    @client.event
    async def on_member_ban(guild, member):
        num = guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        stat = collectionmodules.find_one({"_id": allnum})["logs"]
        if stat == 'on':
            guildd = guild.id
            cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
            channel = client.get_channel(cha)
            embed = discord.Embed(color=member.color if member.color != discord.Color.default() else discord.Color.red(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**{member.mention} is banned**')
            embed.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
            embed.set_footer(text=f"Member ID: {member.id}")
            await channel.send(embed=embed)

            embe = discord.Embed(color=member.color if member.color != discord.Color.default() else discord.Color.red(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**{member.mention}, вы забанены**')
            embe.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
            embe.set_footer(text=f"Guild name: {guild.name}")
            await member.send(embed=embe)

                            
    @client.event
    async def on_guild_channel_delete(channel):
        num = channel.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        stat = collectionmodules.find_one({"_id": allnum})["logs"]
        if stat == 'on':
            guildd = channel.guild.id
            cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
            channell = client.get_channel(cha)
            embed = discord.Embed(color=discord.Color.red(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**Channel {channel.name} is deleted!**')
            embed.set_footer(text=f"channel.id: {channel.id}")
            await channell.send(embed=embed)
            
    @client.event
    async def on_guild_channel_create(channel):
        num = channel.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        stat = collectionmodules.find_one({"_id": allnum})["logs"]
        if stat == 'on':
            guildd = channel.guild.id
            cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
            channell = client.get_channel(cha)
            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**Channel {channel.mention} is created!**')
            embed.set_footer(text=f"channel.id: {channel.id}")
            await channell.send(embed=embed)



    @client.event
    async def on_guild_channel_update(before, after):
        num = before.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        stat = collectionmodules.find_one({"_id": allnum})["logs"]
        if stat == 'on':
            guildd = before.guild.id
            cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
            channell = client.get_channel(cha)
            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**Channel update.\nBefore: {before}\nAfter: {after}**')
            await channell.send(embed=embed)

    @client.event
    async def on_guild_role_create(role):
        num = role.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        stat = collectionmodules.find_one({"_id": allnum})["logs"]
        if stat == 'on':
            guildd = role.guild.id
            cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
            channell = client.get_channel(cha)
            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**Role is created: {role.mention}**')
            embed.set_footer(text=f"Role id: {role.id}")
            await channell.send(embed=embed)

    @client.event
    async def on_guild_role_delete(role):
        num = role.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        stat = collectionmodules.find_one({"_id": allnum})["logs"]
        if stat == 'on':
            guildd = role.guild.id
            cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
            channell = client.get_channel(cha)
            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**Role is deleted: {role.name}**')
            embed.set_footer(text=f"Role id: {role.id}")
            await channell.send(embed=embed)

    @client.event
    async def on_guild_role_update(before, after):
        num = before.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        stat = collectionmodules.find_one({"_id": allnum})["logs"]
        if stat == 'on':
            guildd = before.guild.id
            cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
            channell = client.get_channel(cha)
            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**Role is update.\nBefore: {before}\nAfter: {after}**')
            await channell.send(embed=embed)

    @client.event
    async def on_member_unban(guild, member):
        num = guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        stat = collectionmodules.find_one({"_id": allnum})["logs"]
        if stat == 'on':
            guildd = guild.id
            cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
            channel = client.get_channel(cha)
            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**{member} is unbanned**')
            embed.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
            embed.set_footer(text=f"Member ID: {member.id}")
            await channel.send(embed=embed)

            embe = discord.Embed(color=member.color if member.color != discord.Color.default() else discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**{member.mention}, вы разбанены**')
            embe.set_author(name=member, icon_url=str(member.avatar_url_as(static_format='png', size=2048)))
            embe.set_footer(text=f"Guild name: {guild.name}")
            await member.send(embed=embe)
                                

    @client.event
    async def on_invite_create(invite: discord.Invite):
        num = invite.guild.id
        num2 = '111'
        allnum = str(num) + str(num2)
        stat = collectionmodules.find_one({"_id": allnum})["logs"]
        if stat == 'on':
            guildd = invite.guild.id
            cha = collectionlogschannels.find_one({"_id": guildd})["logchannel"]
            channel = client.get_channel(cha)
            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'**An invite is created**')
            embed.add_field(name='Invite Code', value=invite.code, inline=False)
            embed.add_field(name='Max Uses', value=invite.max_uses, inline=False)
            embed.add_field(name='Temporary', value=invite.temporary, inline=False)

            await channel.send(embed=embed)
       

            
    @client.event
    async def on_command_error(ctx, err):
        if isinstance(err, commands.CommandNotFound):
            await ctx.send(embed=discord.Embed(description=f"Команда не найдена!"))

        elif isinstance(err, commands.BotMissingPermissions):
            await ctx.send(
                embed=discord.Embed(description=f"У бота отсутствуют права: {' '.join(err.missing_perms)}\nВыдайте их ему для полного функционирования бота"))

        elif isinstance(err, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(description=f"У вас недостаточно прав для запуска этой команды!"))

        elif isinstance(err, commands.UserInputError):
            await ctx.send(embed=discord.Embed(description=f"Правильное использование команды {ctx.command}({ctx.command.brief}): `{ctx.command.usage}`"))

        elif isinstance(err, commands.CommandOnCooldown):
            await ctx.send(embed=discord.Embed(description=f"У вас еще не прошел кулдаун на команду {ctx.command}!\nПодождите еще {err.retry_after:.2f}"))

        else:
            await ctx.send(embed=discord.Embed(description=f"Произошла неизвестная ошибка: `{err}`\nПожалуйста, свяжитесь с разработчиками для исправления этой ошибки"))


def setup(client):
    client.add_cog(user(client))
