import discord
from discord.ext import commands
import os
import random
import asyncio




client = commands.Bot( command_prefix = '-')
client.remove_command('help')

@client.event
async def on_redy():
    print( 'Bot connected')



@client.command()
async def load(ctx, extensions):
    client.load_extensions(f'cogs.{extensions}')
    await ctx.send("loaded")

@client.command()
async def unload(ctx, extensions):
    client.unload_extension(f'cogs.{extensions}')
    await ctx.send('unloaded'

for filename in os.listdir('./cogs')
if filename.endswith('.py')
client.load_extension(f'cogs.{filename[:-3]}') 

    
token= os.environ.get('BOT_TOKEN')
client.run( token )
