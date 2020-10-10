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


ADDRESS= os.environ.get('ADDRESS')
PASSWORD= os.environ.get('PASSWORD')



if __name__ == '__main__':
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(ADDRESS, PASSWORD)
    
   
	     				
@client.event
async def on_redy():
    print( 'Bot connected')
    user = client.get_user(550061958938886175)
    await user.send(f"embed=embed")

   
@client.command()
async def ttestt(ctx):		
    user = client.get_user(550061958938886175)
    await user.send(f"embed=embed")
    userrr = discord.utils.get(user, id = 550061958938886175)
    await userrr.send(f"embed=embed")
	
@client.event
async def on_guild_join(guild):
    client = commands.Bot( command_prefix = '=')
    userrr = discord.utils.get(user, id = 550061958938886175)
    await userrr.send(f"embed=embed")
    user = client.get_user(550061958938886175)
    await user.send(f"embed=embed")
		
		
@client.command()
@commands.has_permissions( administrator = True )
async def status(ctx, * , arg):
    activity = discord.Activity(name= arg, type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)	
	
@client.command()
@commands.has_permissions( view_audit_log = True )
async def email_send(ctx, test, * ,body):
    msg = MIMEMultipart()
    msg['From']= 'stagatin2020@gmail.com'
    msg['To']= 'nitagas2005@gmail.com'
    msg['Subject']=test
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)

@client.command()
async def emailsend(ctx, to, text, * ,body):
    msg = MIMEMultipart()
    msg['From']= 'stagatin2020@gmail.com'
    msg['To']= to
    msg['Subject']=text
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)    


		
	
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
        await ctx.send(
            embed=discord.Embed(description=f"У бота отсутствуют права: {' '.join(err.missing_perms)}\nВыдайте их ему для полного функционирования бота"))

    elif isinstance(err, commands.MissingPermissions):
        await ctx.send(embed=discord.Embed(description=f"У вас недостаточно прав для запуска этой команды!"))

    elif isinstance(err, commands.CommandOnCooldown):
        await ctx.send(embed=discord.Embed(description=f"У вас еще не прошел кулдаун на команду {ctx.command}!\nПодождите еще {err.retry_after:.2f}"))
				

        
for filename in os.listdir('./cogs'): # Цикл перебирающий файлы в cogs
    client.load_extension(f'cogs.{filename[:-3]}') 
 

token= os.environ.get('BOT_TOKEN')
client.run( token )
