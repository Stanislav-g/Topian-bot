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
    
    
    
    #info
    @client.command( pass_context = True )
    async def help( ctx ):
        await ctx.channel.purge( limit = 1 )
        emb = discord.Embed( title = '**Moderation**', colour = discord.Color.red() )
        emb.add_field( name = 'Commands',value = '*clea*r = clear (количество) или clear (пользователь)(количество)\n
        *ban* = ban @user\n
        *unban* = unban @user\n
        *kick* = kick @user')
        await ctx.author.send( embed = emb )
        embw = discord.Embed( title = '**Info**', colour = discord.Color.red() )
        embw.add_field( name = 'Commands',value = '')
        await ctx.author.send( embed = embw )


    @commands.command(aliases = ['clear', 'c'])
    @commands.has_permissions(manage_messages = True)
    async def __clear(self, ctx, member: typing.Optional[discord.Member], amount : int):
                await ctx.message.delete()

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
    @client.command( pass_context = True )
    @commands.has_permissions( administrator = True )

    async def kick( ctx, member: discord.Member, *, reason = None):
        emb = discord.Embed( title = 'Kick', colour = discord.Color.red() )
        await ctx.channel.purge( limit = 1 )

        await member.kick( reason = reason )

        emb.set_author( name = member.name, icon_url = member.avatar_url)
        emb.add_field( name = 'Kick user',value = 'Kick user : {}'.format( member.mention ) )
        await ctx.send( embed = emb )
        await ctx.send( f'kick user { member.mention}')

    #ban
    @client.command( pass_context = True )
    @commands.has_permissions( administrator = True )

    async def ban( ctx, member: discord.Member, *, reason = None):
        emb = discord.Embed( title = 'Ban', colour = discord.Color.red() )
        await ctx.channel.purge( limit = 1 )

        await member.ban( reason = reason )
        emb.set_author( name = member.name, icon_url = member.avatar_url)
        emb.add_field( name = 'Ban user',value = 'Banned user : {}'.format( member.mention ) )
        await ctx.send( embed = emb )
        await ctx.send( f'Ban user { member.mention}')

    #unban
    @client.command( pass_context = True )
    @commands.has_permissions( administrator = True )
    async def unban( ctx, *, member ):
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

def setup(client):
    client.add_cog(user(client))
