import discord
from discord.ext import commands

TOKEN = 'MTIwNzYyNDc1NzY5NzA2MDkyNA.GdjW9o.UmPYzX0sfaTBkm8uBTSxYSKDgLqadKsvtJb_hI'

intents = discord.Intents.default()
intents.typing = False
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def invite(ctx):
    invites = []
    for guild in bot.guilds:
        invite = await guild.text_channels[0].create_invite(max_age=86400)  # Create an invite for the first text channel
        invites.append(invite.url)
    
    await ctx.author.send('\n'.join(invites))

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

bot.run(TOKEN)
