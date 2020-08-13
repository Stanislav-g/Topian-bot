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

class user(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def color(self, ctx, amount: int):
        if amount == 1:
            await ctx.send(f"Приготовься, до старта 5 секунд!")
            await asyncio.sleep(5)
            await ctx.send(f"🟥 - 1 \n🟧 - 2\n🟨 - 3\n🟩 - 4")
            await asyncio.sleep(1)
            await ctx.send(f"3")
            await asyncio.sleep(1)
            await ctx.send(f"2")
            await asyncio.sleep(1)
            await ctx.send(f"1")
            await asyncio.sleep(1)
            await ctx.channel.purge(limit = 4)
            await ctx.send(f"что было под номером 3?")
            embed = discord.Embed(title=f"{ctx.author.name}  что было под номером 3?", description= f" 🟥 🟧 🟨 🟩 \n\n")
            message = await ctx.send(embed=embed)
            await message.add_reaction('🟥')
            await message.add_reaction('🟧')
            await message.add_reaction('🟨')
            await message.add_reaction('🟩') 
            async def on_reaction_add(emoji, user):
                if emoji == '🟨':
                    await ctx.send(f"fin")
                   
    #rps
    @commands.command()
    async def rps(self, ctx, *, mess):
        robot = ['Камень', 'Ножницы', 'Бумага']
        if mess == "Камень" or mess == "К" or mess == "камень" or mess == "к":
            robot_choice = random.choice(robot)
            emb = discord.Embed(title = robot_choice, colour = discord.Colour.lighter_grey())
            if robot_choice == 'Ножницы':
                emb.add_field(name = ':scissors:', value = 'Вы выиграли!')
            elif robot_choice == 'Бумага':
                emb.add_field(name = ':scroll:', value = 'Вы проиграли :с')
            else:
                emb.add_field(name = ':moyai:', value = 'Ничья!')
            await ctx.send(embed = emb)

        elif mess == "Бумага" or mess == "Б" or mess == "бумага" or mess == "б":
            robot_choice = random.choice(robot)
            emb = discord.Embed(title = robot_choice, colour = discord.Colour.lighter_grey())
            if robot_choice == 'Ножницы':
                emb.add_field(name = 'scissors:', value = 'Вы проиграли :с')
            elif robot_choice == 'Камень':
                emb.add_field(name = ':moyai:', value = 'Вы выиграли!')
            else:
                emb.add_field(name = '::scroll:', value = 'Ничья!')
            await ctx.send(embed = emb)

        elif mess == "Ножницы" or mess == "Н" or mess == "ножницы" or mess == "н":
            robot_choice = random.choice(robot)
            emb = discord.Embed(title = robot_choice, colour = discord.Colour.lighter_grey())
            if robot_choice == 'Бумага':
                emb.add_field(name = ':scroll:', value = 'Вы выиграли!')
            elif robot_choice == 'Камень':
                emb.add_field(name = ':moyai:', value = 'Вы проиграли :с')
            else:
                emb.add_field(name = ':scissors:', value = 'Ничья!')
            await ctx.send(embed = emb)
    #knb
    @commands.command()
    async def knb(self, ctx, member: discord.Member = None):
        a = random.choice([':moyai: камень',':scissors: ножницы',':scroll: бумага'])
        v = random.choice([':moyai: камень',':scissors: ножницы',':scroll: бумага'])
        if Member == None:
             embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
             embw.add_field( name = 'knb',value = '**knb** = knb @user')
             await ctx.send( embed = embw )
        else:    
            emb = discord.Embed( title = 'Камень, ножницы, бумага', colour = discord.Color.blue() )

            await ctx.send( embed = emb )

            emg = discord.Embed( title = f'{ member.name}', colour = discord.Color.red() )
            await ctx.send( embed = emg )

            emw = discord.Embed( title = a, colour = discord.Color.blue() )
            await ctx.send( embed = emw )

            emd = discord.Embed( title = f'{ ctx.author.name}', colour = discord.Color.red() )
            await ctx.send( embed = emd )

            emx = discord.Embed( title = v, colour = discord.Color.blue() )
            await ctx.send( embed = emx )
            
    @commands.command() # Попытки 5
    async def guess(self, ctx):
        await ctx.message.delete()
        num = random.randint(1, 20)
        attems = 1
        msg = await ctx.send('Подождите...')
        while attems < 6:
            emb = discord.Embed(
                title = f'Попытка №{attems}',
                description= 'Угадайте число от 1 до 20'
            )
            await msg.edit(content= None, embed=emb)
            try:
                msg_o = await  client.wait_for('message', timeout= 30.0, check= lambda msg_o: msg_o.author == ctx.author)
            except asyncio.TimeoutError:
                await msg.edit(content= 'Время вышло!', embed=None)
                break
            else:
                if num == int(msg_o.content):
                    emb1 = discord.Embed(
                        title= 'Вы победили!',
                        description= 'Вы угадали число!'
                    )
                    await msg_o.delete()
                    await msg.edit(content= None, embed=emb1)
                    break
                else:
                    attems_h = 5 - attems
                    attems = attems + 1
                    if attems == 6:
                        emb2 = discord.Embed(
                            title= 'Вы проиграли!',
                            description= f'Загаданое число было : {num}'
                        )
                        await msg_o.delete()
                        await msg.edit(embed=emb2)
                        break

                    emb2 = discord.Embed(
                        title= 'Неудачная попытка!',
                        description= f'Вы не угадали число у вас осталось {attems_h} попыток'
                    )
                    await msg.edit(content= None, embed=emb2)
                    await msg_o.delete() 
                    await asyncio.sleep(2)  
    #coinflip
    @commands.command()
    async def coinflip(self, ctx ):
        a = random.choice(['орел','решка','орел','решка'])
        await ctx.send( a )

   
        
def setup(client):
    client.add_cog(user(client))
