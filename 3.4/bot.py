# Bot code
# Python 3.4

import discord
import credentials
import commands
import datetime
import asyncio
import tmdbsimple as tmdb

client = discord.Client()

@client.event
@asyncio.coroutine
def on_message(message):                                          # Indiv @events for every message command?
   # Bot must not respond to itself
  if message.author == client.user:
     return
   # Our test message params
  if message.content.startswith('*hello'):                     # Greetings
     msg = 'Hello {0.author.mention}!'.format(message)
     yield from client.send_message(message.channel, msg)

  if message.content.startswith('*ping'):                      # C'mon. This must be here.
     msg = 'Pong!'
     yield from client.send_message(message.channel, msg)

  if message.content.startswith('*bbb'):                       # Why does this exist? I couldn't tell you really...
     msg = 'Bish Bash Bosh!'
     yield from client.send_message(message.channel, msg, tts=True)

  if message.content == 'How do you feel, Bot?':                 #FeelsBadMan
     emoji = '<:NotLikeThis:314339829385265153>'                                                    # erm   [\N{UPSIDE-DOWN FACE}]
     yield from client.add_reaction(message, emoji)

  if message.content.startswith('*help'):                        # Send a PM to the user with a list of commands sourced elsewhere & formatted
     msg = commands.Help
     yield from client.send_message(message.author, msg)

  if message.content.startswith('*lul'):
     msg_og = '<:NotLikeThis:314339829385265153>'                # Repeat what will be :lol: (lul?) 5 times, you know, for the lulz
     msg = (msg_og + '\n') * 5
     yield from client.send_message(message.channel, msg)

  if message.content.startswith('*movie'):                        # Unable to test due to tmdbsimple failing to install. Great.
     tmdb.API_KEY = (credentials.tmdb_API)
     movie = tmdb.movie(603)
     response = movie.info()
     msg = movie.title
     yield from client.send_message(message.channel, msg)

#   '''if message.content.startswith('James is a noob'):                          # Wonder if this will work?
#      usr = client.get_all_members()
#      print(usr)
#      msg = 'Yes, I can confirm that {} is a noob!'
#      await client.send_message(message.channel, msg)'''


#@client.event
#async def on_message(message):
#   if message.content.startswith('How do you feel, Bot?'):           # FUCKING SYNTAX GOD DAMNIT

@client.event                                                           # Welcome new members to server
@asyncio.coroutine
def on_member_join(member):
  server = member.server
  msg = 'Welcome {0.mention} to {1.name}!'
  yield from client.send_message(server, msg.format(member, server))
   

@client.event                                                           # Debug text
@asyncio.coroutine
def on_ready():
  DateTime = datetime.datetime.now()
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print(DateTime.strftime("%Y-%m-%d %H:%M:%S"))                                                 # Debugging
  print('----------')
  yield from client.change_presence(game=discord.Game(name='with old code | *help'))   # Dis works 


client.run(credentials.Token)                                           # Run the client with the token
