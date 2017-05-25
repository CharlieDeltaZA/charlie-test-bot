# Bot code

import discord
import credentials

client = discord.Client()

@client.event
async def on_message(message):                                          # Indiv @events for every message command?
   # Bot must not respond to itself
   if message.author == client.user:
      return
   # Our test message params
   if message.content.startswith('!hello'):                     # Greetings
      msg = 'Hello {0.author.mention}!'.format(message)
      await client.send_message(message.channel, msg)

@client.event                                                           # Debug text
async def on_ready():
   # DateTime = datetime.datetime.now()
   print('Logged in as')
   print(client.user.name)
   print(client.user.id)
   # print(DateTime.strftime("%Y-%m-%d %H:%M:%S"))                                                 # Debugging
   print('----------')
   # await client.change_presence(game=discord.Game(name='with code'))   # Dis works 


client.run(credentials.Token)                                           # Run the client with the token
