import datetime

import asyncio
import discord

import os

TOKEN = os.environ['TOKEN']
TIMECHANNEL = int(os.environ['TIMECHANNEL'])

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged on as {client.user}')
    while True:
        now = datetime.datetime.now() - datetime.timedelta(hours=4)
        await client.get_channel(TIMECHANNEL).edit(name=f"{now:%I-%M-%p-%b-%d} EST") # The channel gets changed here
        await asyncio.sleep(60)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f'Message from {message.author}: {message.content}')
    print(f"{message.channel.id}")
    if message.content.lower().find("what time") != -1:
        now = datetime.datetime.now()
        await message.channel.send(f"It is {now:%I:%M %p} EST on {now:%b %d}")

client.run(TOKEN)
