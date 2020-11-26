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
from Cybernator import Paginator

client = commands.Bot( command_prefix = '=', intents = discord.Intents.default())
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
async def -=(ctx):
    await ctx.send("=-=")

@client.command()
async def help(ctx):
    embed1 = discord.Embed(title = 'Команды Бота.', description = '1 - Главная страница\n2 - Модерация.\n3 - Информация.\n4 - Игры\n5 - Модули\n6 - Поиск\n7 - Другое')
    embed2 = discord.Embed(title = 'Модерация.', description = '``=clear`` - удалить сообщения.\n``=ban`` - забанить пользователя.\n``=unban`` - разбанить пользователя.\n``=kick`` - кикнуть пользователя.\n``=emoji`` - добавить реакцию на сообщение.\n``=tempban`` - забанить пользователя на время.\n``=temp_add_role`` - добавить роль пользователю на время.\n``=add_role`` - добавить роль пользователю.\n``=del_role`` - убрать роль у пользователя.\n``=channel_create`` - создать текстовый канал.\n``=voice_create`` - создать голосовой канал.\n``=suggest`` - создать опрос.\n``=changing_name`` - поменять имя пользователю.\n``=text`` - писать от имени бота.\n``=text_emoji`` - отправить сообщение от бота с реакцией.\n``=image`` - отправлять сообщения от имени бота.')
    embed3 = discord.Embed(title = 'Информация.', description = '``=userinfo`` - инфо. о пользователе.\n``=botinfo`` - инфо. о боте.\n``=serverinfo`` - инфо. о сервере.\n``=avatar`` - аватар пользователя.\n``=ping`` - пинг бота\n``=user_boost`` - узнать давал пользователь буст или нет.\n``=info_emoji`` - info_emoji (emoji)')


    embed4 = discord.Embed(title = 'Игры.', description = """``=rps`` - камень, ножницы или бумага.\n``=guess`` - угадай число\n``=coinflip`` - орел или решка.\n``=knb`` - камень, ножницы, бумага с другим пользователем.\n``=color`` - игра, угадай цвет.""")

        
    embed5 = discord.Embed(title = 'Модули.',description = '\n``=modules`` - инфо. о использовании модулей.\n**=module_logs** - модуль логов.\n``=log_channel`` - добавить канал логов.\n**=module_rep** - модуль репутаций.\n``=rep`` - посмотреть репутацию пользователя.\n``=rep_user`` - увеличить или уменьшить репутацию пользователя.\n**=module_ticket** - модуль тикетов.\n``=ticket_create`` - создать тикет.\n``=ticket_delete`` - удалить тикет.\n``=ticket_del`` - удалить тикет, команда для администрации.\n**=module_lvls** - модуль уровней.\n``=lvl`` - посмотреть ваш уровень.\n``=message`` - посмотреть количество отправленных сообщений.\n**=module_reaction** - модуль авто-реакций.\n``=reaction_channel`` - установить канал куда будут ставиться реакции.\n``=del_reaction_channel`` - удалить канал авто реакций.\n**=module_roles** - модуль авто выдачи ролей по реакциям.\n``=auto_role`` - добавить выдачу роли по реакции, команду писать в канале где нужно поставить авто выдачу по реакции.\n``=delete_auto_role`` - убрать выдачу роли по реакции, команду писать в канале где нужно убрать авто выдачу по реакции.\n**=module_economy** - включить модуль экономики.\n``=addrole_shop`` - добавить роль в магазин.\n``=deleterole_shop`` - удалить роль из магазина.\n``=shop`` - посмотреть магазин, если нету ролей в магазине, команда отключается.\n``=buyrole`` - купить роль.\n``=balance`` - посмотреть баланс.\n``=work`` - заработать денег.\n``=profile`` - посмотреть профиль **НОВИНКА**')

    
    embed6 = discord.Embed(title = 'Поиск.', description = '``=search`` - search (запрос)\n``=youtube_search`` - youtube_search (запрос)\n``=yandex`` - yandex (запрос)\n``=wiki`` - wiki (запрос)\n``=google`` - google (запрос)')

    embed7 = discord.Embed(title = 'Другое.', description = '``=wanted`` - картинка с вашей аватаркой **НОВИНКА**\n``=num`` - рандомная цифра от 1 до 100\n``=wordnum`` - посчитать количество слов в тексте.\n``=slapperson`` - ударить пользователя.\n``=emoji_random`` - рандомное эмодзи.\n``=math`` - калькулятор.\n``=covid`` - covid\n``=ball`` - шар предсказаний.\n``=link`` - link (url)\n``=kiss`` - kiss @user\n``=reverse`` - текст задом на перед.\n``=h_coder`` - инфо. о кодировщике.\n``=bug`` - отправить бог о боте.\n``=review`` - отправить отзыв о боте.')
    embeds = [embed1, embed2, embed3, embed4, embed5, embed6, embed7]
    message = await ctx.send(embed = embed1)
    react = ['❌']
    page = Paginator(client, message, only=ctx.author, use_more=False, embeds=embeds, timeout=60, use_exit=True,exit_reaction=react)
    await page.start()
   
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
async def lines(ctx, arg = None):
    user = int(550061958938886175)
    author = int(ctx.author.id)
    if author == user:

        file = open("botfile.py", "r")
        text = len(file.readlines())


        a = str("Основной файл ") + str(text)
        await ctx.send(a)
        file.close()


		
	
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
        await ctx.send(embed=discord.Embed(description=f"Вы неправильно ввели команду или данной команды не существует!\n||{err}||"))
        guildf = ctx.guild.name
        userf = ctx.author.name
        channel = client.get_channel( 773461826696380426 )
        errorall = str(err) + str("     ") + str(guildf)
					   
        await channel.send(errorall)

@client.command()
async def cogs(ctx):
    user = int(550061958938886175)
    author = int(ctx.author.id)
    if author == user:
        for filename in os.listdir('./cogs'):
            filed = open(filename, "r")
            textd = len(filed.readlines())
            a = str("filename ") + str(textd)
            await ctx.send(a)
            filename.close()
					   
					   
for filename in os.listdir('./cogs'): # Цикл перебирающий файлы в cogs					   
    client.load_extension(f'cogs.{filename[:-3]}')

 

token= os.environ.get('BOT_TOKEN')
client.run( token )
