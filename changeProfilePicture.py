import discord

from config import bot_token as token

id = 791813040215425075

# Profile picture in ./res
pfp_path = "res/chad_profile.PNG"
fp = open(pfp_path, 'rb')
pfp = fp.read()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} connected to Discord')
    client.user.edit(avatar=pfp)
    await client.close()

client.run(token)
