import discord
from discord.ext import commands
import asyncio

TOKEN = 'MTIwNzYyNDc1NzY5NzA2MDkyNA.GdjW9o.UmPYzX0sfaTBkm8uBTSxYSKDgLqadKsvtJb_hI'

intents = discord.Intents.default()
intents.typing = False
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def help_message(ctx):
    message = """
    **Available Commands:**
    !help_message - Displays this help message.
    !count - Counts to 1 million.
    !nocount - Stops counting.
    !start - Starts sending messages.
    !stop - Stops sending messages.
    """
    await ctx.send(message)

@bot.command()
async def count(ctx):
    counter = 0
    while counter < 1000000:
        counter += 1
        await ctx.send(counter)

@bot.command()
async def nocount(ctx):
    pass

@bot.command()
async def start(ctx):
    await ctx.send("Starting to send messages.")
    while True:
        await asyncio.sleep(1)

@bot.command()
async def stop(ctx):
    await ctx.send("Stopping sending messages.")

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

bot.run(TOKEN)
