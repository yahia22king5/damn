import openai
import discord
from discord.ext import commands

TOKEN = 'MTIwNzYyNDc1NzY5NzA2MDkyNA.GdjW9o.UmPYzX0sfaTBkm8uBTSxYSKDgLqadKsvtJb_hI'
OPENAI_API_KEY = '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'

openai.api_key = OPENAI_API_KEY

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def gpt(ctx, *, prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50
    )

    await ctx.send(response.choices[0].text.strip())

bot.run(TOKEN)
