import discord
from discord.ext import commands
import asyncio
import random

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

messages = [
    "Hi mom", "abcdefghijklmnopqrstuvwxyz", "sophis", "roblox da best",
    "apple", "banana", "carrot", "dog", "elephant",
    "flower", "guitar", "house", "igloo", "jungle",
    "keyboard", "laptop", "mouse", "notebook", "orange",
    "piano", "queen", "rabbit", "snake", "turtle",
    "umbrella", "violin", "window", "xylophone", "yogurt",
    "zebra", "airplane", "book", "cloud", "desk",
    "eagle", "fish", "globe", "hammer", "icecream"
]

async def send_message_to_owner(owner_dm):
    while True:
        message = random.choice(messages)
        await owner_dm.send(message)
        await asyncio.sleep(1)  # Send a message every 1 second

@bot.event
async def on_ready():
    if bot.user is not None:
        print('Logged in as {0}'.format(bot.user))
    else:
        print('Logged in, but bot user not yet available.')

@bot.command()
async def start(ctx):
    if ctx.guild is None:  # Check if the command was invoked in a DM
        if not hasattr(bot, 'owner_dm'):
            bot.owner_dm = await bot.application.owner.create_dm()
            bot.task = bot.loop.create_task(send_message_to_owner(bot.owner_dm))
            await ctx.send("Message sending started.")
        else:
            await ctx.send("Message sending is already started.")
    else:
        await ctx.send("This command can only be used in a direct message to the bot.")

@bot.command()
async def stop(ctx):
    if ctx.guild is None:  # Check if the command was invoked in a DM
        if hasattr(bot, 'owner_dm'):
            bot.task.cancel()
            del bot.owner_dm
            del bot.task
            await ctx.send("Message sending stopped.")
        else:
            await ctx.send("Message sending is not started yet.")
    else:
        await ctx.send("This command can only be used in a direct message to the bot.")

# Replace 'YOUR_TOKEN_HERE' with your actual bot token
bot.run('MTIwNzYyNDc1NzY5NzA2MDkyNA.GdjW9o.UmPYzX0sfaTBkm8uBTSxYSKDgLqadKsvtJb_hI')
