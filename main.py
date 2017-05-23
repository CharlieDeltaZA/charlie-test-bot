import discord
import credentials

client = discord.Client()

prefix = '!'                                                            # Try make this adjustable somehow?

@client.event
async def on_message(message):                                          # Indiv @events for every message command?
   # Bot must not respond to itself
   if message.author == client.user:
      return
   # Our test message params
   if message.content.startswith(prefix + 'hello'):                     # Greetings
      msg = 'Hello {0.author.mention}!'.format(message)
      await client.send_message(message.channel, msg)

   if message.content.startswith(prefix + 'ping'):                      # C'mon. This must be here.
      msg = 'Pong!'
      await client.send_message(message.channel, msg)

   if message.content.startswith(prefix + 'bbb'):                       # Why does this exist? I couldn't tell you really...
      msg = 'Bish Bash Bosh!'
      await client.send_message(message.channel, msg, tts=True)

@client.event
async def on_message(message):
   if message.content.startswith('How do you feel, Bot?')
      emoji = '🙃'                                                    # erm
      await client.add_reaction(message, emoji)


@client.event                                                           # Welcome new members to server
async def on_member_join(member):
   server = member.server
   fmt = 'Welcome {0.mention} to {1.name}!'
   await client.send_message(server, fmt.format(member, server))

        

@client.event                                                           # Debug text
async def on_ready():
   print('Logged in as')
   print(client.user.name)
   print(client.user.id)
   print('-----')
   await client.change_presence(game=discord.Game(name='with code'))   # Dis works 


client.run(credentials.Token)                                           # Run the client with the token
