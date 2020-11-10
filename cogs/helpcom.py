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
        page = Paginator(self.client, message, only=ctx.author, use_more=False, embeds=embeds, timeout=60, use_exit=True,exit_reaction=react, color=#7FFF00)
        await page.start()


    @commands.command()
    async def tegdntst(self, ctx):
        await ctx.send(f'12345')

            
def setup(client):
    client.add_cog(user(client))
