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

#autorole
@client.command()
class AuditLogEntry(*, users, data, guild):
    channel = client.get_channel( 740117977739034634 )
    await channel.send( embed = discord.Embed( description = f'Пользователь {member.mention}, присоеденился к нам!') )
    await ctx.send('test {} and {} and {}'.format(users, date, guild))
    emb = discord.Embed( title = 'INFO', colour = discord.Color.red() )
    emb.add_field( name = 'ИНФОРМАЦИЯ',value = 'Добро пожаловать на наш сервер, ознакомьтесь с правилами нашего сервера\nПропиши команду -help что-бы узнать мои комманды\nПолезные команды:\n-help\n$help\n\n**ОБЯЗАТЕЛЬНО ПРОЧИТАЙТЕ ПРАВИЛА НА СЕРВЕРЕ И НАЖМИТЕ НА РЕАКЦИЮ 📖**')
    await member.send( embed = emb )

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
        
        
for filename in os.listdir('./cogs'): # Цикл перебирающий файлы в cogs
    client.load_extension(f'cogs.{filename[:-3]}') 
    
token= os.environ.get('BOT_TOKEN')
client.run( token )
