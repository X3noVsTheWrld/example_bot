import discord
from dotenv import load_dotenv
import os
import random

#load variables from .env file
load_dotenv()
TOKEN = os.getenv('TOKEN')

omega_id = os.getenv('omega_id')
omegabot_id = os.getenv('omegabot_id')
jeff_id = os.getenv('jeff_id')

words = []
with open("words.txt", "r") as file:
    for line in file:
        word = line.strip()
        words.append(word)

scrambled_word = ""

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        print(message.author.id)
        if message.content == "/scramble":
            await message.channel.send("Sending scramble word...")
            random_word = random.choice(words)
            print(random_word)
            random_letters = list(random_word)
            random.shuffle(random_letters)
            global scrambled_word
            scrambled_word = random_word
            scramble = "".join(random_letters)
            await message.channel.send("***Unscramble this word***: " + scramble)

        if message.content == scrambled_word:
            await message.channel.send("Hey, " + message.author.name + " got the scramble puzzle correct!")

        if message.author.id == omega_id:
            await message.channel.send("Can't do the Moon Easter Egg Solo, you Nincompoop.")
        if message.author.id == jeff_id:
            await message.channel.send("Stop rage typing in chat, you Nincompoop.")
        if message.content == 'ping':
            await message.channel.send('pong')
        if message.author.id == omegabot_id:
            await message.channel.send("https://i.pinimg.com/originals/96/60/9b/96609b72bf4c9ffe04ed9284f111be24.gif")   

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)