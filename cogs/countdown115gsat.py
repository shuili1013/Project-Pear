import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord import app_commands
from core.any import Cog_Extension
from datetime import datetime

class countdown115gsat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.hybrid_command(
    name="countdown115gsat",
    description="倒數學測"
    )
    
    async def countdown(self, ctx):
        target_date = datetime(2026, 1, 18)
        today = datetime.now()
        delta = target_date - today
        
        embed = discord.Embed (
            title = "倒數 115 學測",
            description = f"115 學測還有 {delta.days} 天 ! (實際天數以大考中心公布為準)",
            color = discord.Color.blue()
            )
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(countdown115gsat(bot))
