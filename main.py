import discord
import os
import time
import requests

from discord.ext import commands
from discord_slash import SlashCommand

prefix = ('?')
client = commands.Bot(intents=discord.Intents.all(), command_prefix=prefix, help_command=None)
slash = SlashCommand(client, sync_commands=True)
token = os.environ['token']

@client.event
async def on_connect():
    os.system('clear||cls')
    print(f'CONNECTED : {client.user}\nPREFIX : {prefix}\nCOMMANDS : {prefix}imagine <prompt>')
    return

@client.event
async def on_command_error(ctx, error):
    return

# ...

@slash.slash(name="imagine", description="Generate an image based on a prompt")
async def _imagine(ctx, prompt: str):
    imagine = prompt
    await ctx.send(f'{ctx.author.mention} **Generating your image on the prompt:** {imagine}')
    url = f"https://image.pollinations.ai/prompt/{imagine}"
    response = requests.get(url)

    if response.status_code == 200:
        file = discord.File(io.BytesIO(response.content), filename="image.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file, embed=embed)
    else:
        await ctx.send("Failed to generate the image.")

client.run(token)
