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

class user(commands.Cog):

    def __init__(self, client):
        self.client = client

     #info
    @commands.command()
    async def bag(self, ctx, * ,arg):       
        channel = client.get_channel( 747764481559494686 )
        emb = discord.Embed( title = '**Кодировщик**', colour= 0x808080)
        emb.add_field( name = 'CODER',value = '=coder encode (text) - зашифровать\n=coder decode (text) расшифровать') 
        emb.set_footer(text='Команда вызвана: {}\n© Copyright 2020 Topian Team | Все права закодированы'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
        await ctx.send( embed = emb )  
        embed.set_author(name=ctx.author.name, icon_url=str(ctx.author.guild.icon_url))
        embed.set_footer(text=f"Author ID: {ctx.author.id}")
        await ctx.send(embed=embed)

        
    #info\n
    @commands.command()
    async def helphelp(self, ctx ):
        await ctx.channel.purge( limit = 1 )
        emb = discord.Embed( title = '**Moderation**', colour= 0x808080)
        emb.add_field( name = 'Commands',value = '**=clear** - clear (количество) или clear (пользователь)(количество)\n**=ban** - ban @user\n **=unban** - unban @user\n **=kick** - kick @user\n **=emoji** - emoji (message id) (emoji)\n**-tempban** - tempban @user *s* or *m* or *h* or *d*\n**=temp_add_role** - temp_add_role (time) @user @role\n **=add_role** - add_role @user @role\n**=channel_create** - channel_create (name)\n**=voice_create** - voice_create (name)\n**=suggest** - suggest (text)\n**=changing_name** - changing_name @user\n**=text** - text (arg)')
        await ctx.author.send( embed = emb )
        embw = discord.Embed( title = '**Info**', colour = discord.Color.green() )
        embw.add_field( name = 'Commands',value = '**=userinfo** - userinfo @user\n**=botinfo**\n**=serverinfo**\n**=avatar** - avatar или avatar @user\n**=ping** - ping\n**=user_boost** - user_ boost @user\n')
        await ctx.author.send( embed = embw )
        embw = discord.Embed( title = '**Search**', colour= 0x808080)
        embw.add_field( name = 'Commands',value = '**=search** - search (запрос)\n**=youtube_search** - youtube_search (запрос)\n**=yandex** - yandex (запрос)\n**=wiki** - wiki (запрос)\n**=google** - google (запрос)\n')
        await ctx.author.send( embed = embw )
        embw = discord.Embed( title = '**Games**', colour = discord.Color.green())
        embw.add_field( name = 'Commands',value = '**=rps** - rps (камень, ножницы или бумага)\n**=guess** - guess\n**=coinflip** - coinflip\n**=knb** - knb @user\n')
        await ctx.author.send( embed = embw )
        embw = discord.Embed( title = '**Other**', colour = discord.Color.green())
        embw.add_field( name = 'Commands',value = '**=num** - num рандомная цифра от 1 до 100\n**=wordnum** - wordnum (text)\n**=slapperson** - slapperson @user\n**=emoji_random** - emoji_random\n**=math** - math (arg) (+-*/) (arg)\n**=covid** - covid\n**=ball** - ball\n**=link** - link (url)\n**=kiss** - kiss @user' )
        await ctx.author.send( embed = embw )

    @commands.command()
    async def h_coder(self, ctx ):
        await ctx.channel.purge( limit = 1 )
        emb = discord.Embed( title = '**Кодировщик**', colour= 0x808080)
        emb.add_field( name = 'CODER',value = '=coder encode (text) - зашифровать\n=coder decode (text) расшифровать') 
        emb.set_footer(text='Команда вызвана: {}\n© Copyright 2020 Topian Team | Все права закодированы'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
        await ctx.send( embed = emb )  
        
    @commands.command(pass_context = True)
    async def help(self, ctx):
        await ctx.channel.purge(limit = 1)
        emb = discord.Embed( 
            title = 'Навигация по командам :clipboard:',
            color = 0x7aa13d
         )

        emb.add_field( name = '__**Moderation**__', value = '''
            **=clear** - clear (количество) или clear (пользователь)(количество)
            **=ban** - ban @user 
            **=unban** - unban @user
            **=kick** - kick @user
            **=emoji** - emoji (message id) (emoji)
            **-tempban** - tempban @user *s* or *m* or *h* or *d*
            **=temp_add_role** - temp_add_role (time) @user @role
            **=add_role** - add_role @user @role
            **=channel_create** - channel_create (name)
            **=voice_create** - voice_create (name)
            **=suggest** - suggest (text)
            **=changing_name** - changing_name @user
            **=text** - text (arg)
            **=image** - image (image)
             
            ''' )
        emb.add_field( name = '__**Info**__', value = '''
            **=userinfo** - userinfo @user
            **=botinfo**
            **=serverinfo**
            **=avatar** - avatar или avatar @user
            **=ping** - ping
            **=user_boost** - user_ boost @user
            **=info_emoji** - info_emoji (emoji)
            ''' )
        emb.add_field( name = '__**Search**__', value = '''
            **=search** - search (запрос)
            **=youtube_search** - youtube_search (запрос)
            **=yandex** - yandex (запрос)
            **=wiki** - wiki (запрос)
            **=google** - google (запрос)
            ''' )
        emb.add_field( name = '__**Games**__', value = '''
            **=rps** - rps (камень, ножницы или бумага)
            **=угадайка** - угадайка
            **=coinflip** - coinflip
            **=knb** - knb @user\n
            ''' )
        emb.add_field( name = '__**Other**__', value = '''
            **=num** - num рандомная цифра от 1 до 100
            **=wordnum** - wordnum (text)
            **=slapperson** - slapperson @user
            **=emoji_random** - emoji_random
            **=math** - math (arg) (+-*/) (arg)
            **=covid** - covid
            **=ball** - ball
            **=link** - link (url)
            **=kiss** - kiss @user
            **=reverse** - reverse (text)
            **=coder** - coder encode (text)
            **=h_coder** - coder help
            **=coder** - coder decode (text)
            **=country** - country file (из какой ты страны)
            ''' )
        await ctx.author.send(embed = emb)        
        
      
        		
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

    @commands.command()
    async def tickets_group(self, ctx):
        if ctx.invoked_subcommand:
            return
        embed = discord.Embed(color=ctx.author.color, timestamp=datetime.datetime.now(
            datetime.timezone.utc), description='Here are all the ticket configuration commands')
        embed.add_field(
            name=f'{ctx.prefix}ticket category [<category>]',
            value='Set the category were tickets are made. **Setting this enables tickets**'
                  '\nRunning this command without providing a category resets it, therefore disabling tickets',
            inline=False
        )
        embed.add_field(
            name=f'{ctx.prefix}ticket limit <number>',
            value='Limit the number of tickets a user can make, 0 = No Limit',
            inline=False
        )
        embed.add_field(
            name=f'{ctx.prefix}ticket name <name>',
            value='Set the name for tickets. There are many variables available for use in the name',
            inline=False
        )
        embed.set_author(name=str(ctx.author), icon_url=str(
            ctx.author.avatar_url_as(static_format='png')))
        return await ctx.send(embed=embed)

    @commands.command()
    async def tickets_category(self, ctx, category: discord.CategoryChannel = None):
        await ctx.config.set('tickets.parent', category)
        if not category:
            return await ctx.success(f'Successfully disabled tickets.')
        return await ctx.success(f'Successfully enabled tickets and set the category to {category}.')

    @commands.command()
    async def tickets_limit(self, ctx, limit: int = 0):
        if limit < 0 or limit > 20:
            return await ctx.error('Invalid limit')
        await ctx.config.set('tickets.limit', limit)
        return await ctx.success(f'Successfully set the ticket limit to {limit}')

    @commands.command()
    async def tickets_name(self, ctx, name: str = None):
        variables = {
            '{increment}': ctx.config.get('tickets.increment'),
            '{name}': ctx.author.name,
            '{id}': ctx.author.id,
            '{word}': random.choice(self.words),
            '{uuid}': str(uuid.uuid4())[:4]
        }
        if not name:
            variables = '\n'.join([f'{k}: {v}' for k, v in variables.items()])
            current = ctx.config.get('tickets.name')
            embed = discord.Embed(
                color=ctx.author.color, timestamp=datetime.datetime.now(datetime.timezone.utc))
            embed.add_field(name='Variables', value=variables, inline=False)
            return await ctx.send(embed=embed)
        if len(name) > 50:
            return await ctx.error('Name is too long, it must be 50 chars or less')
        await ctx.config.set('tickets.name', name)
        fname = name
        for k, v in variables.items():
            fname = fname.replace(k, str(v))
        return await ctx.success(f'Successfully set the tickets name to {name}\nExample: {fname}')

    @commands.command()
    async def tickets_new(self, ctx, *, subject: str = "No subject given"):
        creating = await ctx.send('Creating your ticket...')
       
        variables = {
            '{increment}': config.get('tickets.increment'),
            '{name}': ctx.author.name,
            '{id}': ctx.author.id,
            '{word}': random.choice(self.words),
            '{uuid}': str(uuid.uuid4())[:4],
            '{crab}': '🦀'  # crab in the code? nah, crab in the ticket name
        }
        name = 'test'
        for k, v in variables.items():
            # asbyth has me putting crabs everywhere
            name = name.replace(k, str(v)).replace('crab', '🦀')
        overwrites = {
            ctx.author: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_channels=True, manage_roles=True),
            ctx.guild.default_role: discord.PermissionOverwrite(
                read_messages=False)
        }
        overwrites.update(parent.overwrites)
        ticket = await parent.create_text_channel(
            name=name[:50],
            overwrites=overwrites,
            topic=f'Ticket created by {ctx.author} ({ctx.author.id}) with subject "{subject}"',
            reason=f'Ticket created by {ctx.author} ({ctx.author.id})'
        )
        embed = discord.Embed(
            title=f'Ticket opened by {ctx.author}',
            timestamp=datetime.datetime.now(datetime.timezone.utc),
            color=ctx.author.color
        )
        embed.add_field(name='Subject', value=subject)
        await ticket.send(embed=embed)
        # Removes any channels that no longer exist.
        tchannels = [c for c in config.get('tickets.channels') if c]
        tchannels.append(ticket)
        await config.set('tickets.channels', tchannels)
        await config.set('tickets.increment', config.get('tickets.increment') + 1)
        return await creating.edit(content=f'<:check:674359197378281472> Successfully made your ticket, {ticket.mention}')

    @commands.command()
    async def tickets_add(self, ctx, *, user: discord.Member):
        tchannels = ctx.config.get('tickets.channels')
        if ctx.channel not in tchannels:
            return await ctx.error('This command can only be ran in ticket channels!')
        if str(ctx.author.id) not in ctx.channel.topic and not ctx.author.permissions_in(ctx.channel).manage_channels:
            return await ctx.error('You must own this ticket or have `Manage Channels` permission to add users')
        overwrites = ctx.channel.overwrites
        overwrites.update({user: discord.PermissionOverwrite(read_messages=True, send_messages=True)})
        await ctx.channel.edit(overwrites=overwrites)
        return await ctx.success(f'Successfully added {user.mention} to the ticket')

    @commands.command()
    async def tickets_remove(self, ctx, *, user: discord.Member):
        tchannels = ctx.config.get('tickets.channels')
        if ctx.channel not in tchannels:
            return await ctx.error('This command can only be ran in ticket channels!')
        if str(ctx.author.id) not in ctx.channel.topic and not ctx.author.permissions_in(ctx.channel).manage_channels:
            return await ctx.error('You must own this ticket or have `Manage Channels` permission to remove users')
        if str(user.id) in ctx.channel.topic:
            return await ctx.error('You cannot remove the ticket author')
        if not user.permissions_in(ctx.channel).read_messages:
            return await ctx.error(f'{user} is not here, so how are you gonna remove them? 🤔')
        if user.permissions_in(ctx.channel).manage_channels:
            return await ctx.error(f'You cannot remove this user')
        overwrites = ctx.channel.overwrites
        overwrites.update({user: discord.PermissionOverwrite(read_messages=False, send_messages=False)})
        await ctx.channel.edit(overwrites=overwrites)
        return await ctx.success(f'Successfully removed {user} from the ticket')

    @commands.command()
    async def tickets_close(self, ctx, *, reason: str = "No Reason Provided"):
        config = ctx.config
        tchannels = config.get('tickets.channels')
        if ctx.channel not in tchannels:
            return await ctx.error('This command can only be ran in ticket channels!')
        if not ctx.author.permissions_in(ctx.channel).manage_channels and not str(ctx.author.id) in str(ctx.channel.topic):
            return await ctx.error('You must own this ticket or have `Manage Channels` permission to close')
        await ctx.error(f'Are you sure you want to close this ticket? Type `close` to confirm')
        try:
            await self.bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel and m.content.lower() == 'close', timeout=10)
        except asyncio.TimeoutError:
            return await ctx.error('No response, aborting close.')
        closing = await ctx.send('Closing ticket, this may make take a bit...')
        transcript = []
        async for m in ctx.channel.history(limit=None):
            transcript.append(
                f'{m.author} ({m.author.id}) at {m.created_at.strftime("%d/%m/%Y @ %I:%M:%S %p")} UTC\n{m.content}')
        transcript.reverse()
        string = io.StringIO('\n\n'.join(transcript))
        # If author is not found for some odd reason, fallback to message author for log embed color
        author = ctx.author
        for m in ctx.channel.members:
            if str(m.id) in ctx.channel.topic:  # they do be the ticket author doe
                author = m
                try:
                    await m.send(f'Your ticket in {ctx.guild} was closed for the reason "{reason}". The transcript is below',
                                 file=discord.File(string, filename=f'{ctx.channel}-transcript.txt'))
                except Exception:
                    pass  # no transcript for you, boo hoo :(
        actionlogs = config.get('log.action')
        if actionlogs:
            transcript.append(
                f'{len(transcript)} total messages, closed by {ctx.author}')
            string = io.StringIO('\n\n'.join(transcript))
            embed = discord.Embed(
                title=f'Ticket {ctx.channel} was closed',
                timestamp=datetime.datetime.now(datetime.timezone.utc),
                color=author.color
            )
            embed.add_field(
                name='Closed by', value=f'{ctx.author} ({ctx.author.id})', inline=False)
            embed.add_field(name='Reason', value=reason, inline=False)
            await actionlogs.send(
                embed=embed,
                file=discord.File(string, filename=f'transcript.txt')
            )
        return await ctx.channel.delete(reason=f'Ticket closed by {ctx.author} for "{reason}"')
            
def setup(client):
    client.add_cog(user(client))
