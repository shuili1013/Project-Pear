import os
import discord
from discord import message
from discord.ext import commands
from discord import app_commands

import json
import time
import datetime
from datetime import datetime, timezone, timedelta
import requests
from bs4 import BeautifulSoup

intents = discord.Intents().all()
client = commands.Bot(command_prefix="-", owner_ids = [], intents=intents) #框框內輸入你的discord id
client.remove_command("help")

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        client.load_extension(f"cogs.{name}")

@client.event
async def on_ready():
    intents = discord.Intents.default()
    await client.change_presence(activity = discord.Streaming(name="", url="")) #機器人狀態 name=狀態名稱 url=超連結
    intents.message_content = True
    print(str(datetime.utcnow().astimezone(timezone(timedelta(hours=16)))).split(".",1)[0],"Bot is on ready",client.user)

    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            name = file[:-3]
            await client.load_extension(f"cogs.{name}")
            print(f"load cogs.{name}")

async def on_command_error(ctx, error):
    return

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    await client.load_extension(f'cogs.{extension}')
    await ctx.send(f"已成功載入 {extension} 套件")

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'已成功卸載 {extension} 套件')

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    await client.reload_extension(f'cogs.{extension}')
    await ctx.send(f'已重新載入 {extension} 套件')

@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency*100000)/100}ms")

@client.command(name="sync") 
@commands.is_owner()
async def sync(ctx):
    synced = await client.tree.sync()
    await ctx.send(f"同步了{len(synced)}個指令")


with open('config.json', "r") as file:
    config = json.load(file)
client.run(config['bot_token'])