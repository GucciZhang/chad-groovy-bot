import discord

from config import bot_token

# Token set in config.py
token = bot_token

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} connected to Discord')

    print(f"{client.user} is connected to the following servers:")
    for guild in client.guilds:
        print(f"{guild.name} (id: {guild.id})")

        print(f"{guild.member_count} members:")
        async for member in guild.fetch_members():
            print(f"{member.name} (id: {member.id})")

        channels = await guild.fetch_channels()
        for channel in channels:
            print(f"{channel.name} (id: {channel.id})")

    await client.close()

client.run(token)
