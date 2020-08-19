import discord
from discord.ext import commands
import os
import random
import asyncio
from discord.utils import get



client = commands.Bot( command_prefix = '=')
client.remove_command('help')

@client.event
async def on_redy():
    print( 'Bot connected')
    
@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id == 745665708008013884: # ID Сообщения
        guild = client.get_guild(payload.guild_id)
        role = None

        if str(payload.emoji) == '🍰': # Emoji для реакций
            role = guild.get_role(745625103416688652) # ID Ролей для выдачи

        if role:
            member = guild.get_member(payload.user_id)
            if member:
                await member.add_roles(role)  
                    
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
