import discord
import credentials

client = discord.Client()

@client.event
async def on_message(message):
   # Bot must not respond to itself
   if message.author == client.user:
      return
   # Our test message params
   if message.content.startswith('!hello'):
      msg = 'Hello {0.author.mention}' #.format(message)
      await client.send_message(message.channel, msg)

   if message.content.startswith('!ping'):
      msg = 'Pong!'
      await client.send_message(message.channel, msg)

# @client.event
# async def on_message(message):


@client.event
async def on_ready():
   print('Logged in as')
   print(client.user.name)
   print(client.user.id)
   print('-----')

client.run(credentials.Token)
