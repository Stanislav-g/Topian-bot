import discord
from discord.ext import commands
import os
import random
import asyncio
from discord.utils import get
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
from discord.utils import find
from pymongo import MongoClient

client = commands.Bot( command_prefix = '=')
client.remove_command('help')
guild_subscriptions = True

clu= os.environ.get('MONGODB_URI')
cluster = MongoClient(clu)
db = cluster["topianbot"]
collection = db["money"]
collectionmodules = db["modules"]
collectionshop = db["shop"]
collectionticket = db["ticket"]
collectionlogschannels = db["logschannels"]
collectionreaction = db["reaction"]
collectionroles = db["roles"]
	     				
@client.event
async def on_redy():
    print( 'Bot connected')

   
@client.command()
async def servers(ctx, arg = None):
    user = int(550061958938886175)
    author = int(ctx.author.id)
    if author == user:
        for guild in client.guilds:
            await ctx.send(guild)
            await ctx.send(guild.id)

    else:
        await ctx.send(f"Вы не создатель бота!")

@client.command()
async def invite(ctx, arg = None):
    user = int(550061958938886175)
    author = int(ctx.author.id)
    if author == user:
        for guild in client.guilds:
            idi = int(guild.id)
            argd = int(arg)
            if idi == argd:
                await ctx.send(f"ok!")
                for channel in guild.text_channels:
                    if channel.permissions_for(guild.me).send_messages:
                        invite = await channel.create_invite()
                        await ctx.send(invite)
                        break
    else:
        await ctx.send(f"Вы не создатель бота!")	
	
@client.command()
async def send(ctx, arg = None, *, argg):
    user = int(550061958938886175)
    author = int(ctx.author.id)
    if author == user:
        for guild in client.guilds:
            await ctx.send(guild)
            idi = int(guild.id)
            argd = int(arg)
            if idi == argd:
                await ctx.send(f"Сообщение отправлено!")
                for channel in guild.text_channels:
                    if channel.permissions_for(guild.me).send_messages:
                        await channel.send(argg)
                        break
    else:
        await ctx.send(f"Вы не создатель бота!")
        
@client.command()
async def new(ctx, *, argg):
    if not argg:
        await ctx.send(f"=new arg")
    user = int(550061958938886175)
    author = int(ctx.author.id)
    if author == user:
        for guild in client.guilds:
             for channel in guild.text_channels:
                 if channel.permissions_for(guild.me).send_messages:
                    await channel.send(argg)
                    await ctx.send(f"Сообщение отправлено!")
                    break
    else:
        await ctx.send(f"Вы не создатель бота!")    	
	
	
	
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            message = await channel.send(embed = discord.Embed(description = f"""Привет! Я Topian Bot, чтобы узнать мои команды напиши ``=help``"""))
            invite = await channel.create_invite()

            embed = discord.Embed(title=':white_check_mark: бота пригласили на новый сервер!', type='rich', color=0x2ecc71) #Green
            embed.set_thumbnail(url=guild.icon_url)
            embed.add_field(name='Name', value=guild.name, inline=True)
            embed.add_field(name='ID', value=guild.id, inline=True)
            embed.add_field(name='Создатель сервера', value=f'{guild.owner}', inline=True)
            embed.add_field(name='Регион', value=guild.region, inline=True)
            embed.add_field(name='Людей на сервере', value=guild.member_count, inline=True)
            embed.add_field(name='Сервер создан', value=guild.created_at, inline=True)
            embed.add_field(name= 'Приглашение на сервер', value=invite, inline=True)
            channel = client.get_channel( 765246160235003936 )
            await channel.send(embed=embed)
            break

		
@client.command()
async def status(ctx, * , arg):
    user = int(550061958938886175)
    author = int(ctx.author.id)
    if author == user:    
        activity = discord.Activity(name= arg, type=discord.ActivityType.watching)
        await client.change_presence(activity=activity)	
    else:
        await ctx.send(f"Вы не создатель бота!") 
	


		
	
@client.command()
async def load(ctx, extensions):
    client.load_extensions(f'cogs.{extensions}')
    await ctx.send("loaded")

@client.command()
async def unload(ctx, extensions):
    client.unload_extension(f'cogs.{extensions}')
    await ctx.send('unloaded')
    
    
@client.command()
async def reload(ctx, extensions):
    client.unload_extension(f'cogs.{extensions}')# отгружаем ког
    client.load_extension(f'cogs.{extensions}')# загружаем 
    await ctx.send('reloaded')


    #join to channel
@client.command()
async def join(ctx):
    global voise
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'Бот присоеденился к каналу: {channel}')

    #leave from channel 
@client.command()
async def leave(ctx):
   channel = ctx.message.author.voice.channel
   voice = get(client.voice_clients, guild = ctx.guild)

   if voice and voice.is_connected():
        await voice.disconnect()
   else:
        voice = await channel.connect()
        await ctx.send(f'Бот отключился от канала: {channel}')

	
	




@client.command()
async def module_roles(ctx, arg = None):
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








@client.command()
async def autoreaction(ctx, message:int = None, role = None, reaction:str = None):  
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
        



   
@client.command()
async def delete_autoreaction(ctx, message = None, reaction = None):  
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
        


@client.event
async def on_raw_reaction_add(payload):
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
                    guild = client.get_guild(payload.guild_id)
                    role = None
                    
                    if str(payload.emoji) == reactionn: # Emoji для реакций
                        role = guild.get_role(int(rolee)) # ID Ролей для в
                        
                        if role:
                            member = guild.get_member(payload.user_id)
                            if member:
                                await member.add_roles(role)



@client.event
async def on_raw_reaction_remove(payload):
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
                    guild = client.get_guild(payload.guild_id)
                    role = None
                    
                    if str(payload.emoji) == reactionn: # Emoji для реакций
                        role = guild.get_role(int(rolee)) # ID Ролей для в
                        
                        if role:
                            member = guild.get_member(payload.user_id)
                            if member:
                                await member.remove_roles(role)

	
@client.event
async def on_command_error(ctx, err):

    if isinstance(err, commands.BotMissingPermissions):
        await ctx.send(embed=discord.Embed(description=f"У бота отсутствуют права: {' '.join(err.missing_perms)}\nВыдайте их ему для полного функционирования бота"))

    elif isinstance(err, commands.MissingPermissions):
        await ctx.send(embed=discord.Embed(description=f"У вас недостаточно прав для запуска этой команды!"))

    elif isinstance(err, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(description=f"У вас еще не прошел кулдаун на команду {ctx.command}!\nПодождите еще {err.retry_after:.2f}"))
	
    else:
        await ctx.send(embed=discord.Embed(description=f"Произошла неизвестная ошибка: `{err}`\nПожалуйста, свяжитесь с разработчиками для исправления этой ошибки"))


for filename in os.listdir('./cogs'): # Цикл перебирающий файлы в cogs
    client.load_extension(f'cogs.{filename[:-3]}') 
 

token= os.environ.get('BOT_TOKEN')
client.run( token )
