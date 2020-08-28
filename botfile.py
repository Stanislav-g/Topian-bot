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
    
client = commands.Bot( command_prefix = '=')
client.remove_command('help')


ADDRESS= os.environ.get('ADDRESS')
PASSWORD= os.environ.get('PASSWORD')



if __name__ == '__main__':
	s.settimeout(0.0)
	s = smtplib.SMTP(host='smtp.gmail.com', port=587)
	s.starttls()
	s.login(ADDRESS, PASSWORD)
	     				
@client.event
async def on_redy():
    print( 'Bot connected')
   

	
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
async def on_raw_reaction_add(payload):
    if payload.message_id == 745689538608758806: # ID Сообщения
        guild = client.get_guild(payload.guild_id)
        role = None

        if str(payload.emoji) == '1️⃣': # Emoji для реакций
            role = guild.get_role(745685081489801246) # ID Ролей для выдачи
        elif str(payload.emoji) == '2️⃣':
            role = guild.get_role(745685081506709674)
        elif str(payload.emoji) == '3️⃣':
            role = guild.get_role(745685081548652594)
        elif str(payload.emoji) == '4️⃣':
            role = guild.get_role(745687846576455832)
            
        if role:
            member = guild.get_member(payload.user_id)
            if member:
                await member.add_roles(role)          
        
for filename in os.listdir('./cogs'): # Цикл перебирающий файлы в cogs
    client.load_extension(f'cogs.{filename[:-3]}') 
 

token= os.environ.get('BOT_TOKEN')
client.run( token )
