#!/usr/bin/env python3
#Filename: index.py
"""
    DISCORD BOT --(Incomplete)
    Author : Vaibhav Sharma
    Version : 1.0

    This is a fun discord bot, used to get game related data and making gaming experience easier. This Bot is related to the game C.A.T.S also known as Cats Arena Turbo Stars. It shows different stats of particular parts like weapon/body/wheels etc.
    I am also working on another bot, World Atlas bot. Which will help to get any country data, from map to it's currency/language/capital and much more by using some advanced topics like Webscrapping(--Incomplete--) and it's been mixed/combined with this same bot for testing purposes.

    The code uses Offical Discord bot API, to connect and send bot online. 
    
    Offical documentation can be found on - https://discordpy.readthedocs.io/en/latest/

"""

#Importing required modules.
import os                       #Connecting the API with OS. 
import json, csv                #To access source data files
import discord                  #Python discord API
from dotenv import load_dotenv  #Importing the .env TOKEN file
import requests                 #Html parser module
from bs4 import BeautifulSoup   #Webscrapping API BeautifulSoup

#Loading the .env file from same directory.
load_dotenv()

#Getting the bot token from the .env file to send it online.
TOKEN = os.getenv('DISCORD_TOKEN')

#Lists for storing the Places and links from CSV data file.
places = []
links = []

#Reading the source data of CSV and JSON file and loading them.
#CSV (From directory ' ./CSVfiles ' ) in ReadOnly mode.
with open('CSVfiles/countries.csv', 'r', newline='') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        places.append(row[0])
        links.append(row[1])
#JSON(From directory ' ./JSONfiles ' ) in ReadOnly mode.
json_data1 = json.load(open('JSONfiles/bodies.json' , 'r'))
json_data2 = json.load(open('JSONfiles/copies.json' , 'r'))
json_data3 = json.load(open('JSONfiles/gadgets.json', 'r'))
json_data4 = json.load(open('JSONfiles/weapons.json', 'r'))
json_data5 = json.load(open('JSONfiles/wheels.json' , 'r'))

#Getting Parts in python-lists using loops
bodies = []
for i in range(22):
    data1 = json_data1[i]
    bodies.append(data1['a'].lower().replace(" ", ""))

copies = []
for i in range(5):
    data2 = json_data2[i]
    copies.append(data2['a'].lower().replace(" ", ""))

gadgets = []
for i in range(26):
    data3 = json_data3[i]
    gadgets.append(data3['a'].lower().replace(" ", ""))

weapons = []
for i in range(28):
    data4 = json_data4[i]
    weapons.append(data4['a'].lower().replace(" ", ""))

wheels = []
for i in range(42):
    data5 = json_data5[i]
    wheels.append(data5['a'].lower().replace(" ", ""))

#Incomplete atlast bot.

"""with open('flags.csv', 'r', newline='') as csvFile2:
    reader2 = csv.reader(csvFile2)
    for row in reader2:
        flags.append(row[0])
        links2.append(row[1])
"""     

