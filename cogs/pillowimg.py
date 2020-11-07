 
import discord
from discord.ext import commands
from pymongo import MongoClient
import random
from random import randint, choice, choices
import os
import random
import asyncio
from discord.utils import get
import datetime
import smtplib
import socket
from discord.utils import find
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import requests
from io import BytesIO

class user(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    clu= os.environ.get('MONGODB_URI')
    cluster = MongoClient(clu)
    db = cluster["topianbot"]
    collection = db["money"]
    collectionmodules = db["modules"]
    collectionshop = db["shop"]
    collectionticket = db["ticket"]
    collectionlogschannels = db["logschannels"]

        
    @commands.command()
    async def profile(self, ctx, user: discord.Member = None):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"]
        collection = db["money"]
        if user == None:
            user = ctx.author

        imge = Image.open("test4.jpg")
        img = imge.resize((400, 200))
        idraw = ImageDraw.Draw(img)

        headline = ImageFont.truetype('SansPosterBold.ttf', size = 20)

        headlines = ImageFont.truetype('Roboto-Medium.ttf', size = 15)
        name = str(user.name) + str('#') + str(user.discriminator)
        join = str("Member joined: ") + str(user.joined_at.strftime('%b %#d, %Y'))
        idraw.text((100, 20), name, font = headline, fill ="black")
        idraw.text((100, 45), join, font = headlines, fill ="black")
        
        num = ctx.author.guild.id
        num2 = user.id
        allnum = num + num2
        if collection.count_documents({"_id": allnum}) == 1:
            balance = collection.find_one({"_id": allnum})["balance"]
            bal = str("Balance: ") + str(balance) + str("$")
            idraw.text((10, 100), bal, font = headlines, fill ="black")
            message = collection.find_one({"_id": allnum})["message"]
            mes = str("Messages: ") + str(message)
            idraw.text((10, 130), mes, font = headlines, fill ="black")
            lv = collection.find_one({"_id": allnum})["lvl"]
            lvl = str("LVL: ") + str(lv)
            idraw.text((10, 160), lvl, font = headlines, fill ="black")

        
        asset = user.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((80, 80))

        img.paste(pfp, (10, 10))
        img.save('canvas.png')
        await ctx.send(file = discord.File("canvas.png"))

        
    @commands.command()
    async def wanted(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
        wanted = Image.open("wanted.jpg")
        asset = user.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((310, 310))

        wanted.paste(pfp, (160, 260))

        wanted.save("profile.jpg")
        await ctx.send(file = discord.File("profile.jpg"))


def setup(client):
    client.add_cog(user(client))
