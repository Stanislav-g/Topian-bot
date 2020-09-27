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
   
@client.event
async def on_guild_join(guild):
    channel = client.get_channel( 747764481559494686 )
    await channel.send(f"hi")
	


@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello {}!'.format(guild.name))

@client.command()
@commands.has_permissions( administrator = True )
async def w_create(ctx, wid: int):
    chan = client.get_channel(wid)
    web=await chan.create_webhook(name='New web')
    await ctx.author.send(web.url)

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
        

            
        
for filename in os.listdir('./cogs'): # Цикл перебирающий файлы в cogs
    client.load_extension(f'cogs.{filename[:-3]}') 
 

token= os.environ.get('BOT_TOKEN')
client.run( token )
