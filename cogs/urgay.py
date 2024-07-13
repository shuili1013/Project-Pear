import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord import app_commands
from core.any import Cog_Extension
import random

class URGay(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @bot.hybrid_command(
    name="hello",
    description="機器人向你問好"
    )
    async def _hello(self,ctx):
        await ctx.send(f"<@{ctx.author.id}> ，嗨 ") #<@{ctx.author.id}> 為觸發該指令的使用者

async def setup(bot):
    await bot.add_cog(URGay(bot))