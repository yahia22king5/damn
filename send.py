import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    owner = client.application.owner
    general_channel = discord.utils.get(client.get_all_channels(), name='general')
    async for message in general_channel.history(limit=1):
        owner_dm = await owner.create_dm()
        await owner_dm.send(f"Your bot is now online! Last message in general: {message.content}")

@client.event
async def on_member_join(member):
    welcome_message = "Welcome to the server! We're glad to have you here."
    await member.send(welcome_message)

# Replace 'YOUR_TOKEN_HERE' with your actual bot token
client.run('MTIwNzYyNDc1NzY5NzA2MDkyNA.GdjW9o.UmPYzX0sfaTBkm8uBTSxYSKDgLqadKsvtJb_hI')
