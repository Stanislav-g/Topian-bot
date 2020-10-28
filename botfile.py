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

client = commands.Bot( command_prefix = '=', intents = discord.Intents.all())
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
