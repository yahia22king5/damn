import discord
from discord.ext import commands

TOKEN = 'MTIwNzYyNDc1NzY5NzA2MDkyNA.GdjW9o.UmPYzX0sfaTBkm8uBTSxYSKDgLqadKsvtJb_hI'

intents = discord.Intents.default()
intents.typing = False
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def strator(ctx):
    roles_info = []
    for guild in bot.guilds:
        highest_role = guild.me.top_role
        roles_info.append(f'Highest role in {guild.name}: {highest_role.name}')

    await ctx.author.send('\n'.join(roles_info))

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

bot.run(TOKEN)
