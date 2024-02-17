import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    welcome_message = "Welcome to the server! We're glad to have you here."
    await member.send(welcome_message)

# Replace 'YOUR_TOKEN_HERE' with your actual bot token
client.run('HEMTIwNzYyNDc1NzY5NzA2MDkyNA.GloxTZ.0keNbVz-6A_hsfjy8YuSZXz83jljOy0uNoi348')
