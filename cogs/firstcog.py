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
import typing 

class user(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def example(self,ctx):
        await ctx.send("work")
    

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound ):
            await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.name}, данной команды не существует.**', color=0x0c0c0c))
            
    

       
   
    @commands.command(aliases = ['clear', 'c'])
    @commands.has_permissions(manage_messages = True)
    @commands.has_permissions( administrator = True )
    async def __clear(self, ctx, member: typing.Optional[discord.Member], amount: int = None):
                await ctx.message.delete()
                if amount == None:
                    embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
                    embw.add_field( name = 'Clear',value = '**clear** = clear (количество) или clear (пользователь)(количество)')
                    await ctx.send( embed = embw )
                else:
                    if member == None:
                        await ctx.channel.purge(limit = amount)
                
                    elif member != None and member in ctx.guild.members:
                        number = 0
                        def predicate(message):
                            return message.author == member
                        async for elem in ctx.channel.history().filter(predicate):
                            await elem.delete()
                            number += 1
                            if number >= amount:
                                break
    #kick
    @commands.command( pass_context = True )
    @commands.has_permissions( administrator = True )

    async def kick(self, ctx, member: discord.Member = None, *, reason = None):
        if member == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Kick',value = '**kick** = kick @user')
            await ctx.send( embed = embw )
        else:    
            emb = discord.Embed( title = 'Kick', colour = discord.Color.red() )
            await ctx.channel.purge( limit = 1 )

            await member.kick( reason = reason )

            emb.set_author( name = member.name, icon_url = member.avatar_url)
            emb.add_field( name = 'Kick user',value = 'Kick user : {}'.format( member.mention ) )
            await ctx.send( embed = emb )
            await ctx.send( f'kick user { member.mention}')

    #ban
    @commands.command( pass_context = True )
    @commands.has_permissions( administrator = True )
    async def ban(self, ctx, member: discord.Member = None, *, reason = None):
        if member == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Ban',value = '**ban** = ban @user')
            await ctx.send( embed = embw )
        else:    
            emb = discord.Embed( title = 'Ban', colour = discord.Color.red() )
            await ctx.channel.purge( limit = 1 )

            await member.ban( reason = reason )
            emb.set_author( name = member.name, icon_url = member.avatar_url)
            emb.add_field( name = 'Ban user',value = 'Banned user : {}'.format( member.mention ) )
            await ctx.send( embed = emb )
            await ctx.send( f'Ban user { member.mention}')

    #unban
    @commands.command( pass_context = True )
    @commands.has_permissions( administrator = True )
    async def unban(self, ctx, *, member = None):
        if member == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Ban',value = '**unban** = unban @user')
            await ctx.send( embed = embw )
        else:    
            emb.set_author( name = member.name, icon_url = member.avatar_url)
            emb = discord.Embed( title = 'unban', colour = discord.Color.red() )
            await ctx.channel.purge( limit = 1)
            banned_users = await ctx.guild.bans()
            emb.add_field( name = 'unban user',value = 'Unbaned user : {}'.format( member.mention ) )
            await ctx.send( embed = emb )

            for ban_entry in banned_users:
                user = ban_entry.user

                await ctx.guild.unban ( user)

                await ctx.send( f'Unbanned user {user.mention }' )

                return
    
        #emoji       
    @commands.command()
    @commands.has_permissions( administrator = True )
    async def emoji(self, ctx, id:int = None, reaction:str = None):
            await ctx.message.delete()
            if id == None:
                embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
                embw.add_field( name = 'Emoji',value = '**emoji** = emoji (message id) (emoji)')
                await ctx.send( embed = embw )
            elif reaction == None:
                embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
                embw.add_field( name = 'Emoji',value = '**emoji** = emoji (message id) (emoji)')
                await ctx.send( embed = embw )
            message = await ctx.message.channel.fetch_message(id)
            await message.add_reaction(reaction)
        #tempban
    @commands.command()
    @commands.has_permissions( administrator = True )
    async def tempban(self, ctx, member : discord.Member = None, time:int = None, arg:str = None, *, reason = None):
        await ctx.channel.purge( limit = 1 )
        if member == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Tempban',value = '**tempban** = tempban @user *s* or *m* or *h* or *d*')
            await ctx.send( embed = embw )
            
        elif time == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Tempban',value = '**tempban** = tempban @user *s* or *m* or *h* or *d*')
            await ctx.send( embed = embw )
            
        elif arg == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Tempban',value = '**tempban** = tempban @user *s* or *m* or *h* or *d*')
            await ctx.send( embed = embw )
        elif reason == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Tempban',value = '**tempban** = tempban @user *s* or *m* or *h* or *d*')
            await ctx.send( embed = embw )
        else:
            if member == ctx.message.author:
                return await ctx.send("Ты не можешь забанить сам себя.")
            msgg =  f'Пользователь : {member}, забанен по причине : {reason}.'
            msgdm = f'Вы были забанены на сервере {ctx.guild.name}, по причине : {reason}.'
            if reason == None:
                msgdm = f'Вы были забанены на сервере : {ctx.guild.name}.'
            if reason == None:
                msgg =  f'Пользователь : {member}, забанен.'
            await ctx.send(msgg)  
            await member.send(msgdm)
            await ctx.guild.ban(member, reason=reason)
            if arg == "s":
                await asyncio.sleep(time)          
            elif arg == "m":
                await asyncio.sleep(time * 60)
            elif arg == "h":
                await asyncio.sleep(time * 60 * 60)
            elif arg == "d":
                await asyncio.sleep(time * 60 * 60 * 24)
            await member.unban()
            await ctx.send(f'Пользователь : {member}, разбанен.')
            await member.send(f'Вы были разбанены на сервере : {ctx.guild.name}')



    @commands.command()
    @commands.has_permissions(administrator = True)
    async def changing_name(self, ctx, member: discord.Member = None, nickname: str = None):
        await ctx.channel.purge( limit = 1 )
        
        try:
            if member is None:
                embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
                embw.add_field( name = 'changing_name',value = '**changing_name** = changing_name @user')
                await ctx.send( embed = embw )
            elif nickname is None:
                embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
                embw.add_field( name = 'changing_name',value = '**changing_name** = changing_name @user')
                await ctx.send( embed = embw )
            else:
                await member.edit(nick = nickname)
                await ctx.send(embed = discord.Embed(description = f"У пользователя **{member.name}** был изменен ник на **{nickname}**"))
        except:
            await ctx.send(embed = discord.Embed(description = f"Я не могу изменить ник пользователя **{member.name}**!"))

    #suggest
    @commands.command( pass_context = True, aliases = [ "Предложить", "предложить", "предложка", "Предложка", "Suggest" ])
    @commands.has_permissions( administrator = True )
    async def suggest(self, ctx , * , arg = None):
        if arg == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Suggest',value = '**suggest** = suggest (text)')
            await ctx.send( embed = embw )
        else:
            embed = discord.Embed(title=f"{ctx.author.name} Предложил :", description= f" {arg} \n\n")

            embed.set_thumbnail(url=ctx.guild.icon_url)

            message = await ctx.send(embed=embed)
            await message.add_reaction('✅')
            await message.add_reaction('❎')

    #text chat
    @commands.command()
    @commands.has_permissions( administrator = True )
    async def text(self, ctx , reaction:str = None, * , arg = None):
            await ctx.channel.purge( limit = 1 )
            if reaction == None: 
                await ctx.send(f" {arg} ")
            else:
                message = await ctx.send(f" {arg} ")
                await message.add_reaction(reaction)


        #text member
    @commands.command()
    @commands.has_permissions( administrator = True )
    async def textmember_lc(self, ctx , * , arg = None, member: discord.Member = None):
            await ctx.channel.purge( limit = 1 )  
            await member.send(f" {arg} ")   
    
    #temp_add_role
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def temp_add_role(self, ctx, amount : int = None, member: discord.Member = None, role: discord.Role = None):
        await ctx.channel.purge( limit = 1 )
        if amount == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Tempban',value = '*temp_add_role** = temp_add_role (time) @user @role')
            await ctx.send( embed = embw )
            
        elif member == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Tempban',value = '**temp_add_role** = temp_add_role (time) @user @role')
            await ctx.send( embed = embw )

        elif role == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Tempban',value = '**temp_add_role** = temp_add_role (time) @user @role')
            await ctx.send( embed = embw )
           
        else:
            try:

                if member is None:

                    await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: пользователя!**'))

                elif role is None:

                    await ctx.send(embed = discord.Embed(description = '**:grey_exclamation: Обязательно укажите: роль!**'))

                else:

                    await discord.Member.add_roles(member, role)
                    await ctx.send(embed = discord.Embed(description = f'**Роль успешна выдана на {amount} секунд!**'))
                    await asyncio.sleep(amount)
                    await discord.Member.remove_roles(member, role)

            except:

                await ctx.send(embed = discord.Embed(description = f'**:exclamation: Не удалось выдать роль.**', color=0x0c0c0c))
    #voice_create
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def voice_create(self, ctx, *, arg = None):
        await ctx.channel.purge( limit = 1 )
        if arg == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Voice_create',value = '**voice_create** = voice_create (name)')
            await ctx.send( embed = embw )
        else:
            guild = ctx.guild
            channel = await guild.create_voice_channel(f'{arg}')
            await ctx.send(embed = discord.Embed(description = f'**:microphone2: Голосовой канал "{arg}" успешно создан!**', color=0x0c0c0c))

    #channel_create   
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def channel_create(self, ctx, *, arg = None): 
        await ctx.channel.purge( limit = 1 )
        if arg == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'Channel_create',value = '**channel_create** = channel_create (name)')
            await ctx.send( embed = embw )
        else:
            guild = ctx.guild
            channel = await guild.create_text_channel(f'{arg}')
            await ctx.send(embed = discord.Embed(description = f'**:keyboard: Текстовый канал "{arg}" успешно создан!**', color=0x0c0c0c))

    #voice_create
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def rolec(self, ctx, *, arg = None):
        await ctx.channel.purge( limit = 1 )
        if arg == None:
            embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
            embw.add_field( name = 'role_create',value = '**role_create** = role_create (name)')
            await ctx.send( embed = embw )
        else:
            guild = ctx.guild
            role = await guild.create_role(f'{arg}')
            await ctx.send(embed = discord.Embed(description = f'**роль "{arg}" создана!**', color=0x0c0c0c))

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def add_role(self, ctx, member: discord.Member = None, role: discord.Role = None):
        
        try:
            if member is None:
                embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
                embw.add_field( name = 'Add_role',value = '**add_role** = add_role @user @role')
                await ctx.send( embed = embw )
            elif role is None:
                embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
                embw.add_field( name = 'Add_role',value = '**add_role** = add_role @user @role')
                await ctx.send( embed = embw )
            else:
                await discord.Member.add_roles(member, role)
                await ctx.send(embed = discord.Embed(description = f'**Роль успешна выдана**'))

        except:
            await ctx.send(embed = discord.Embed(description = f' Не удалось выдать роль.', color=0x0c0c0c))

    @commands.command()
    async def role_members(self, ctx, rolee: discord.Role = None, role: discord.Role = None):
        membersrole = rolee.members
        await ctx.send( "users {}".format( membersrole ) ) 
        

		
     
def setup(client):
    client.add_cog(user(client))
