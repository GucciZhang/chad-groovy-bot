import discord

from config import bot_token as token

client = discord.Client()

commands = [
    "-play",
    "-skip",
    "-join",
    "-queue",
    "-next",
    "-back",
    "-clear",
    "-jump",
    "-loop",
    "-lyrics",
    "-pause",
    '-resume',
    "-remove",
    "-disconnect",
    "-shuffle",
    "-song",
    "-24/7",
    "-bass",
    "-volume",
    "-speed",
    "-pitch",
    "-nightcore",
    "-vaporwave",
    "-reset",
    "-fast",
    "-rewind",
    "-search",
    "-seek",
    "-stop",
    "-move",
    "-saved",
    "-prefix",
    "-announce",
    "-perms"]

groovy_user_id = 234395307759108106
groovy_channel_id = 746892961958199370

@client.event
async def on_ready():
    print(f'{client.user} connected to Discord')


@client.event
async def on_message(message):
    sender = message.author
    groovy_channel = client.get_channel(groovy_channel_id)

    if sender == client.user:
        return

    if message.channel != groovy_channel:
        if sender.id == groovy_user_id:
            new_content = message.content
            new_embed = message.embeds[0] if message.embeds else None
            await groovy_channel.send(content=new_content, embed=new_embed)
            await message.delete()

        else:
            tokens = message.content.split()
            if tokens and tokens[0] in commands:
                embed = discord.Embed()
                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.description = message.content
                await groovy_channel.send(embed=embed)

                await message.delete()


client.run(token)
