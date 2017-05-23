import discord

client = discord.Client()

@client.event
async def on_message(message):
        # Bot must not respond to itself
        if message.author == client.user:
                return
        # Our test message params
        if message.content.startswith('!hello'):
                msg = 'Hello {0.author.mention}'.format(message)
                await client.send_message(message.channel, msg)

@client.event
async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('-----')

client.run('MzE2NTMxNjM5MTM4MjU0ODQ5.DAWxwA._Ofw-Jz8tZT0mdMoNT2PP5l_PxI')
