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
            owner = message.guild.owner
            overwrites = {
                owner: discord.PermissionOverwrite(read_messages=True, send_messages=True),
                message.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_channels=True, manage_roles=True),
                message.guild.default_role: discord.PermissionOverwrite(
                read_messages=False)
            }

            ticket = await message.guild.create_text_channel(
                name='Topian Bot info.',
                overwrites=overwrites,
                topic=f'Information',
                    eason=f'Information'
            )
            await ticket.send(embed = discord.Embed(description = f"""**Moderation**
                    ``=clear`` - удалить сообщения.
                    ``=ban`` - забанить пользователя.
                    ``=unban`` - разбанить пользователя.
                    ``=kick`` - кикнуть пользователя.
                    ``=emoji`` - добавить реакцию на сообщение.
                    ``=tempban`` - забанить пользователя на время.
                    ``=temp_add_role`` - добавить роль пользователю на время.
                    ``=add_role`` - добавить роль пользователю.
                    ``=del_role`` - убрать роль у пользователя.
                    ``=channel_create`` - создать текстовый канал.
                    ``=voice_create`` - создать голосовой канал.
                    ``=suggest`` - создать опрос.
                    ``=changing_name`` - поменять имя пользователю.
                    ``=text`` - писать от имени бота.
                    ``=text_emoji`` - отправить сообщение от бота с реакцией.
                    ``=image`` - отправлять сообщения от имени бота.
                     
                    **Info**
                    ``=userinfo`` - инфо. о пользователе.
                    ``=botinfo`` - инфо. о боте.
                    ``=serverinfo`` - инфо. о сервере.
                    ``=avatar`` - аватар пользователя.
                    ``=ping`` - пинг бота
                    ``=user_boost`` - узнать давал пользователь буст или нет.
                    ``=info_emoji`` - info_emoji (emoji)
                    **Search**
                    ``=search`` - search (запрос)
                    ``=youtube_search`` - youtube_search (запрос)
                    ``=yandex`` - yandex (запрос)
                    ``=wiki`` - wiki (запрос)
                    ``=google`` - google (запрос)
                         ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍        ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍
                    """))
            
            await ticket.send(embed = discord.Embed(description = f"""
                    **Games**
                    ``=rps`` - камень, ножницы или бумага.
                    ``=угадайка`` - угадайка* (НЕ ДОСТУПНО)
                    ``=coinflip`` - орел или решка.
                    ``=knb`` - камень, ножницы, бумага с другим пользователем.
                    ``=color`` - игра, угадай цвет.
                    **Other**
                    ``=num`` - рандомная цифра от 1 до 100
                    ``=wordnum`` - посчитать количество слов в тексте.
                    ``=slapperson`` - ударить пользователя.
                    ``=emoji_random`` - рандомное эмодзи.
                    ``=math`` - калькулятор.
                    ``=covid`` - covid
                    ``=ball`` - шар предсказаний.
                    ``=link`` - link (url)
                    ``=kiss`` - kiss @user
                    ``=reverse`` - текст задом на перед.
                    ``=h_coder`` - инфо. о кодировщике.
                    ``=bug`` - отправить бог о боте.
                    ``=review`` - отправить отзыв о боте.
                         ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍        ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍
                    """))

            await ticket.send(embed = discord.Embed(description = f"""                
                    **Modules**
                    ``=modules`` - инфо. о использовании модулей.
                    ``=module_logs`` - модуль логов.
                    ``=log_channel`` - добавить канал логов.
                    ``=module_rep`` - модуль репутаций.
                    ``=rep`` - посмотреть репутацию пользователя.
                    ``=rep_user`` - увеличить или уменьшить репутацию пользователя.
                    ``=module_ticket`` - модуль тикетов.
                    ``=ticket_create`` - создать тикет.
                    ``=ticket_delete`` - удалить тикет.
                    ``=ticket_del`` - удалить тикет, команда для администрации.
                    ``=module_lvls`` - модуль уровней.
                    ``=lvl`` - посмотреть ваш уровень.
                    ``=message`` - посмотреть количество отправленных сообщений.
                    ``=module_reaction`` - модуль авто-реакций.
                    ``=reaction_channel`` - установить канал куда будут ставиться реакции.‌‌‍
                         ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍        ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍
                    """))
            await ticket.send(embed = discord.Embed(description = f"""Мой сервер поддежки:  https://discord.gg/Vnb57MM"""))
            embed = discord.Embed(title=':white_check_mark: бота пригласили на новый сервер!', type='rich', color=0x2ecc71) #Green
            embed.set_thumbnail(url=guild.icon_url)
            embed.add_field(name='Name', value=guild.name, inline=True)
            embed.add_field(name='ID', value=guild.id, inline=True)
            embed.add_field(name='Создатель сервера', value=f'{guild.owner} ({guild.owner.id})', inline=True)
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
	
    else:
        await ctx.send(embed=discord.Embed(description=f"Произошла неизвестная ошибка: `{err}`\nПожалуйста, свяжитесь с разработчиками для исправления этой ошибки"))

			

        
for filename in os.listdir('./cogs'): # Цикл перебирающий файлы в cogs
    client.load_extension(f'cogs.{filename[:-3]}') 
 

token= os.environ.get('BOT_TOKEN')
client.run( token )
