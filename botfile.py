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
async def country(ctx):      

    randomflag2 = random.choice(['🏳️‍🌈','🇺🇳','🇦🇫','🇦🇱','🇩🇪','🇦🇩','🇦🇴 ',' 🇦🇮 ',' 🇦🇶 ',' 🇦🇬 ',' 🇸🇦 ',' 🇩🇿 ',' 🇦🇷 ',' 🇦🇲 ',' 🇦🇼 ',' 🇦🇺 ',' 🇦🇹 ',' 🇦🇿 ',' 🇧🇸 ',' 🇧🇩 ',' 🇧🇧 ',' 🇧🇭 ',' 🇧🇪 ',' 🇧🇿 ',' 🇧🇯 ',' 🇧🇲 ',' 🇧🇾 ',' 🇧🇴 ',' 🇧🇦 ',' 🇧🇼 ',' 🇧🇷 ',' 🇧🇳 ',' 🇧🇬 ',' 🇧🇫 ',' 🇧🇮 ',' 🇧🇹 ',' 🇨🇻 ',' 🇰🇭 ',' 🇨🇲 ',' 🇨🇦 ',' 🇮🇨 ',' 🇧🇶 ',' 🇶🇦 ',' 🇹🇩 ',' 🇨🇿 ',' 🇨🇱 ',' 🇨🇳 ',' 🇨🇾 ',' 🇻🇦 ',' 🇨🇴 ',' 🇰🇲 ',' 🇨🇬 ',' 🇰🇵 ',' 🇰🇷 ',' 🇨🇷 ',' 🇨🇮 ',' 🇭🇷 ',' 🇨🇺 ',' 🇨🇼 ',' 🇩🇰 ',' 🇩🇲 ',' 🇪🇨 ',' 🇪🇬 ',' 🇸🇻 ',' 🇦🇪 ',' 🇪🇷 ',' 🇸🇰 ',' 🇸🇮 ',' 🇪🇸 ',' 🇺🇸 ',' 🇪🇪 ',' 🇸🇿 ',' 🇪🇹 ',' 🇵🇭 ',' 🇫🇮 ',' 🇫🇯 ',' 🇫🇷 ',' 🇬🇦 ',' 🇬🇲 ',' 🇬🇪 ',' 🇬🇭 ',' 🇬🇮 ',' 🇬🇩 ',' 🇬🇷 ',' 🇬🇱 ',' 🇬🇵 ',' 🇬🇺 ',' 🇬🇹 ',' 🇬🇫 ',' 🇬🇬 ',' 🇬🇳 ',' 🇬🇶 ',' 🇬🇼 ',' 🇬🇾 ',' 🇭🇹 ',' 🇭🇳 ',' 🇭🇰 ',' 🇭🇺 ',' 🇮🇳 ',' 🇮🇩 ',' 🇮🇶 ',' 🇮🇷 ',' 🇮🇪 ',' 🇮🇲 ',' 🇨🇽 ',' 🇳🇫 ',' 🇮🇸 ',' 🇦🇽 ',' 🇰🇾 ',' 🇨🇨 ',' 🇨🇰 ',' 🇫🇴 ',' 🇬🇸 ',' 🇫🇰 ',' 🇲🇵 ',' 🇲🇭 ',' 🇵🇳 ',' 🇸🇧 ',' 🇹🇨 ',' 🇻🇬 ',' 🇻🇮 ',' 🇮🇱 ',' 🇮🇹 ',' 🇯🇲 ',' 🇯🇵 ',' 🇯🇪 ',' 🇯🇴 ',' 🇰🇿 ',' 🇰🇪 ',' 🇰🇬 ',' 🇰🇮 ',' 🇽🇰 ',' 🇰🇼 ',' 🇱🇦 ',' 🇱🇸 ',' 🇱🇻 ',' 🇱🇧 ',' 🇱🇷 ',' 🇱🇾 ',' 🇱🇮 ',' 🇱🇹 ',' 🇱🇺 ',' 🇲🇴 ',' 🇲🇰 ',' 🇲🇬 ',' 🇲🇾 ',' 🇲🇼 ',' 🇲🇻 ',' 🇲🇱 ',' 🇲🇹 ',' 🇲🇦 ',' 🇲🇶 ',' 🇲🇺 ',' 🇲🇷 ',' 🇾🇹 ',' 🇲🇽 ',' 🇫🇲 ',' 🇲🇩 ',' 🇲🇨 ',' 🇲🇳 ',' 🇲🇪 ',' 🇲🇸 ',' 🇲🇿 ',' 🇲🇲 ',' 🇳🇦 ',' 🇳🇷 ',' 🇳🇵 ',' 🇳🇮 ',' 🇳🇪 ',' 🇳🇬 ',' 🇳🇺 ',' 🇳🇴 ',' 🇳🇨 ',' 🇳🇿 ',' 🇴🇲 ',' 🇳🇱 ',' 🇵🇰 ',' 🇵🇼 ',' 🇵🇦 ',' 🇵🇬 ',' 🇵🇾 ',' 🇵🇪 ',' 🇵🇫 ',' 🇵🇱 ',' 🇵🇹 ',' 🇵🇷 ',' 🇬🇧 ',' 🏴󠁧󠁢󠁥󠁮󠁧󠁿 ',' 🏴󠁧󠁢󠁳󠁣󠁴󠁿 ',' 🏴󠁧󠁢󠁷󠁬󠁳󠁿 ',' 🇨🇫 ',' 🇨🇩 ',' 🇩🇴 ',' 🇷🇪 ',' 🇷🇼 ',' 🇷🇴 ',' 🇷🇺 ',' 🇪🇭 ',' 🇼🇸 ',' 🇦🇸 ',' 🇧🇱 ',' 🇰🇳 ',' 🇸🇲 ',' 🇵🇲 ',' 🇻🇨 ',' 🇸🇭 ',' 🇱🇨 ',' 🇸🇹 ',' 🇸🇳 ',' 🇷🇸 ',' 🇸🇨 ',' 🇸🇱 ',' 🇸🇬 ',' 🇸🇽 ',' 🇸🇾 ',' 🇸🇴 ',' 🇱🇰 ',' 🇿🇦 ',' 🇸🇩 ',' 🇸🇸 ',' 🇸🇪 ',' 🇨🇭 ',' 🇸🇷 ',' 🇹🇭 ',' 🇹🇼 ',' 🇹🇿 ',' 🇹🇯 ',' 🇮🇴 ',' 🇹🇫 ',' 🇵🇸 ',' 🇹🇱 ',' 🇹🇬 ',' 🇹🇰 ',' 🇹🇴 ',' 🇹🇹 ',' 🇹🇳 ',' 🇹🇲 ',' 🇹🇷 ',' 🇹🇻 ',' 🇺🇦 ',' 🇺🇬 ',' 🇺🇾 ',' 🇺🇿 ',' 🇻🇺 ',' 🇻🇪 ',' 🇻🇳 ',' 🇼🇫 ',' 🇾🇪 ',' 🇩🇯 ',' 🇿🇲 ',' 🇿🇼'

])
    randomflag3 = random.choice(['🏳️‍🌈','🇺🇳','🇦🇫','🇦🇱','🇩🇪','🇦🇩','🇦🇴 ',' 🇦🇮 ',' 🇦🇶 ',' 🇦🇬 ',' 🇸🇦 ',' 🇩🇿 ',' 🇦🇷 ',' 🇦🇲 ',' 🇦🇼 ',' 🇦🇺 ',' 🇦🇹 ',' 🇦🇿 ',' 🇧🇸 ',' 🇧🇩 ',' 🇧🇧 ',' 🇧🇭 ',' 🇧🇪 ',' 🇧🇿 ',' 🇧🇯 ',' 🇧🇲 ',' 🇧🇾 ',' 🇧🇴 ',' 🇧🇦 ',' 🇧🇼 ',' 🇧🇷 ',' 🇧🇳 ',' 🇧🇬 ',' 🇧🇫 ',' 🇧🇮 ',' 🇧🇹 ',' 🇨🇻 ',' 🇰🇭 ',' 🇨🇲 ',' 🇨🇦 ',' 🇮🇨 ',' 🇧🇶 ',' 🇶🇦 ',' 🇹🇩 ',' 🇨🇿 ',' 🇨🇱 ',' 🇨🇳 ',' 🇨🇾 ',' 🇻🇦 ',' 🇨🇴 ',' 🇰🇲 ',' 🇨🇬 ',' 🇰🇵 ',' 🇰🇷 ',' 🇨🇷 ',' 🇨🇮 ',' 🇭🇷 ',' 🇨🇺 ',' 🇨🇼 ',' 🇩🇰 ',' 🇩🇲 ',' 🇪🇨 ',' 🇪🇬 ',' 🇸🇻 ',' 🇦🇪 ',' 🇪🇷 ',' 🇸🇰 ',' 🇸🇮 ',' 🇪🇸 ',' 🇺🇸 ',' 🇪🇪 ',' 🇸🇿 ',' 🇪🇹 ',' 🇵🇭 ',' 🇫🇮 ',' 🇫🇯 ',' 🇫🇷 ',' 🇬🇦 ',' 🇬🇲 ',' 🇬🇪 ',' 🇬🇭 ',' 🇬🇮 ',' 🇬🇩 ',' 🇬🇷 ',' 🇬🇱 ',' 🇬🇵 ',' 🇬🇺 ',' 🇬🇹 ',' 🇬🇫 ',' 🇬🇬 ',' 🇬🇳 ',' 🇬🇶 ',' 🇬🇼 ',' 🇬🇾 ',' 🇭🇹 ',' 🇭🇳 ',' 🇭🇰 ',' 🇭🇺 ',' 🇮🇳 ',' 🇮🇩 ',' 🇮🇶 ',' 🇮🇷 ',' 🇮🇪 ',' 🇮🇲 ',' 🇨🇽 ',' 🇳🇫 ',' 🇮🇸 ',' 🇦🇽 ',' 🇰🇾 ',' 🇨🇨 ',' 🇨🇰 ',' 🇫🇴 ',' 🇬🇸 ',' 🇫🇰 ',' 🇲🇵 ',' 🇲🇭 ',' 🇵🇳 ',' 🇸🇧 ',' 🇹🇨 ',' 🇻🇬 ',' 🇻🇮 ',' 🇮🇱 ',' 🇮🇹 ',' 🇯🇲 ',' 🇯🇵 ',' 🇯🇪 ',' 🇯🇴 ',' 🇰🇿 ',' 🇰🇪 ',' 🇰🇬 ',' 🇰🇮 ',' 🇽🇰 ',' 🇰🇼 ',' 🇱🇦 ',' 🇱🇸 ',' 🇱🇻 ',' 🇱🇧 ',' 🇱🇷 ',' 🇱🇾 ',' 🇱🇮 ',' 🇱🇹 ',' 🇱🇺 ',' 🇲🇴 ',' 🇲🇰 ',' 🇲🇬 ',' 🇲🇾 ',' 🇲🇼 ',' 🇲🇻 ',' 🇲🇱 ',' 🇲🇹 ',' 🇲🇦 ',' 🇲🇶 ',' 🇲🇺 ',' 🇲🇷 ',' 🇾🇹 ',' 🇲🇽 ',' 🇫🇲 ',' 🇲🇩 ',' 🇲🇨 ',' 🇲🇳 ',' 🇲🇪 ',' 🇲🇸 ',' 🇲🇿 ',' 🇲🇲 ',' 🇳🇦 ',' 🇳🇷 ',' 🇳🇵 ',' 🇳🇮 ',' 🇳🇪 ',' 🇳🇬 ',' 🇳🇺 ',' 🇳🇴 ',' 🇳🇨 ',' 🇳🇿 ',' 🇴🇲 ',' 🇳🇱 ',' 🇵🇰 ',' 🇵🇼 ',' 🇵🇦 ',' 🇵🇬 ',' 🇵🇾 ',' 🇵🇪 ',' 🇵🇫 ',' 🇵🇱 ',' 🇵🇹 ',' 🇵🇷 ',' 🇬🇧 ',' 🏴󠁧󠁢󠁥󠁮󠁧󠁿 ',' 🏴󠁧󠁢󠁳󠁣󠁴󠁿 ',' 🏴󠁧󠁢󠁷󠁬󠁳󠁿 ',' 🇨🇫 ',' 🇨🇩 ',' 🇩🇴 ',' 🇷🇪 ',' 🇷🇼 ',' 🇷🇴 ',' 🇷🇺 ',' 🇪🇭 ',' 🇼🇸 ',' 🇦🇸 ',' 🇧🇱 ',' 🇰🇳 ',' 🇸🇲 ',' 🇵🇲 ',' 🇻🇨 ',' 🇸🇭 ',' 🇱🇨 ',' 🇸🇹 ',' 🇸🇳 ',' 🇷🇸 ',' 🇸🇨 ',' 🇸🇱 ',' 🇸🇬 ',' 🇸🇽 ',' 🇸🇾 ',' 🇸🇴 ',' 🇱🇰 ',' 🇿🇦 ',' 🇸🇩 ',' 🇸🇸 ',' 🇸🇪 ',' 🇨🇭 ',' 🇸🇷 ',' 🇹🇭 ',' 🇹🇼 ',' 🇹🇿 ',' 🇹🇯 ',' 🇮🇴 ',' 🇹🇫 ',' 🇵🇸 ',' 🇹🇱 ',' 🇹🇬 ',' 🇹🇰 ',' 🇹🇴 ',' 🇹🇹 ',' 🇹🇳 ',' 🇹🇲 ',' 🇹🇷 ',' 🇹🇻 ',' 🇺🇦 ',' 🇺🇬 ',' 🇺🇾 ',' 🇺🇿 ',' 🇻🇺 ',' 🇻🇪 ',' 🇻🇳 ',' 🇼🇫 ',' 🇾🇪 ',' 🇩🇯 ',' 🇿🇲 ',' 🇿🇼'

])
    randomflag = random.choice(['🏳️‍🌈','🇺🇳','🇦🇫','🇦🇱','🇩🇪','🇦🇩','🇦🇴 ',' 🇦🇮 ',' 🇦🇶 ',' 🇦🇬 ',' 🇸🇦 ',' 🇩🇿 ',' 🇦🇷 ',' 🇦🇲 ',' 🇦🇼 ',' 🇦🇺 ',' 🇦🇹 ',' 🇦🇿 ',' 🇧🇸 ',' 🇧🇩 ',' 🇧🇧 ',' 🇧🇭 ',' 🇧🇪 ',' 🇧🇿 ',' 🇧🇯 ',' 🇧🇲 ',' 🇧🇾 ',' 🇧🇴 ',' 🇧🇦 ',' 🇧🇼 ',' 🇧🇷 ',' 🇧🇳 ',' 🇧🇬 ',' 🇧🇫 ',' 🇧🇮 ',' 🇧🇹 ',' 🇨🇻 ',' 🇰🇭 ',' 🇨🇲 ',' 🇨🇦 ',' 🇮🇨 ',' 🇧🇶 ',' 🇶🇦 ',' 🇹🇩 ',' 🇨🇿 ',' 🇨🇱 ',' 🇨🇳 ',' 🇨🇾 ',' 🇻🇦 ',' 🇨🇴 ',' 🇰🇲 ',' 🇨🇬 ',' 🇰🇵 ',' 🇰🇷 ',' 🇨🇷 ',' 🇨🇮 ',' 🇭🇷 ',' 🇨🇺 ',' 🇨🇼 ',' 🇩🇰 ',' 🇩🇲 ',' 🇪🇨 ',' 🇪🇬 ',' 🇸🇻 ',' 🇦🇪 ',' 🇪🇷 ',' 🇸🇰 ',' 🇸🇮 ',' 🇪🇸 ',' 🇺🇸 ',' 🇪🇪 ',' 🇸🇿 ',' 🇪🇹 ',' 🇵🇭 ',' 🇫🇮 ',' 🇫🇯 ',' 🇫🇷 ',' 🇬🇦 ',' 🇬🇲 ',' 🇬🇪 ',' 🇬🇭 ',' 🇬🇮 ',' 🇬🇩 ',' 🇬🇷 ',' 🇬🇱 ',' 🇬🇵 ',' 🇬🇺 ',' 🇬🇹 ',' 🇬🇫 ',' 🇬🇬 ',' 🇬🇳 ',' 🇬🇶 ',' 🇬🇼 ',' 🇬🇾 ',' 🇭🇹 ',' 🇭🇳 ',' 🇭🇰 ',' 🇭🇺 ',' 🇮🇳 ',' 🇮🇩 ',' 🇮🇶 ',' 🇮🇷 ',' 🇮🇪 ',' 🇮🇲 ',' 🇨🇽 ',' 🇳🇫 ',' 🇮🇸 ',' 🇦🇽 ',' 🇰🇾 ',' 🇨🇨 ',' 🇨🇰 ',' 🇫🇴 ',' 🇬🇸 ',' 🇫🇰 ',' 🇲🇵 ',' 🇲🇭 ',' 🇵🇳 ',' 🇸🇧 ',' 🇹🇨 ',' 🇻🇬 ',' 🇻🇮 ',' 🇮🇱 ',' 🇮🇹 ',' 🇯🇲 ',' 🇯🇵 ',' 🇯🇪 ',' 🇯🇴 ',' 🇰🇿 ',' 🇰🇪 ',' 🇰🇬 ',' 🇰🇮 ',' 🇽🇰 ',' 🇰🇼 ',' 🇱🇦 ',' 🇱🇸 ',' 🇱🇻 ',' 🇱🇧 ',' 🇱🇷 ',' 🇱🇾 ',' 🇱🇮 ',' 🇱🇹 ',' 🇱🇺 ',' 🇲🇴 ',' 🇲🇰 ',' 🇲🇬 ',' 🇲🇾 ',' 🇲🇼 ',' 🇲🇻 ',' 🇲🇱 ',' 🇲🇹 ',' 🇲🇦 ',' 🇲🇶 ',' 🇲🇺 ',' 🇲🇷 ',' 🇾🇹 ',' 🇲🇽 ',' 🇫🇲 ',' 🇲🇩 ',' 🇲🇨 ',' 🇲🇳 ',' 🇲🇪 ',' 🇲🇸 ',' 🇲🇿 ',' 🇲🇲 ',' 🇳🇦 ',' 🇳🇷 ',' 🇳🇵 ',' 🇳🇮 ',' 🇳🇪 ',' 🇳🇬 ',' 🇳🇺 ',' 🇳🇴 ',' 🇳🇨 ',' 🇳🇿 ',' 🇴🇲 ',' 🇳🇱 ',' 🇵🇰 ',' 🇵🇼 ',' 🇵🇦 ',' 🇵🇬 ',' 🇵🇾 ',' 🇵🇪 ',' 🇵🇫 ',' 🇵🇱 ',' 🇵🇹 ',' 🇵🇷 ',' 🇬🇧 ',' 🏴󠁧󠁢󠁥󠁮󠁧󠁿 ',' 🏴󠁧󠁢󠁳󠁣󠁴󠁿 ',' 🏴󠁧󠁢󠁷󠁬󠁳󠁿 ',' 🇨🇫 ',' 🇨🇩 ',' 🇩🇴 ',' 🇷🇪 ',' 🇷🇼 ',' 🇷🇴 ',' 🇷🇺 ',' 🇪🇭 ',' 🇼🇸 ',' 🇦🇸 ',' 🇧🇱 ',' 🇰🇳 ',' 🇸🇲 ',' 🇵🇲 ',' 🇻🇨 ',' 🇸🇭 ',' 🇱🇨 ',' 🇸🇹 ',' 🇸🇳 ',' 🇷🇸 ',' 🇸🇨 ',' 🇸🇱 ',' 🇸🇬 ',' 🇸🇽 ',' 🇸🇾 ',' 🇸🇴 ',' 🇱🇰 ',' 🇿🇦 ',' 🇸🇩 ',' 🇸🇸 ',' 🇸🇪 ',' 🇨🇭 ',' 🇸🇷 ',' 🇹🇭 ',' 🇹🇼 ',' 🇹🇿 ',' 🇹🇯 ',' 🇮🇴 ',' 🇹🇫 ',' 🇵🇸 ',' 🇹🇱 ',' 🇹🇬 ',' 🇹🇰 ',' 🇹🇴 ',' 🇹🇹 ',' 🇹🇳 ',' 🇹🇲 ',' 🇹🇷 ',' 🇹🇻 ',' 🇺🇦 ',' 🇺🇬 ',' 🇺🇾 ',' 🇺🇿 ',' 🇻🇺 ',' 🇻🇪 ',' 🇻🇳 ',' 🇼🇫 ',' 🇾🇪 ',' 🇩🇯 ',' 🇿🇲 ',' 🇿🇼'

])
    num = random.randint(1,80)
    while randomflag == randomflag2 or randomflag == randomflag3 or randomflag3 == randomflag2 or randomflag3 == randomflag or randomflag2 == randomflag3 or randomflag2 == randomflag:
        randomflag2 = random.choice(['🏳️‍🌈','🇺🇳','🇦🇫','🇦🇱','🇩🇪','🇦🇩','🇦🇴 ',' 🇦🇮 ',' 🇦🇶 ',' 🇦🇬 ',' 🇸🇦 ',' 🇩🇿 ',' 🇦🇷 ',' 🇦🇲 ',' 🇦🇼 ',' 🇦🇺 ',' 🇦🇹 ',' 🇦🇿 ',' 🇧🇸 ',' 🇧🇩 ',' 🇧🇧 ',' 🇧🇭 ',' 🇧🇪 ',' 🇧🇿 ',' 🇧🇯 ',' 🇧🇲 ',' 🇧🇾 ',' 🇧🇴 ',' 🇧🇦 ',' 🇧🇼 ',' 🇧🇷 ',' 🇧🇳 ',' 🇧🇬 ',' 🇧🇫 ',' 🇧🇮 ',' 🇧🇹 ',' 🇨🇻 ',' 🇰🇭 ',' 🇨🇲 ',' 🇨🇦 ',' 🇮🇨 ',' 🇧🇶 ',' 🇶🇦 ',' 🇹🇩 ',' 🇨🇿 ',' 🇨🇱 ',' 🇨🇳 ',' 🇨🇾 ',' 🇻🇦 ',' 🇨🇴 ',' 🇰🇲 ',' 🇨🇬 ',' 🇰🇵 ',' 🇰🇷 ',' 🇨🇷 ',' 🇨🇮 ',' 🇭🇷 ',' 🇨🇺 ',' 🇨🇼 ',' 🇩🇰 ',' 🇩🇲 ',' 🇪🇨 ',' 🇪🇬 ',' 🇸🇻 ',' 🇦🇪 ',' 🇪🇷 ',' 🇸🇰 ',' 🇸🇮 ',' 🇪🇸 ',' 🇺🇸 ',' 🇪🇪 ',' 🇸🇿 ',' 🇪🇹 ',' 🇵🇭 ',' 🇫🇮 ',' 🇫🇯 ',' 🇫🇷 ',' 🇬🇦 ',' 🇬🇲 ',' 🇬🇪 ',' 🇬🇭 ',' 🇬🇮 ',' 🇬🇩 ',' 🇬🇷 ',' 🇬🇱 ',' 🇬🇵 ',' 🇬🇺 ',' 🇬🇹 ',' 🇬🇫 ',' 🇬🇬 ',' 🇬🇳 ',' 🇬🇶 ',' 🇬🇼 ',' 🇬🇾 ',' 🇭🇹 ',' 🇭🇳 ',' 🇭🇰 ',' 🇭🇺 ',' 🇮🇳 ',' 🇮🇩 ',' 🇮🇶 ',' 🇮🇷 ',' 🇮🇪 ',' 🇮🇲 ',' 🇨🇽 ',' 🇳🇫 ',' 🇮🇸 ',' 🇦🇽 ',' 🇰🇾 ',' 🇨🇨 ',' 🇨🇰 ',' 🇫🇴 ',' 🇬🇸 ',' 🇫🇰 ',' 🇲🇵 ',' 🇲🇭 ',' 🇵🇳 ',' 🇸🇧 ',' 🇹🇨 ',' 🇻🇬 ',' 🇻🇮 ',' 🇮🇱 ',' 🇮🇹 ',' 🇯🇲 ',' 🇯🇵 ',' 🇯🇪 ',' 🇯🇴 ',' 🇰🇿 ',' 🇰🇪 ',' 🇰🇬 ',' 🇰🇮 ',' 🇽🇰 ',' 🇰🇼 ',' 🇱🇦 ',' 🇱🇸 ',' 🇱🇻 ',' 🇱🇧 ',' 🇱🇷 ',' 🇱🇾 ',' 🇱🇮 ',' 🇱🇹 ',' 🇱🇺 ',' 🇲🇴 ',' 🇲🇰 ',' 🇲🇬 ',' 🇲🇾 ',' 🇲🇼 ',' 🇲🇻 ',' 🇲🇱 ',' 🇲🇹 ',' 🇲🇦 ',' 🇲🇶 ',' 🇲🇺 ',' 🇲🇷 ',' 🇾🇹 ',' 🇲🇽 ',' 🇫🇲 ',' 🇲🇩 ',' 🇲🇨 ',' 🇲🇳 ',' 🇲🇪 ',' 🇲🇸 ',' 🇲🇿 ',' 🇲🇲 ',' 🇳🇦 ',' 🇳🇷 ',' 🇳🇵 ',' 🇳🇮 ',' 🇳🇪 ',' 🇳🇬 ',' 🇳🇺 ',' 🇳🇴 ',' 🇳🇨 ',' 🇳🇿 ',' 🇴🇲 ',' 🇳🇱 ',' 🇵🇰 ',' 🇵🇼 ',' 🇵🇦 ',' 🇵🇬 ',' 🇵🇾 ',' 🇵🇪 ',' 🇵🇫 ',' 🇵🇱 ',' 🇵🇹 ',' 🇵🇷 ',' 🇬🇧 ',' 🏴󠁧󠁢󠁥󠁮󠁧󠁿 ',' 🏴󠁧󠁢󠁳󠁣󠁴󠁿 ',' 🏴󠁧󠁢󠁷󠁬󠁳󠁿 ',' 🇨🇫 ',' 🇨🇩 ',' 🇩🇴 ',' 🇷🇪 ',' 🇷🇼 ',' 🇷🇴 ',' 🇷🇺 ',' 🇪🇭 ',' 🇼🇸 ',' 🇦🇸 ',' 🇧🇱 ',' 🇰🇳 ',' 🇸🇲 ',' 🇵🇲 ',' 🇻🇨 ',' 🇸🇭 ',' 🇱🇨 ',' 🇸🇹 ',' 🇸🇳 ',' 🇷🇸 ',' 🇸🇨 ',' 🇸🇱 ',' 🇸🇬 ',' 🇸🇽 ',' 🇸🇾 ',' 🇸🇴 ',' 🇱🇰 ',' 🇿🇦 ',' 🇸🇩 ',' 🇸🇸 ',' 🇸🇪 ',' 🇨🇭 ',' 🇸🇷 ',' 🇹🇭 ',' 🇹🇼 ',' 🇹🇿 ',' 🇹🇯 ',' 🇮🇴 ',' 🇹🇫 ',' 🇵🇸 ',' 🇹🇱 ',' 🇹🇬 ',' 🇹🇰 ',' 🇹🇴 ',' 🇹🇹 ',' 🇹🇳 ',' 🇹🇲 ',' 🇹🇷 ',' 🇹🇻 ',' 🇺🇦 ',' 🇺🇬 ',' 🇺🇾 ',' 🇺🇿 ',' 🇻🇺 ',' 🇻🇪 ',' 🇻🇳 ',' 🇼🇫 ',' 🇾🇪 ',' 🇩🇯 ',' 🇿🇲 ',' 🇿🇼'

])
        randomflag3 = random.choice(['🏳️‍🌈','🇺🇳','🇦🇫','🇦🇱','🇩🇪','🇦🇩','🇦🇴 ',' 🇦🇮 ',' 🇦🇶 ',' 🇦🇬 ',' 🇸🇦 ',' 🇩🇿 ',' 🇦🇷 ',' 🇦🇲 ',' 🇦🇼 ',' 🇦🇺 ',' 🇦🇹 ',' 🇦🇿 ',' 🇧🇸 ',' 🇧🇩 ',' 🇧🇧 ',' 🇧🇭 ',' 🇧🇪 ',' 🇧🇿 ',' 🇧🇯 ',' 🇧🇲 ',' 🇧🇾 ',' 🇧🇴 ',' 🇧🇦 ',' 🇧🇼 ',' 🇧🇷 ',' 🇧🇳 ',' 🇧🇬 ',' 🇧🇫 ',' 🇧🇮 ',' 🇧🇹 ',' 🇨🇻 ',' 🇰🇭 ',' 🇨🇲 ',' 🇨🇦 ',' 🇮🇨 ',' 🇧🇶 ',' 🇶🇦 ',' 🇹🇩 ',' 🇨🇿 ',' 🇨🇱 ',' 🇨🇳 ',' 🇨🇾 ',' 🇻🇦 ',' 🇨🇴 ',' 🇰🇲 ',' 🇨🇬 ',' 🇰🇵 ',' 🇰🇷 ',' 🇨🇷 ',' 🇨🇮 ',' 🇭🇷 ',' 🇨🇺 ',' 🇨🇼 ',' 🇩🇰 ',' 🇩🇲 ',' 🇪🇨 ',' 🇪🇬 ',' 🇸🇻 ',' 🇦🇪 ',' 🇪🇷 ',' 🇸🇰 ',' 🇸🇮 ',' 🇪🇸 ',' 🇺🇸 ',' 🇪🇪 ',' 🇸🇿 ',' 🇪🇹 ',' 🇵🇭 ',' 🇫🇮 ',' 🇫🇯 ',' 🇫🇷 ',' 🇬🇦 ',' 🇬🇲 ',' 🇬🇪 ',' 🇬🇭 ',' 🇬🇮 ',' 🇬🇩 ',' 🇬🇷 ',' 🇬🇱 ',' 🇬🇵 ',' 🇬🇺 ',' 🇬🇹 ',' 🇬🇫 ',' 🇬🇬 ',' 🇬🇳 ',' 🇬🇶 ',' 🇬🇼 ',' 🇬🇾 ',' 🇭🇹 ',' 🇭🇳 ',' 🇭🇰 ',' 🇭🇺 ',' 🇮🇳 ',' 🇮🇩 ',' 🇮🇶 ',' 🇮🇷 ',' 🇮🇪 ',' 🇮🇲 ',' 🇨🇽 ',' 🇳🇫 ',' 🇮🇸 ',' 🇦🇽 ',' 🇰🇾 ',' 🇨🇨 ',' 🇨🇰 ',' 🇫🇴 ',' 🇬🇸 ',' 🇫🇰 ',' 🇲🇵 ',' 🇲🇭 ',' 🇵🇳 ',' 🇸🇧 ',' 🇹🇨 ',' 🇻🇬 ',' 🇻🇮 ',' 🇮🇱 ',' 🇮🇹 ',' 🇯🇲 ',' 🇯🇵 ',' 🇯🇪 ',' 🇯🇴 ',' 🇰🇿 ',' 🇰🇪 ',' 🇰🇬 ',' 🇰🇮 ',' 🇽🇰 ',' 🇰🇼 ',' 🇱🇦 ',' 🇱🇸 ',' 🇱🇻 ',' 🇱🇧 ',' 🇱🇷 ',' 🇱🇾 ',' 🇱🇮 ',' 🇱🇹 ',' 🇱🇺 ',' 🇲🇴 ',' 🇲🇰 ',' 🇲🇬 ',' 🇲🇾 ',' 🇲🇼 ',' 🇲🇻 ',' 🇲🇱 ',' 🇲🇹 ',' 🇲🇦 ',' 🇲🇶 ',' 🇲🇺 ',' 🇲🇷 ',' 🇾🇹 ',' 🇲🇽 ',' 🇫🇲 ',' 🇲🇩 ',' 🇲🇨 ',' 🇲🇳 ',' 🇲🇪 ',' 🇲🇸 ',' 🇲🇿 ',' 🇲🇲 ',' 🇳🇦 ',' 🇳🇷 ',' 🇳🇵 ',' 🇳🇮 ',' 🇳🇪 ',' 🇳🇬 ',' 🇳🇺 ',' 🇳🇴 ',' 🇳🇨 ',' 🇳🇿 ',' 🇴🇲 ',' ð³🇱 ',' 🇵🇰 ',' 🇵🇼 ',' 🇵🇦 ',' 🇵🇬 ',' 🇵🇾 ',' 🇵🇪 ',' 🇵🇫 ',' 🇵🇱 ',' 🇵🇹 ',' 🇵🇷 ',' 🇬🇧 ',' 🏴󠁧󠁢󠁥󠁮󠁧󠁿 ',' 🏴󠁧󠁢󠁳󠁣󠁴󠁿 ',' 🏴󠁧󠁢󠁷󠁬󠁳󠁿 ',' 🇨🇫 ',' 🇨🇩 ',' 🇩🇴 ',' 🇷🇪 ',' 🇷🇼 ',' 🇷🇴 ',' 🇷🇺 ',' 🇪🇭 ',' 🇼🇸 ',' 🇦🇸 ',' 🇧🇱 ',' 🇰🇳 ',' 🇸🇲 ',' 🇵🇲 ',' 🇻🇨 ',' 🇸🇭 ',' 🇱🇨 ',' 🇸🇹 ',' 🇸🇳 ',' 🇷🇸 ',' 🇸🇨 ',' 🇸🇱 ',' 🇸🇬 ',' 🇸🇽 ',' 🇸🇾 ',' 🇸🇴 ',' 🇱🇰 ',' 🇿🇦 ',' 🇸🇩 ',' 🇸🇸 ',' 🇸🇪 ',' 🇨🇭 ',' 🇸🇷 ',' 🇹🇭 ',' 🇹🇼 ',' 🇹🇿 ',' 🇹🇯 ',' 🇮🇴 ',' 🇹🇫 ',' 🇵🇸 ',' 🇹🇱 ',' 🇹🇬 ',' 🇹🇰 ',' 🇹🇴 ',' 🇹🇹 ',' 🇹🇳 ',' 🇹🇲 ',' 🇹🇷 ',' 🇹🇻 ',' 🇺🇦 ',' 🇺🇬 ',' 🇺🇾 ',' 🇺🇿 ',' 🇻🇺 ',' 🇻🇪 ',' 🇻🇳 ',' 🇼🇫 ',' 🇾🇪 ',' 🇩🇯 ',' 🇿🇲 ',' 🇿🇼'

])
        randomflag = random.choice(['🏳️‍🌈','🇺🇳','🇦🇫','🇦🇱','🇩🇪','🇦🇩','🇦🇴 ',' 🇦🇮 ',' 🇦🇶 ',' 🇦🇬 ',' 🇸🇦 ',' 🇩🇿 ',' 🇦🇷 ',' 🇦🇲 ',' 🇦🇼 ',' 🇦🇺 ',' 🇦🇹 ',' 🇦🇿 ',' 🇧🇸 ',' 🇧🇩 ',' 🇧🇧 ',' 🇧🇭 ',' 🇧🇪 ',' 🇧🇿 ',' 🇧🇯 ',' 🇧🇲 ',' 🇧🇾 ',' 🇧🇴 ',' 🇧🇦 ',' 🇧🇼 ',' 🇧🇷 ',' 🇧🇳 ',' 🇧🇬 ',' 🇧🇫 ',' 🇧🇮 ',' 🇧🇹 ',' 🇨🇻 ',' 🇰🇭 ',' 🇨🇲 ',' 🇨🇦 ',' 🇮🇨 ',' 🇧🇶 ',' 🇶🇦 ',' 🇹🇩 ',' 🇨🇿 ',' 🇨🇱 ',' 🇨🇳 ',' 🇨🇾 ',' 🇻🇦 ',' 🇨🇴 ',' 🇰🇲 ',' 🇨🇬 ',' 🇰🇵 ',' 🇰🇷 ',' 🇨🇷 ',' 🇨🇮 ',' 🇭🇷 ',' 🇨🇺 ',' 🇨🇼 ',' 🇩🇰 ',' 🇩🇲 ',' 🇪🇨 ',' 🇪🇬 ',' 🇸🇻 ',' 🇦🇪 ',' 🇪🇷 ',' 🇸🇰 ',' 🇸🇮 ',' 🇪🇸 ',' 🇺🇸 ',' 🇪🇪 ',' 🇸🇿 ',' 🇪🇹 ',' 🇵🇭 ',' 🇫🇮 ',' 🇫🇯 ',' 🇫🇷 ',' 🇬🇦 ',' 🇬🇲 ',' 🇬🇪 ',' 🇬🇭 ',' 🇬🇮 ',' 🇬🇩 ',' 🇬🇷 ',' 🇬🇱 ',' 🇬🇵 ',' 🇬🇺 ',' 🇬🇹 ',' 🇬🇫 ',' 🇬🇬 ',' 🇬🇳 ',' 🇬🇶 ',' 🇬🇼 ',' 🇬🇾 ',' 🇭🇹 ',' 🇭🇳 ',' 🇭🇰 ',' 🇭🇺 ',' 🇮🇳 ',' 🇮🇩 ',' 🇮🇶 ',' 🇮🇷 ',' 🇮🇪 ',' 🇮🇲 ',' 🇨🇽 ',' 🇳🇫 ',' 🇮🇸 ',' 🇦🇽 ',' 🇰🇾 ',' 🇨🇨 ',' 🇨🇰 ',' 🇫🇴 ',' 🇬🇸 ',' 🇫🇰 ',' 🇲🇵 ',' 🇲🇭 ',' 🇵🇳 ',' 🇸🇧 ',' 🇹🇨 ',' 🇻🇬 ',' 🇻🇮 ',' 🇮🇱 ',' 🇮🇹 ',' 🇯🇲 ',' 🇯🇵 ',' 🇯🇪 ',' 🇯🇴 ',' 🇰🇿 ',' 🇰🇪 ',' 🇰🇬 ',' 🇰🇮 ',' 🇽🇰 ',' 🇰🇼 ',' 🇱🇦 ',' 🇱🇸 ',' 🇱🇻 ',' 🇱🇧 ',' 🇱🇷 ',' 🇱🇾 ',' 🇱🇮 ',' 🇱🇹 ',' 🇱🇺 ',' 🇲🇴 ',' 🇲🇰 ',' 🇲🇬 ',' 🇲🇾 ',' 🇲🇼 ',' 🇲🇻 ',' 🇲🇱 ',' 🇲🇹 ',' 🇲🇦 ',' 🇲🇶 ',' 🇲🇺 ',' 🇲🇷 ',' 🇾🇹 ',' 🇲🇽 ',' 🇫🇲 ',' 🇲🇩 ',' 🇲🇨 ',' 🇲🇳 ',' 🇲🇪 ',' 🇲🇸 ',' 🇲🇿 ',' 🇲🇲 ',' 🇳🇦 ',' 🇳🇷 ',' 🇳🇵 ',' 🇳🇮 ',' 🇳🇪 ',' 🇳🇬 ',' 🇳🇺 ',' 🇳🇴 ',' 🇳🇨 ',' 🇳🇿 ',' 🇴🇲 ',' 🇳🇱 ',' 🇵🇰 ',' 🇵🇼 ',' 🇵🇦 ',' 🇵🇬 ',' 🇵🇾 ',' 🇵🇪 ',' 🇵🇫 ',' 🇵🇱 ',' 🇵🇹 ',' 🇵🇷 ',' 🇬🇧 ',' 🏴󠁧󠁢󠁥󠁮󠁧󠁿 ',' 🏴󠁧󠁢󠁳󠁣󠁴󠁿 ',' 🏴󠁧󠁢󠁷󠁬󠁳󠁿 ',' 🇨🇫 ',' 🇨🇩 ',' 🇩🇴 ',' 🇷🇪 ',' 🇷🇼 ',' 🇷🇴 ',' 🇷🇺 ',' 🇪🇭 ',' 🇼🇸 ',' 🇦🇸 ',' 🇧🇱 ',' 🇰🇳 ',' 🇸🇲 ',' 🇵🇲 ',' 🇻🇨 ',' 🇸🇭 ',' 🇱🇨 ',' 🇸🇹 ',' 🇸🇳 ',' 🇷🇸 ',' 🇸🇨 ',' 🇸🇱 ',' 🇸🇬 ',' 🇸🇽 ',' 🇸🇾 ',' 🇸🇴 ',' 🇱🇰 ',' 🇿🇦 ',' 🇸🇩 ',' 🇸🇸 ',' 🇸🇪 ',' 🇨🇭 ',' 🇸🇷 ',' 🇹🇭 ',' 🇹🇼 ',' 🇹🇿 ',' 🇹🇯 ',' 🇮🇴 ',' 🇹🇫 ',' 🇵🇸 ',' 🇹🇱 ',' 🇹🇬 ',' 🇹🇰 ',' 🇹🇴 ',' 🇹🇹 ',' 🇹🇳 ',' 🇹🇲 ',' 🇹🇷 ',' 🇹🇻 ',' 🇺🇦 ',' 🇺🇬 ',' 🇺🇾 ',' 🇺🇿 ',' 🇻🇺 ',' 🇻🇪 ',' 🇻🇳 ',' 🇼🇫 ',' 🇾🇪 ',' 🇩🇯 ',' 🇿🇲 ',' 🇿🇼'

])
    files = []
    for file in ctx.message.attachments:
        fp = io.BytesIO()
        await file.save(fp)
        if file in ctx.message.attachments:
            files.append(discord.File(fp, filename = file.filename, spoiler = file.is_spoiler()))
            await ctx.send(files = files)
            if num < 100:
                between = int(100 - num)
                num2 = random.randint(1,between)
                summa = (num + num2)
                    
                if summa <= 100:
                        
                    allnums = int(num + num2)
                    between_second = (100 - allnums)
                    num3 = between_second
                    if num > num2:   
                        if num > num3:   
                            if num2 > num3:
                                
                                embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num}%\n2 {randomflag2} {num2}%\n3 {randomflag3} {num3}%')
                                embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                                await ctx.send(embed=embed)
         

                            else:
                                embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num}%\n2 {randomflag2} {num3}%\n3 {randomflag3} {num2}%')                        
                                embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                                await ctx.send(embed=embed)  

                        else:
                            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num3}%\n2 {randomflag2} {num}%\n3 {randomflag3} {num2}%')                        
                            embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                            await ctx.send(embed=embed)

                            
                    elif num2 > num:
                        if num2 > num3:
                            if num > num3:
                                embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num2}%\n2 {randomflag2} {num}%\n3 {randomflag3} {num3}%')                        
                                embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                                await ctx.send(embed=embed)


                            else:
                                embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num2}%\n2 {randomflag2} {num3}%\n3 {randomflag3} {num}%')                        
                                embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                                await ctx.send(embed=embed)

              

                        else:
                            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num3}%\n2 {randomflag2} {num2}%\n3 {randomflag3} {num}%')                        
                            embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                            await ctx.send(embed=embed)


                                 
                    elif num3 > num:
                        if num3 > num3:
                            if num > num3:
                                embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num3}%\n2 {randomflag2} {num}%\n3 {randomflag3} {num2}%')                        
                                embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                                await ctx.send(embed=embed)


                            else:
                                embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num3}%\n2 {randomflag2} {num2}%\n3 {randomflag3} {num}%')                        
                                embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                                await ctx.send(embed=embed)
                                


                        else:
                            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.now(datetime.timezone.utc), description=f'1 {randomflag} {num2}%\n2 {randomflag2} {num3}%\n3 {randomflag3} {num}%')                        
                            embed.set_footer(text = f'© Copyright 2020 Topian Team | Все права защищены', icon_url = ctx.author.avatar_url)
                            await ctx.send(embed=embed)


    else:
        await ctx.send(f"Вы не прикрепили картинку")
		
	
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
        

            
        
for filename in os.listdir('./cogs'): # Цикл перебирающий файлы в cogs
    client.load_extension(f'cogs.{filename[:-3]}') 
 

token= os.environ.get('BOT_TOKEN')
client.run( token )
