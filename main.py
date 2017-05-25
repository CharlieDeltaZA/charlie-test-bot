# Main file for charlie-test-bot

# No longer in use - 25/05/2017

import discord
import credentials
#import commands
import datetime                                                         # For debugging `on_ready`

client = discord.Client()

# prefix = '!'                                                            # Try make this adjustable somehow?

@client.event
async def on_message(message):                                          # Indiv @events for every message command?
   # Bot must not respond to itself
   if message.author == client.user:
      return
   # Our test message params
   if message.content.startswith('!hello'):                     # Greetings
      msg = 'Hello {0.author.mention}!'.format(message)
      await client.send_message(message.channel, msg)

   if message.content.startswith('!ping'):                      # C'mon. This must be here.
      msg = 'Pong!'
      await client.send_message(message.channel, msg)

   if message.content.startswith('!bbb'):                       # Why does this exist? I couldn't tell you really...
      msg = 'Bish Bash Bosh!'
      await client.send_message(message.channel, msg, tts=True)

   #if message.content == 'How do you feel, Bot?':
   #   emoji = '\N{UPSIDE-DOWN FACE}'                                                    # erm
   #   await client.add_reaction(message, emoji)

@client.event
async def on_message(message):
#   if message.content.startswith('How do you feel, Bot?'):           # FUCKING SYNTAX GOD DAMNIT
   if message.author == client.user:
      return
   
   if message.content == 'How do you feel, Bot?':
      emoji = '\N{UPSIDE-DOWN FACE}'                                                    # erm
      await client.add_reaction(message, emoji)   

#@client.event
#async def on_message(message):                                       # Send a PM to the user with a list of commands sourced elsewhere & formatted
#   if message.content.startswith('!help'):
#      msg = commands.Help
#      await client.send_message(message.author, msg)


#@client.event                                                           # Welcome new members to server
#async def on_member_join(member):
#   server = member.server
#   msg = 'Welcome {0.mention} to {1.name}!'
#   await client.send_message(server, msg.format(member, server))

        

@client.event                                                           # Debug text
async def on_ready():
   DateTime = datetime.datetime.now()
   print('Logged in as')
   print(client.user.name)
   print(client.user.id)
   print(DateTime.strftime("%Y-%m-%d %H:%M:%S"))                                                 # Debugging
   print('----------')
   await client.change_presence(game=discord.Game(name='with code'))   # Dis works 


client.run(credentials.Token)                                           # Run the client with the token
