import discord
from discord.ext import commands
import os
import random
import asyncio
from discord.utils import get



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
    await ctx.send('unloaded')
    
    
@client.command()
async def reload(ctx, extensions):
    client.unload_extension(f'cogs.{extensions}')# отгружаем ког
    client.load_extension(f'cogs.{extensions}')# загружаем 
    await ctx.send('reloaded')

@commands.Cog.listener()
    async def clear_error( ctx, error ):
        if isinstance( error, commands.MissingRequiredArgument ):
            await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

        if isinstance( error, commands.MissingPermissions ):
            await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав ')

    @ban.error    
    async def ban_error( ctx, error ):
        if isinstance( error, commands.MissingRequiredArgument ):
            await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

        if isinstance( error, commands.MissingPermissions ):
            await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав ')

    @commands.Cog.listener()    
    async def unban_error( ctx, error ):
        if isinstance( error, commands.MissingRequiredArgument ):
            await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

        if isinstance( error, commands.MissingPermissions ):
            await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав ')
    @commands.Cog.listener()  
    async def kick_error( ctx, error ):
        if isinstance( error, commands.MissingRequiredArgument ):
            await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент')

        if isinstance( error, commands.MissingPermissions ):
            await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав ')
   
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        ignored = commands.UserInputError

        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(
                description = 'Ошибка: данная команда не существует!\nДля получения списка всевозможных доступных команд, напишите <префикс>help.',
                color = 0x800080
            )
            embed.set_footer(
                text = f'{self.client.user.name} | все права закодированы.',
                icon_url = self.bot.user.avatar_url
            )
            return await ctx.send(embed=embed)

        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                description = 'Ошибка: у вас недостаточно прав для использования данной команды!',
                color = 0x800080
            )
            embed.set_footer(
                text = f'{self.client.user.name} | все права закодированы.',
                icon_url = self.bot.user.avatar_url
            )

            return await ctx.send(embed=embed
                                  
                                  
for filename in os.listdir('./cogs'): # Цикл перебирающий файлы в cogs
    client.load_extension(f'cogs.{filename[:-3]}') 
    
token= os.environ.get('BOT_TOKEN')
client.run( token )
