import discord
from dotenv import load_dotenv
import os

#load variables from .env file
load_dotenv()
TOKEN = os.getenv('TOKEN')

omega_id = 219593665201438720
omegabot_id = 1434682224070103162
jeff_id = 1096612044897255444


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        print(message.author.id)
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