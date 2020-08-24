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
import random as r
import requests
class user(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command( pass_context = True )
    async def num(self, ctx ):
        await ctx.send(random.randint(1,101))

    @commands.command()
    async def wordnum(self, ctx, *args):
        await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))



    @commands.command()
    async def slapperson(self, ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
        slapped = ", ".join(x.name for x in members)
        gif = random.choice(['https://tenor.com/view/back-slap-backhand-funny-animals-penguin-slap-gif-11724800','https://tenor.com/view/slap-bears-gif-10422113','https://tenor.com/view/gap-slapped-knockout-punch-gif-5122019','https://tenor.com/view/kevin-hart-slap-face-your-gif-10570690'])
        await ctx.send('{} ,был ударен участником {} {}'.format(slapped, ctx.author, reason))
        await ctx.send(gif)
        
        
    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        gif = random.choice(['https://tenor.com/view/kiss-love-anime-gif-12837192','https://tenor.com/view/anime-kiss-love-sweet-gif-5095865'])
        embed = discord.Embed(title=f"{ctx.author}, поцеловал {member.name}", description= " ")
        await ctx.send(embed=embed)
        await ctx.send(gif)


    #math
    @commands.command()
    async def math(self, ctx, a : int, arg, b : int ):
        try:
            if arg == '+':
                await ctx.send(embed = discord.Embed(description = f'**:bookmark_tabs: Результат:** { a + b }', color=0x0c0c0c))  

            elif arg == '-':
                await ctx.send(embed = discord.Embed(description = f'**:bookmark_tabs: Результат:** { a - b }', color=0x0c0c0c))  

            elif arg == '/':
                await ctx.send(embed = discord.Embed(description = f'**:bookmark_tabs: Результат:** { a / b }', color=0x0c0c0c))

            elif arg == '*':
                await ctx.send(embed = discord.Embed(description = f'**:bookmark_tabs: Результат:** { a * b }', color=0x0c0c0c))      

        except:       
            await ctx.send(embed = discord.Embed(description = f'**:exclamation: Произошла ошибка.**', color=0x0c0c0c))

    #emoji
    @commands.command()
    async def emoji_random(self, ctx ):
        a = random.choice([':ghost:',':skull_crossbones:',':poop: ',':upside_down: ',':face_with_raised_eyebrow:',':nerd:',':face_with_monocle:',':tired_face:',':confounded:',':exploding_head:',':face_with_symbols_over_mouth:',':hot_face:',':cold_face:',':rage:',':cowboy:',':clown:',':space_invader:',':fox:',':chicken:',':penguin:',':comet:',':bow_and_arrow:',':tv:',':money_with_wings:',':gem:',':gun:',':bomb:',':firecracker:',':knife:',':toilet:',':test_tube:',':microbe:'])
        await ctx.send( a )


    @commands.command()
    async def covid(self, ctx):   
        await ctx.send(f'https://www.worldometers.info/coronavirus/')

    #ball    
    @commands.command()
    async def ball(self, ctx, arg = None):
        embe = discord.Embed( title = random.choice(['Да :8ball: ','Нет :8ball: ','Может быть','Думаю нет','Думаю да','Хорошо','Не сейчас','Позже','Сложный вопрос','Не знаю','Надо подумать','Потом','Ты шутишь?','Конечно, да!']), colour = discord.Color.red() )
        await ctx.send(embed=embe)

    #link     
    @commands.command()
    async def link(self, ctx, url ):
        r = requests.get(url)
        if r.status_code == 404:
            await ctx.message.delete()
            await ctx.send(f"Ссылка не работает")
        else:
            await ctx.send(f"Ссылка работает")

    ev_player = [''] #игроки в розыгрыше
    start_ev = 0 #перемычка

    #event_roles
    @commands.command()
    async def event_roles(self, ctx, role: discord.Role = None, member: discord.Member = None, amount: int = None):
        global ev_player
        global start_ev
        if role is None:
            await ctx.send('**Упомяните роль для розыгрыша.**' '\n' '`/event_roles [role]`')
            return  
        start_ev = 1
        await ctx.send(f'Администратор запустил розыгрыш роли {role.mention}. Для участия пропишите `-уч`.' '\n' f"**Розыгрыш состоится через 1 час.**")
        await asyncio.sleep(3600)
        ev_win = r.choice(ev_player)
        member = ev_win
        await ctx.send(f'**Поздравляем {ev_win.mention}! Он выигрывает в розыгрыше и получает роль {role.mention}.**')
        await ev_win.add_roles(role)
        ev_player = ['']
        start_ev = 0

    #mp
    @commands.command()
    async def уч(self, ctx):
        global ev_player
        global start_ev
        author = ctx.message.author
        if start_ev == 0:
            await ctx.send('**Сейчас нету розыгрыша ролей!**')
            return
        if author in ev_player:
            await ctx.send('Вы уже приняли участие в этом розыгрыше!')
            return
        else:
            ev_player.append(author)
            print(f'Игрок {author} принял участие в розыгрыши роли.')
            await ctx.send(embed = discord.Embed(description = f'**{author.mention}, Вы успешно приняли участие в розыгрыши роли!**', color = 0xee3131))
            print('Розыгрыш роли завершен.')  
            
    @commands.command()
    async def info_emoji(self, ctx, emoji: discord.Emoji = None):
        if not emoji:
            e = discord.Embed(description = ":x: {0}, укажи **эмодзи**, о которым хочешь узнать **информацию** :x:".format(ctx.author.mention), color = 0xFF0000)

            e.set_footer(text = f'{client.user.name} © 2020 | Все права защищены', icon_url = client.user.avatar_url)
            e.timestamp = datetime.utcnow()

            await ctx.send(embed = e)

        e = discord.Embed(description = f"[Эмодзи]({emoji.url}) сервера - {emoji}", color = 0x00FF00)

        e.add_field(name = "Название эмодзи:", value = "**`{0}`**".format(emoji.name))
        e.add_field(name = "Автор:", value = "{0}".format((await ctx.guild.fetch_emoji(emoji.id)).user.mention))
        e.add_field(name = "‎‎‎‎", value = "‎‎‎‎")
        e.add_field(name = "Дата добавления:", value = "**`{0}`**".format((emoji.created_at.date())))
        e.add_field(name = "ID эмодзи:", value = "**`{0}`**".format(emoji.id))
        e.add_field(name = "‎‎‎‎", value = "‎‎‎‎")
        e.set_thumbnail(url = "{0}".format(emoji.url))
        e.set_author(icon_url = 'https://www.flaticon.com/premium-icon/icons/svg/3084/3084443.svg', name = 'Бот | Эмодзи')
        e.set_footer(text = f'{client.user.name} © 2020 | Все права защищены', icon_url = client.user.avatar_url)
        e.timestamp = datetime.utcnow()

        await ctx.send(embed = e)   
        
    @commands.command(name='weather', aliases=['погода'])
    async def weather(self, ctx, city: str = None):
        if not city:
            await ctx.send(embed = discord.Embed(description="**Ты не указал город -_-**", colour=discord.Color.from_rgb(47, 49, 54)))
            await ctx.message.add_reaction("🔴")
        else:
            owm = pyowm.OWM('api key')
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(city)
            w = observation.weather
            temp = w.temperature('celsius')["temp"]
            temp_max = w.temperature('celsius')["temp_max"]
            temp_min = w.temperature('celsius')["temp_min"]
            feels_like = w.temperature('celsius')["feels_like"]

            embed = discord.Embed(
                colour=discord.Color.from_rgb(47, 49, 54),
                description=f"**Погода в городе {city}**",
                timestamp=ctx.message.created_at
            )
            embed.set_thumbnail(url="https://avatars.mds.yandex.net/get-pdb/752643/d215f5fe-77ec-4923-aea7-b2184f2b6598/orig")
            embed.add_field(name="Температура", value=f"{temp} °С")
            embed.add_field(name="Ощущается как", value=f"{feels_like} °С")
            embed.add_field(name="Максимальная температура", value=f"{temp_max} °С")
            embed.add_field(name="Минимальная температура", value=f"{temp} °С")
            await ctx.send(embed=embed)
            await ctx.message.add_reaction("🟢")

    @commands.command()
    async def image(self, ctx):
        files = []
        for file in ctx.message.attachments:
            fp = io.BytesIO()
            await file.save(fp)
            files.append(discord.File(fp, filename = file.filename, spoiler = file.is_spoiler()))
        await ctx.send(files = files)    
        
def setup(client):
    client.add_cog(user(client))
