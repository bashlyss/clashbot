import datetime

import os
import asyncio

import discord

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
        now = datetime.datetime.now() - datetime.timedelta(hours=4)
        await message.channel.send(f"It is {now:%I:%M %p} EST on {now:%b %d}")

@client.event
async def on_reaction_add(reaction, user):
    is_raffle = reaction.message.content.lower().find('raffle') != -1
    if is_raffle:
        print(reaction.emoji)
    if is_raffle and reaction.emoji == "kirby":
        users = await reaction.users().flatten()
        winner = random.choice(users)
        await reaction.message.channel.send(f"Bouncing Kirby raffle winner is {winner}")

client.run(TOKEN)
