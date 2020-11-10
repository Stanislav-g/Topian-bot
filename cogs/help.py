import discord
from discord.ext import commands
import datetime
from discord.utils import get
import asyncio
from time import sleep
from colorsys import hls_to_rgb
import os
import random
from random import randint, choice, choices
import io
import sqlite3
import datetime
import random as r
from Cybernator import Paginator
class user(commands.Cog):

    def __init__(self, client):
        self.client = client

    #rate: how many times the command can be used before triggering the cooldown
    rate = 1
    #per: the amount of seconds the cooldown lasts
    per = 3600


    @commands.cooldown(rate, per, commands.BucketType.user)
    @commands.command()
    async def bug(self, ctx, * ,arg = None):  
        guildf = ctx.guild.name
        userf = ctx.author.name
        if arg == None:
            await ctx.send(f"Вы забыли написать отзыв. Правильное использование: =bug (text)")
        else:
            channel = self.client.get_channel( 765195705383518220 )
            await channel.send(embed = discord.Embed(description = f"""С сервера **{guildf}**, был отправлен баг.\nБаг отправил **{userf}**\n\nБаг:\n{arg}"""))

    @commands.cooldown(rate, per, commands.BucketType.user)    
    @commands.command()
    async def review(self, ctx, * ,arg = None):  
        guildf = ctx.guild.name
        userf = ctx.author.name
        if arg == None:
            await ctx.send(f"Вы забыли написать отзыв. Правильное использование: =review (text)")
        else:
            channel = self.client.get_channel( 765195681215807499 )
            await channel.send(embed = discord.Embed(description = f"""С сервера **{guildf}**, был отправлен отзыв.\nОтзыв отправил **{userf}**\n\nОтзыв:\n{arg}"""))
            

    @commands.command(pass_context = True)
    async def help(self, ctx):
        embed1 = discord.Embed(title = 'Команды Бота.', description = '1 - Главная страница\n2 - Модерация.\n3 - Информация.\n4 - Игры\n5 - Модули\n6 - Поиск\n7 - Другое')
        embed2 = discord.Embed(title = 'Модерация.', description = '``=clear`` - удалить сообщения.\n``=ban`` - забанить пользователя.\n``=unban`` - разбанить пользователя.\n``=kick`` - кикнуть пользователя.\n``=emoji`` - добавить реакцию на сообщение.\n``=tempban`` - забанить пользователя на время.\n``=temp_add_role`` - добавить роль пользователю на время.\n``=add_role`` - добавить роль пользователю.\n``=del_role`` - убрать роль у пользователя.\n``=channel_create`` - создать текстовый канал.\n``=voice_create`` - создать голосовой канал.\n``=suggest`` - создать опрос.\n``=changing_name`` - поменять имя пользователю.\n``=text`` - писать от имени бота.\n``=text_emoji`` - отправить сообщение от бота с реакцией.\n``=image`` - отправлять сообщения от имени бота.')
        embed3 = discord.Embed(title = 'Информация.', description = '``=userinfo`` - инфо. о пользователе.\n``=botinfo`` - инфо. о боте.\n``=serverinfo`` - инфо. о сервере.\n``=avatar`` - аватар пользователя.\n``=ping`` - пинг бота\n``=user_boost`` - узнать давал пользователь буст или нет.\n``=info_emoji`` - info_emoji (emoji)')



        embed4 = discord.Embed(title = 'Игры.', description = """``=rps`` - камень, ножницы или бумага.\n``=guess`` - угадай число\n``=coinflip`` - орел или решка.\n``=knb`` - камень, ножницы, бумага с другим пользователем.\n``=color`` - игра, угадай цвет.""")

        
        embed5 = discord.Embed(title = 'Модули.',description = '\n``=modules`` - инфо. о использовании модулей.**=module_logs** - модуль логов.\n``=log_channel`` - добавить канал логов.**=module_rep** - модуль репутаций.\n``=rep`` - посмотреть репутацию пользователя.\n``=rep_user`` - увеличить или уменьшить репутацию пользователя.**=module_ticket** - модуль тикетов.\n``=ticket_create`` - создать тикет.\n``=ticket_delete`` - удалить тикет.\n``=ticket_del`` - удалить тикет, команда для администрации.**=module_lvls** - модуль уровней.\n``=lvl`` - посмотреть ваш уровень.\n``=message`` - посмотреть количество отправленных сообщений.**=module_reaction** - модуль авто-реакций.\n``=reaction_channel`` - установить канал куда будут ставиться реакции.\n``=del_reaction_channel`` - удалить канал авто реакций.**=module_roles** - модуль авто выдачи ролей по реакциям.\n``=auto_role`` - добавить выдачу роли по реакции, команду писать в канале где нужно поставить авто выдачу по реакции.\n``=delete_auto_role`` - убрать выдачу роли по реакции, команду писать в канале где нужно убрать авто выдачу по реакции.**=module_economy** - включить модуль экономики.\n``=addrole_shop`` - добавить роль в магазин.\n``=deleterole_shop`` - удалить роль из магазина.\n``=shop`` - посмотреть магазин, если нету ролей в магазине, команда отключается.\n``=buyrole`` - купить роль.\n``=balance`` - посмотреть баланс.\n``=work`` - заработать денег.\n``=profile`` - посмотреть провиль **НОВИНКА**')

        

        embed6 = discord.Embed(title = 'Поиск.', description = '\n``=search`` - search (запрос)\n``=youtube_search`` - youtube_search (запрос)\n``=yandex`` - yandex (запрос)\n``=wiki`` - wiki (запрос)\n``=google`` - google (запрос)')

        embed7 = discord.Embed(title = 'Другое.', description = '``=wanted`` - картинка с вашей аватаркой **НОВИНКА**\n``=num`` - рандомная цифра от 1 до 100\n``=wordnum`` - посчитать количество слов в тексте.\n``=slapperson`` - ударить пользователя.\n``=emoji_random`` - рандомное эмодзи.\n``=math`` - калькулятор.\n``=covid`` - covid\n``=ball`` - шар предсказаний.\n``=link`` - link (url)\n``=kiss`` - kiss @user\n``=reverse`` - текст задом на перед.\n``=h_coder`` - инфо. о кодировщике.\n``=bug`` - отправить бог о боте.\n``=review`` - отправить отзыв о боте.')
        embeds = [embed1, embed2, embed3, embed4, embed5, embed6, embed7]
        message = await ctx.send(embed = embed1)
        react = ['❌']
        page = Paginator(client, message, only=ctx.author, use_more=False, embeds=embeds, timeout=60, use_exit=True,exit_reaction=react)
        await page.start()







    @commands.command()
    async def h_coder(self, ctx ):
        await ctx.channel.purge( limit = 1 )
        emb = discord.Embed( title = '**Кодировщик**', colour= 0x808080)
        emb.add_field( name = 'CODER',value = '=coder encode (text) - зашифровать\n=coder decode (text) расшифровать') 
        emb.set_footer(text='Команда вызвана: {}\n© Copyright 2020 Topian Team | Все права закодированы'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
        await ctx.send( embed = emb )  


    
    @commands.command(pass_context = True)
    async def helphelp(self, ctx): 
        await ctx.send(embed = discord.Embed(description = f"{ctx.author.mention}, я отправил список команд тебе в личку!"))
        await ctx.author.send(embed = discord.Embed(description = f"""**Moderation**
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
        
        await ctx.author.send(embed = discord.Embed(description = f"""
                **Games**
                ``=rps`` - камень, ножницы или бумага.
                ``=guess`` - угадай число
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

        await ctx.author.send(embed = discord.Embed(description = f"""                
                **Modules**
                ``=modules`` - инфо. о использовании модулей.
                **=module_logs** - модуль логов.
                ``=log_channel`` - добавить канал логов.
                **=module_rep** - модуль репутаций.
                ``=rep`` - посмотреть репутацию пользователя.
                ``=rep_user`` - увеличить или уменьшить репутацию пользователя.
                **=module_ticket** - модуль тикетов.
                ``=ticket_create`` - создать тикет.
                ``=ticket_delete`` - удалить тикет.
                ``=ticket_del`` - удалить тикет, команда для администрации.
                **=module_lvls** - модуль уровней.
                ``=lvl`` - посмотреть ваш уровень.
                ``=message`` - посмотреть количество отправленных сообщений.
                **=module_reaction** - модуль авто-реакций.
                ``=reaction_channel`` - установить канал куда будут ставиться реакции.
                ``=del_reaction_channel`` - удалить канал авто реакций.
                **=module_roles** - модуль авто выдачи ролей по реакциям.
                ``=auto_role`` - добавить выдачу роли по реакции, команду писать в канале где нужно поставить авто выдачу по реакции.
                ``=delete_auto_role`` - убрать выдачу роли по реакции, команду писать в канале где нужно убрать авто выдачу по реакции.
                **=module_economy** - включить модуль экономики.
                ``=addrole_shop`` - добавить роль в магазин.
                ``=deleterole_shop`` - удалить роль из магазина.
                ``=shop`` - посмотреть магазин, если нету ролей в магазине, команда отключается.
                ``=buyrole`` - купить роль.
                ``=balance`` - посмотреть баланс.
                ``=work`` - заработать денег.
                     ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍        ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍‍    ‌‌‍
                """))    


    @commands.command()
    async def modules(self, ctx):
        emt = discord.Embed(title=f"Информация об использовании модулей.",description="Чтобы включить модуль, напишите следующую команду: =module_(имя модуля) on\nЧтобы отключить модуль, напишите следующую команду: =module_(имя модуля) off", color = 0x00FF00)
        emt.add_field(name=f'``=module_logs on``', value="Включить модуль логов", inline=True)  # Создает строку
        emt.add_field(name=f'``=module_logs off``', value="Отключить модуль логов", inline=True)  # Создает строку
        emt.add_field(name=f'``=module_rep on``', value="Включить модуль репутаций", inline=True)  # Создает строку
        emt.add_field(name=f'``=module_rep off``', value="Отключить модуль репутаций", inline=True)  # Создает строку
        emt.add_field(name=f'``=module_ticket on``', value="Включить модуль тикетов", inline=True)  # Создает строку
        emt.add_field(name=f'``=module_ticket off``', value="Отключить модуль тикетов", inline=True)  # Создает строку
        emt.add_field(name=f'``=module_reaction on``', value="Включить модуль авто-реакций", inline=True)  # Создает строку
        emt.add_field(name=f'``=module_reaction off``', value="Отключить модуль авто-реакций", inline=True)  # Создает строку
        emt.add_field(name=f'``=module_lvls on``', value="Включить модуль уровней", inline=True)  # Создает строку
        emt.add_field(name=f'``=module_lvls off``', value="Отключить модуль уровней", inline=True)  # Создает строку
        emt.add_field(name=f'``=module_roles on``', value="Включить модуль авто выдачи ролей по реакциям", inline=True)  # Создает строку
        emt.add_field(name=f'``=module_roles off``', value="Отключить модуль авто выдачи ролей по реакциям", inline=True)  # Создает строку
        emt.add_field(name=f'``=module_economy on``', value="Включить модуль авто выдачи ролей по реакциям", inline=True)  # Создает строку
        emt.add_field(name=f'``=module_economy off``', value="Отключить модуль авто выдачи ролей по реакциям", inline=True)  # Создает строку
        await ctx.send(embed=emt)
          
 

        
    @commands.command()
    @commands.has_permissions( administrator = True )
    async def log(self, ctx, num : int = None, member: discord.Member = None ):
        guild = ctx.message.guild
        if member == None:
            async for entry in guild.audit_logs(limit= num):
                emb = discord.Embed( title = 'Logs', colour = discord.Color.red() )
                emb.add_field( name = 'logs',value = '**{0.user}** did {0.action} to **{0.target}** *{0.before}* to *{0.after}*'.format(entry))
                await ctx.send( embed = emb )
        else:
            entries = await guild.audit_logs(limit=None, user=guild.me).flatten()
            await ctx.send('I made {} moderation actions.'.format(len(entries)))
    

    @commands.command()
    async def coder(self, ctx, vibor, * , word):        
        letters = len(word)
        let = 0
        lttte = letters
        bukvi = ['1','2','3','4','5','6','7','8','9','0','&','%','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',',','.','-',' ','!','?']
        excl = ('|')
        myfile = open("words.txt", "w")


        if vibor == 'encode':
            while True:
                if word[let] in bukvi:
                    if word[let] == 'a':
                        myfile.write("b")
                    elif word[let] == 'b':
                        myfile.write("c")
                    elif word[let] == 'c':
                        myfile.write("d")
                    elif word[let] == 'd':
                        myfile.write("e")
                    elif word[let] == 'e':
                        myfile.write("f")
                    elif word[let] == 'f':
                        myfile.write("g")
                    elif word[let] == 'g':
                        myfile.write("h")
                    elif word[let] == 'h':
                        myfile.write("l")
                    elif word[let] == 'l':
                        myfile.write("k")
                    elif word[let] == 'k':
                        myfile.write("m")
                    elif word[let] == 'm':
                        myfile.write("n")
                    elif word[let] == 'n':
                        myfile.write("o")
                    elif word[let] == 'o':
                        myfile.write("p")
                    elif word[let] == 'p':
                        myfile.write("r")
                    elif word[let] == 'r':
                        myfile.write("s")
                    elif word[let] == 's':
                        myfile.write("t")
                    elif word[let] == 't':
                        myfile.write("q")
                    elif word[let] == 'q':
                        myfile.write("w")
                    elif word[let] == 'w':
                        myfile.write("y")
                    elif word[let] == 'y':
                        myfile.write("u")
                    elif word[let] == 'u':
                        myfile.write("j")
                    elif word[let] == 'j':
                        myfile.write("z")
                    elif word[let] == 'z':
                        myfile.write("x")
                    elif word[let] == 'x':
                        myfile.write("v")
                    elif word[let] == 'v':
                        myfile.write(",")
                    elif word[let] == ',':
                        myfile.write(".")
                    elif word[let] == '.':
                        myfile.write("-")
                    elif word[let] == '-':
                        myfile.write(" ")
                    elif word[let] == ' ':
                        myfile.write("!")
                    elif word[let] == '!':
                        myfile.write("?")
                    elif word[let] == '?':
                        myfile.write("i")
                    elif word[let] == 'i':
                        myfile.write("a")
                        
                    if word[let] == 'A':
                        myfile.write("B")
                    elif word[let] == 'B':
                        myfile.write("C")
                    elif word[let] == 'C':
                        myfile.write("D")
                    elif word[let] == 'D':
                        myfile.write("E")
                    elif word[let] == 'E':
                        myfile.write("F")
                    elif word[let] == 'F':
                        myfile.write("G")
                    elif word[let] == 'G':
                        myfile.write("H")
                    elif word[let] == 'H':
                        myfile.write("L")
                    elif word[let] == 'L':
                        myfile.write("K")
                    elif word[let] == 'K':
                        myfile.write("M")
                    elif word[let] == 'M':
                        myfile.write("N")
                    elif word[let] == 'N':
                        myfile.write("O")
                    elif word[let] == 'O':
                        myfile.write("P")
                    elif word[let] == 'P':
                        myfile.write("R")
                    elif word[let] == 'R':
                        myfile.write("S")
                    elif word[let] == 'S':
                        myfile.write("T")
                    elif word[let] == 'T':
                        myfile.write("Q")
                    elif word[let] == 'Q':
                        myfile.write("W")
                    elif word[let] == 'W':
                        myfile.write("Y")
                    elif word[let] == 'Y':
                        myfile.write("U")
                    elif word[let] == 'U':
                        myfile.write("J")
                    elif word[let] == 'J':
                        myfile.write("Z")
                    elif word[let] == 'Z':
                        myfile.write("X")
                    elif word[let] == 'X':
                        myfile.write("V")
                    elif word[let] == 'V':
                        myfile.write("&")
                    elif word[let] == 'I':
                        myfile.write("A")

                    elif word[let] == '1':
                        myfile.write("2")
                    elif word[let] == '2':
                        myfile.write("3")
                    elif word[let] == '3':
                        myfile.write("4")
                    elif word[let] == '4':
                        myfile.write("5")
                    elif word[let] == '5':
                        myfile.write("6")
                    elif word[let] == '6':
                        myfile.write("7")
                    elif word[let] == '7':
                        myfile.write("8")
                    elif word[let] == '8':
                        myfile.write("9")
                    elif word[let] == '9':
                        myfile.write("0")
                    elif word[let] == '0':
                        myfile.write("1")
                    
                let = let + 1
                if let == lttte:
                    myfile.close()
                    break

        if vibor == 'decode':
            while True:
                if word[let] in bukvi:
                    if word[let] == 'b':
                        myfile.write("a")
                    elif word[let] == 'c':
                        myfile.write("b")
                    elif word[let] == 'd':
                        myfile.write("c")
                    elif word[let] == 'e':
                        myfile.write("d")
                    elif word[let] == 'f':
                        myfile.write("e")
                    elif word[let] == 'g':
                        myfile.write("f")
                    elif word[let] == 'h':
                        myfile.write("g")
                    elif word[let] == 'l':
                        myfile.write("h")
                    elif word[let] == 'k':
                        myfile.write("l")
                    elif word[let] == 'm':
                        myfile.write("k")
                    elif word[let] == 'n':
                        myfile.write("m")
                    elif word[let] == 'o':
                        myfile.write("n")
                    elif word[let] == 'p':
                        myfile.write("o")
                    elif word[let] == 'r':
                        myfile.write("p")
                    elif word[let] == 's':
                        myfile.write("r")
                    elif word[let] == 't':
                        myfile.write("s")
                    elif word[let] == 'q':
                        myfile.write("t")
                    elif word[let] == 'w':
                        myfile.write("q")
                    elif word[let] == 'y':
                        myfile.write("w")
                    elif word[let] == 'u':
                        myfile.write("y")
                    elif word[let] == 'j':
                        myfile.write("u")
                    elif word[let] == 'z':
                        myfile.write("j")
                    elif word[let] == 'x':
                        myfile.write("z")
                    elif word[let] == 'v':
                        myfile.write("x")
                    elif word[let] == ',':
                        myfile.write("v")
                    elif word[let] == '.':
                        myfile.write(",")
                    elif word[let] == '-':
                        myfile.write(".")
                    elif word[let] == ' ':
                        myfile.write("-")
                    elif word[let] == '!':
                        myfile.write(" ")
                    elif word[let] == '?':
                        myfile.write("!")
                    elif word[let] == 'i':
                        myfile.write("?")
                    elif word[let] == 'a':
                        myfile.write("i")
                        
                    
                    elif word[let] == 'B':
                        myfile.write("A")
                    elif word[let] == 'C':
                        myfile.write("B")
                    elif word[let] == 'D':
                        myfile.write("C")
                    elif word[let] == 'E':
                        myfile.write("D")
                    elif word[let] == 'F':
                        myfile.write("E")
                    elif word[let] == 'G':
                        myfile.write("F")
                    elif word[let] == 'H':
                        myfile.write("G")
                    elif word[let] == 'L':
                        myfile.write("H")
                    elif word[let] == 'K':
                        myfile.write("L")
                    elif word[let] == 'M':
                        myfile.write("K")
                    elif word[let] == 'N':
                        myfile.write("M")
                    elif word[let] == 'O':
                        myfile.write("N")
                    elif word[let] == 'P':
                        myfile.write("O")
                    elif word[let] == 'R':
                        myfile.write("P")
                    elif word[let] == 'S':
                        myfile.write("R")
                    elif word[let] == 'T':
                        myfile.write("S")
                    elif word[let] == 'Q':
                        myfile.write("T")
                    elif word[let] == 'W':
                        myfile.write("Q")
                    elif word[let] == 'Y':
                        myfile.write("W")
                    elif word[let] == 'U':
                        myfile.write("Y")
                    elif word[let] == 'J':
                        myfile.write("U")
                    elif word[let] == 'Z':
                        myfile.write("J")
                    elif word[let] == 'X':
                        myfile.write("Z")
                    elif word[let] == 'V':
                        myfile.write("X")
                    elif word[let] == '&':
                        myfile.write("V")
                    elif word[let] == 'A':
                        myfile.write("I")


                    elif word[let] == '2':
                        myfile.write("1")
                    elif word[let] == '3':
                        myfile.write("2")
                    elif word[let] == '4':
                        myfile.write("3")
                    elif word[let] == '5':
                        myfile.write("4")
                    elif word[let] == '6':
                        myfile.write("5")
                    elif word[let] == '7':
                        myfile.write("6")
                    elif word[let] == '8':
                        myfile.write("7")
                    elif word[let] == '9':
                        myfile.write("8")
                    elif word[let] == '0':
                        myfile.write("9")
                    elif word[let] == '1':
                        myfile.write("0")
                let = let + 1
                if let == lttte:
                    myfile.close()
                    break
                
        
        myfile2 = open("words.txt", "r")    
        cont=myfile2.read()
        await ctx.send(cont)
        myfile2.close()
  

    @commands.command()
    async def test(self, ctx):
        await ctx.send(f'12345')

            
def setup(client):
    client.add_cog(user(client))
