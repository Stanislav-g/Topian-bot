import discord
from discord.ext import commands
import datetime
from datetime import datetime
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
        
    fi = [''] 
    se = [''] 
    three = [''] 
    fo = [''] 
    fif = [''] 
    start_ev = ['']    
    ev_player = [''] #игроки в розыгрыше
    
    clu= os.environ.get('MONGODB_URI')
    cluster = MongoClient(clu)
    db = cluster["topianbot"]
    collection = db["money"]
    collectionmodules = db["modules"]
    collectionshop = db["shop"]
    collectionticket = db["ticket"]
    collectionlogschannels = db["logschannels"]

    
    @commands.command()
    async def num_guess(self, ctx, numg: int = None, stavka: int = None):
        
        num1 = ctx.author.guild.id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["on_off"] == 'on':
                num = ctx.author.guild.id
                num2 = ctx.author.id
                allnum = num + num2
                if collection.count_documents({"_id": allnum}) == 0:
                    await ctx.send(f"Ваша учетная запись не создана, вы можете создать ее командой -economic")
                else:
                    if not numg:
                        embed = discord.Embed(title='Num  guess.', color=0x00ff00)
                        embed.add_field(name='Правила игры.', value="Num guess это игра где надо угадать число в диапазоне от 1 до 20.\nЧтобы выиграть деньги вы должны поставить ставку.\nСтавка может быть любой, если вы угадаете число, вы заберете удвоенную ставку, если вы проиграете, вы отдадите вашу ставку боту.\n", inline=False)
                        embed.add_field(name='Пример использования команды.', value="**=num_guess 14 200** | 14 это число, а 200 это ставка.", inline=True)
                        embed.add_field(name='Выигрыш со ставкой 200', value="Ставка умножается на 2, выигрыш будет 400.",inline=True)
                        await ctx.send(embed=embed)
                    elif not stavka:
                        await ctx.send(f"**{ctx.author}**, укажите ставку.")
                    else:
                        
                        balancee = collection.find_one({"_id": allnum})["balance"]

                        if stavka > balancee:
                            await ctx.send(f"**{ctx.author}**, на вашем счету недостаточно средств.")
                        else:
                            chislo = random.randint(1,20)
                            if numg == chislo:
                                stavkaitog = stavka * 2
                                balance = collection.update_one({"_id": allnum}, {"$set": {"balance": balancee + stavkaitog}})
                                balanceee = collection.find_one({"_id": allnum})["balance"]
                                await ctx.send(f"**{ctx.author}**, вы угадали! Ваш баланс увеличен на {stavkaitog} , ваш баланс составляет {balanceee} 💵")
                        
                            else:
                                balance = collection.update_one({"_id": allnum}, {"$set": {"balance": balancee - stavka}})
                                balanceeem = collection.find_one({"_id": allnum})["balance"]
                                await ctx.send(f"**{ctx.author}**, вы проиграли. Ваш баланс уменьшен на {stavka}, ваш баланс составляет {balanceeem} 💵")
            else:
                await ctx.send(f"Модуль экономики на этом сервере выключен, чтобы узнать подробности введите команду ``=modules`` ")            


    @commands.command()
    async def color(self, ctx): 
        global fi
        global se
        global three
        global fo
        global fif
        global start_ev
        global ev_player
        a = random.choice(['1','2','3'])
        if a == '1':    
            await ctx.send(f"Приготовься, до старта 5 секунд!")
            await asyncio.sleep(5)
            message = await ctx.send(f"🟥 - 14\n🟧 - 45\n🟨 - 34\n🟩 - 35")
            await asyncio.sleep(1)
            messagee = await ctx.send(f"3")
            await asyncio.sleep(1)
            messageee = await ctx.send(f"2")
            await asyncio.sleep(1)
            messageeee = await ctx.send(f"1")
            await asyncio.sleep(1)
            await message.delete()
            await messagee.delete()
            await messageee.delete()
            await messageeee.delete()
            embed = discord.Embed(title=f"{ctx.author.name}  что было под номером 14?", description= f" 🟥 🟧 🟨 🟩 \n\n")
            message = await ctx.send(embed=embed)
            await message.add_reaction('🟥')
            await message.add_reaction('🟧')
            await message.add_reaction('🟨')
            await message.add_reaction('🟩')
            message = await ctx.send(f"У тебя есть 15 секунд что-бы сделать выбор")
            await asyncio.sleep(12)
            messagee = await ctx.send(f"3")
            await asyncio.sleep(1)
            messageee = await ctx.send(f"2")
            await asyncio.sleep(1)
            messageeee = await ctx.send(f"1")
            await asyncio.sleep(1) 
            await message.delete()
            await messagee.delete()
            await messageee.delete()
            await messageeee.delete()
            if start_ev >= '2':
                await ctx.send(f"Ты угадал правильно!")
            else:
                await ctx.send(f"Ты не угадал")
                
        elif a == '2':
            await ctx.send(f"Приготовься, до старта 5 секунд!")
            await asyncio.sleep(5)
            message = await ctx.send(f"🟥 - 55 \n🟧 - 19\n🟨 - 34\n🟩 - 35")
            await asyncio.sleep(1)
            messagee = await ctx.send(f"3")
            await asyncio.sleep(1)
            messageee = await ctx.send(f"2")
            await asyncio.sleep(1)
            messageeee = await ctx.send(f"1")
            await asyncio.sleep(1)
            await message.delete()
            await messagee.delete()
            await messageee.delete()
            await messageeee.delete()
            embed = discord.Embed(title=f"{ctx.author.name}  что было под номером 19?", description= f" 🟥 🟧 🟨 🟩 \n\n")
            message = await ctx.send(embed=embed)
            await message.add_reaction('🟥')
            await message.add_reaction('🟧')
            await message.add_reaction('🟨')
            await message.add_reaction('🟩')
            message = await ctx.send(f"У тебя есть 15 секунд что-бы сделать выбор")
            await asyncio.sleep(12)
            messagee = await ctx.send(f"3")
            await asyncio.sleep(1)
            messageee = await ctx.send(f"2")
            await asyncio.sleep(1)
            messageeee = await ctx.send(f"1")
            await asyncio.sleep(1) 
            await message.delete()
            await messagee.delete()
            await messageee.delete()
            await messageeee.delete()
            if ev_player >= '2':
                await ctx.send(f"Ты угадал правильно!")
            else:
                await ctx.send(f"Ты не угадал")
                
        elif a == '3':  
            
            await ctx.send(f"Приготовься, до старта 5 секунд!")
            await asyncio.sleep(5)
            message = await ctx.send(f"🟥 - 14 \n🟧 - 45\n🟨 - 34\n🟩 - 35")
            await asyncio.sleep(1)
            messagee = await ctx.send(f"3")
            await asyncio.sleep(1)
            messageee = await ctx.send(f"2")
            await asyncio.sleep(1)
            messageeee = await ctx.send(f"1")
            await asyncio.sleep(1)
            await message.delete()
            await messagee.delete()
            await messageee.delete()
            await messageeee.delete()
            embed = discord.Embed(title=f"{ctx.author.name}  что было под номером 35?", description= f" 🟥 🟧 🟨 🟩 \n\n")
            message = await ctx.send(embed=embed)
            await message.add_reaction('🟥')
            await message.add_reaction('🟧')
            await message.add_reaction('🟨')
            await message.add_reaction('🟩')
            message = await ctx.send(f"У тебя есть 15 секунд что-бы сделать выбор")
            await asyncio.sleep(12)
            messagee = await ctx.send(f"3")
            await asyncio.sleep(1)
            messageee = await ctx.send(f"2")
            await asyncio.sleep(1)
            messageeee = await ctx.send(f"1")
            await asyncio.sleep(1) 
            await message.delete()
            await messagee.delete()
            await messageee.delete()
            await messageeee.delete()
            if three == '2':
                await ctx.send(f"Ты угадал правильно!")
            
            else:
                await ctx.send(f"Ты не угадал")                  
        
         
        
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        
        global ev_player
        global start_ev
        global three
        global fo
        global fi
        global u
        
           
        if str(payload.emoji) == '🟥': # Emoji для реакций
            start_ev = '2'
            
        elif str(payload.emoji) == '🟧': # Emoji для реакций
            ev_player = '2'
            
        elif str(payload.emoji) == '🟩': # Emoji для реакций
            three = '2'
            
        else:
            ev_player = '0'  
            start_ev = '0'
            three = '0'
            fi = '0'
            fo = '0'
         
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        
        global ev_player
        global start_ev
        global three
        global fo
        global fi
        
        if str(payload.emoji) == '🟧': # Emoji для реакций
            ev_player = '0'
        elif str(payload.emoji) == '🟥': # Emoji для реакций
            start_ev = '0'
        elif str(payload.emoji) == '🟩': # Emoji для реакций
            three = '0'
       
    
           
    @commands.command()
    async def rps(self, ctx, *, mess = None):
        if mess == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'rps',value = '**rps** = rps камень, ножницы, бумага.')
            await ctx.send( embed = embw )        
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
                emb.add_field(name = ':scissors:', value = 'Вы проиграли :с')
            elif robot_choice == 'Камень':
                emb.add_field(name = ':moyai:', value = 'Вы выиграли!')
            else:
                emb.add_field(name = ':scroll:', value = 'Ничья!')
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
        if member == None:
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
                msg_o = await  self.client.wait_for('message', timeout= 30.0, check= lambda msg_o: msg_o.author == ctx.author)
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

    @commands.command()
    async def slapperson(self, ctx, member: discord.Member = None, *, reason = None):
        if member == None:
                await ctx.send('{} ,вы не упомянули пользователя'.format( ctx.author))
        elif reason == None:
                await ctx.send('{} ,вы не написали почему хотите ударить пользователя'.format( ctx.author))   
        else:
            await ctx.send('{} ,был ударен участником {} {}'.format(member, ctx.author, reason))
            gif = random.choice(['https://tenor.com/view/back-slap-backhand-funny-animals-penguin-slap-gif-11724800','https://tenor.com/view/slap-bears-gif-10422113','https://tenor.com/view/gap-slapped-knockout-punch-gif-5122019','https://tenor.com/view/kevin-hart-slap-face-your-gif-10570690'])        
            await ctx.send(gif)
        
def setup(client):
    client.add_cog(user(client))
