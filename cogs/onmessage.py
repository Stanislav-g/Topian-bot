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
    
    @commands.Cog.listener()
    async def on_message(self, message ):
        clu= os.environ.get('MONGODB_URI')
        cluster = MongoClient(clu)
        db = cluster["topianbot"]
        collection = db["money"]
        collectionmodules = db["modules"]
        collectionshop = db["shop"]
        collectionticket = db["ticket"]
        collectionlogschannels = db["logschannels"]        
        num1 = message.author.guild.id
        num22 = '111'
        allnum4 = str(num1) + str(num22)
        if collectionmodules.count_documents({"_id": allnum4}) == 1:
            if collectionmodules.find_one({"_id": allnum4})["lvls"] == 'on':
                num = message.author.guild.id
                num2 = message.author.id
                allnum = num + num2
                if collection.count_documents({"_id": allnum}) == 0:
                    name = message.author.name
                    num = message.author.guild.id
                    num2 = message.author.id
                    allnum = num + num2
                    collection.insert_one({"_id": allnum, "name": name, "balance": 0, "lvl": 0, "rep": 0, "message": 0})
                    
                else:
                    num = message.author.guild.id
                    num2 = message.author.id
                    allnum = num + num2
                    message = collection.find_one({"_id": allnum})["message"]
                    msg = int(message) + int('1')
                    collection.update_one({"_id": allnum}, {"$set": {"message": msg}}) 





def setup(client):
    client.add_cog(user(client))
