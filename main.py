import discord
import os
import requests

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$Debug'):
        await message.channel.send('Debug-Info:')
        await message.channel.send(message.channel)
        await message.channel.send(message.channel.type)
        await message.channel.send(message.author)
        await message.channel.send(message.author.id)
        await message.channel.send(message.id)
        await message.channel.send(message.attachments)
        await message.channel.send(message.created_at)

    if message.content.startswith('Activity'):
        streaming = discord.Streaming(name="Online", url="")
        await client.change_presence(status=discord.Status.idle, activity=streaming)

    if message.content.startswith('$Webhook'):
        Me = 941035467804139581
        if message.author.id == Me:
            text = message.content
            text = text[8:]
            r = requests.post('https://discord.com/api/webhooks/977034068258615307/kGnDVtNjeT1zB3dABj8AE_sHlYJOiuDpGP7X4WqNXuaUw2jfVQ2ZYguMrAz_wH-Tstzv', data={
                "username": "Bot-User",
                "content": text
            })

client.run(os.environ["DISCORD_TOKEN"])