class CustomClient(discord.Client):
    """Custom class which is subclass of discord.Client"""

    """
        Discord API uses Asynchronous programming like concurrency, parallelism, Threading or multiprocessing.
    """
    async def on_ready(self) -> str:
        #Signal to check the connectivity of bot to server.
        print(f'{self.user} has been connected to discord')


    async def on_message(self, message):
        #Message detection by bot.
        if message.author == self.user:
            #If the message is send by bot itself, then it returns NOTHING.
            #self.user is a instance from the superclass discord.Client
            return

        """
            Else, if the message content states other IF conditions 
            True, then respective condition will be executed.
        """

        #HELP command.
        if message.content[1:] == 'help':
            response = """```
            For the Game data.
                Categories:
                1: Bodies
                2: Copies(+Cost)
                3: Gadgets
                4: Weapons
                5: Wheels
                Type - $bodies, etc.

            For map of any Country.
                This bot is mixed with a small(On process) Atlas bot.

                Type -> $map-list --- To list the country names.
                Type -> $map-(Country)

                Kindly replace the Country with BRACKETS with the name ofcountry for map.
                        ```"""
        await message.channel.send(response)

        #listing the whole list of map.
        if message.content == '$map-list':
            response = '\n'.join(places)
            await message.channel.send(f"```{response}```")

        #Map
        if message.content.startswith('$map-'):

            place = message.content[5:].lower()
            if place in places:
                index = places.index(place)
                await message.channel.send(links[index])

        #Listing the whole list of parts(Bodies, Copies, Gadgets, Weapons and Wheels)
        if message.content[1:].lower() == 'bodies':
            response = "\n".join(bodies)
            await message.channel.send(f"```{response}```")

        if message.content[1:].lower() == 'copies':
            response = "\n".join(copies)
            await message.channel.send(f"```{response}```")

        if message.content[1:].lower() == 'gadgets':
            response = "\n".join(gadgets)
            await message.channel.send(f"```{response}```")

        if message.content[1:].lower() == 'weapons':
            response = "\n".join(weapons)
            await message.channel.send(f"```{response}```")

        if message.content[1:].lower() == 'wheels':
            response = "\n".join(wheels)
            await message.channel.send(f"```{response}```")

        #Output formatting
        #Bodies.
        if message.content[1:] in bodies:
            health = json_data1[bodies.index(message.content[1:])]
            response = f"""
        Name     = {health['a']}
        Battery  = {health['b']}
        rarity   = {health['c']}
        Health   = {health['d']}
        Bonus    = {health['e']}
        --------------------------
        Level-1  = {health['1']}
        Level-2  = {health['2']}
        Level-3  = {health['3']}
        Level-4  = {health['4']}
        Level-5  = {health['5']}
        Level-6  = {health['6']}
        Level-7  = {health['7']}
        Level-8  = {health['8']}
        Level-9  = {health['9']}
        Level-10 = {health['10']}
        Level-11 = {health['11']}
        Level-12 = {health['12']}
        Level-13 = {health['13']}
        """
            await message.channel.send(f'```{response}```')

        #Copies
        if message.content[1:] in copies:
            copy = json_data2[copies.index(message.content[1:])]
            response = f"""
        Type  = {copy['a']}
        ----------------------
        Level Parts  == Cost
        ----------------------
        2     {copy['1']}         {copy['2']}
        3     {copy['3']}         {copy['4']}
        4     {copy['5']}         {copy['6']}
        5     {copy['7']}         {copy['8']}
        6     {copy['9']}         {copy['10']}
        7     {copy['11']}        {copy['12']}
        8     {copy['13']}        {copy['14']}
        9     {copy['15']}        {copy['16']}
        10    {copy['17']}       {copy['18']}
        11    {copy['19']}       {copy['20']}
        12    {copy['21']}       {copy['22']}
        13    {copy['23']}       {copy['24']}

        """
            await message.channel.send(f'```{response}```')

        #Gadgets
        if message.content[1:] in gadgets:
            health = json_data3[gadgets.index(message.content[1:])]
            response = f"""
        Name     = {health['a']}
        Battery  = {health['b']}
        rarity   = {health['c']}
        Health   = {health['d']}
        Bonus    = {health['e']}
        --------------------------
        Level-1  = {health['1']}
        Level-2  = {health['2']}
        Level-3  = {health['3']}
        Level-4  = {health['4']}
        Level-5  = {health['5']}
        Level-6  = {health['6']}
        Level-7  = {health['7']}
        Level-8  = {health['8']}
        Level-9  = {health['9']}
        Level-10 = {health['10']}
        Level-11 = {health['11']}
        Level-12 = {health['12']}
        Level-13 = {health['13']}
        """
            await message.channel.send(f'```{response}```')

        #Weapons
        if message.content[1:] in weapons:
            damage = json_data4[weapons.index(message.content[1:])]
            response = f"""
        Name     = {damage['a']}
        Battery  = {damage['b']}
        rarity   = {damage['c']}
        Damage   = {damage['d']}
        Bonus    = {damage['e']}
        --------------------------
        Level-1  = {damage['1']}
        Level-2  = {damage['2']}
        Level-3  = {damage['3']}
        Level-4  = {damage['4']}
        Level-5  = {damage['5']}
        Level-6  = {damage['6']}
        Level-7  = {damage['7']}
        Level-8  = {damage['8']}
        Level-9  = {damage['9']}
        Level-10 = {damage['10']}
        Level-11 = {damage['11']}
        Level-12 = {damage['12']}
        Level-13 = {damage['13']}
        """
            await message.channel.send(f'```{response}```')

        #Wheels
        if message.content[1:] in wheels:
            health = json_data5[wheels.index(message.content[1:])]
            response = f"""
        Name     = {health['a']}
        Battery  = {health['b']}
        rarity   = {health['c']}
        Health   = {health['d']}
        Bonus    = {health['e']}
        --------------------------
        Level-1  = {health['1']}
        Level-2  = {health['2']}
        Level-3  = {health['3']}
        Level-4  = {health['4']}
        Level-5  = {health['5']}
        Level-6  = {health['6']}
        Level-7  = {health['7']}
        Level-8  = {health['8']}
        Level-9  = {health['9']}
        Level-10 = {health['10']}
        Level-11 = {health['11']}
        Level-12 = {health['12']}
        Level-13 = {health['13']}
        """
            await message.channel.send(f'```{response}```')

        #Incomplete Atlast bot, still in progress.

        """if message.content.startswith('$flag-'):

            flag = message.content[5:].lower()
            if flag in flags:
                country = links2[flags.index(flag)]
                response = requests.get(country)

                if response.status_code != 200:
                    await message.channel.send("Sorry this can't be reached right now")
                    return
                soup = BeautifulSoup(response.content, 'html.parser')
                x = soup.find_all(class_='b-lazy')
                y = x[9]
                await message.channel.send(site)
        """

def Main():
    #Creating an instance of CustomClient class and running it with bot token.
    client = CustomClient()
    client.run(TOKEN)


if __name__ == '__main__':
    Main()