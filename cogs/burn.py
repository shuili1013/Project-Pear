import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord import app_commands
from core.any import Cog_Extension
import random

class burn(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @bot.hybrid_command(
    name="burn",
    description="燃燒機器人"
    )
    async def _burn(self,ctx):
        await ctx.send(f"🔥🔥🔥🔥🔥<@{self.bot.user.id}>🔥🔥🔥🔥🔥")

async def setup(bot):
    await bot.add_cog(burn(bot))