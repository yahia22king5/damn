import discord
from discord.ext import commands

TOKEN = 'MTIwNzYyNDc1NzY5NzA2MDkyNA.GdjW9o.UmPYzX0sfaTBkm8uBTSxYSKDgLqadKsvtJb_hI'

intents = discord.Intents.default()
intents.typing = False
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        await bot.process_commands(message)
    else:
        member = message.author
        if message.content.startswith('!count'):
            if message.guild and discord.utils.get(message.guild.roles, name="Member") in member.roles:
                counter = 0
                while counter < 1000000:
                    counter += 1
                    await message.channel.send(counter)
            elif message.guild:
                await message.channel.send("You do not have permission to use this command.")
            else:
                counter = 0
                while counter < 1000000:
                    counter += 1
                    await message.channel.send(counter)

bot.run(TOKEN)
