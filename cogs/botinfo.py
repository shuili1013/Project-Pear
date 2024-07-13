import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord import app_commands
from core.any import Cog_Extension
from .utils.date import get_date,get_time
from datetime import datetime

class info(commands.Cog):
    def __init__(self, bot:commands.bot):
        self.bot = bot 


    @bot.hybrid_command(
    name="info",
    description="機器人內容"
    ) 
    async def _info(self, ctx):
        try:
            embed = discord.Embed (color=discord.Colour.blurple(), title="About",
                                   description="this bot is powered by discord.py")
            embed.set_author(name="shuili", url="https://www.youtube.com/channel/UCrz4htYxkzF6hElhKg9ceWg",
                         icon_url="https://cdn.discordapp.com/emojis/1210514388042121268.webp?size=128&quality=high")
            embed.set_thumbnail(
            url="https://cdn.discordapp.com/emojis/1087600137347530822.webp?size=128&quality=high")
            embed.set_footer(text=get_date())



            embed.add_field(name="Link",
                            value="[Youtube](https://www.youtube.com/channel/UCrz4htYxkzF6hElhKg9ceWg)\n \
                                [Twitch](https://www.twitch.tv/shuili15yyy)",inline=True)
            embed.add_field(name="Bot info", value="made by shuili \npowered by discord.py", inline=True)
            

            guild = ctx.guild
            channel = ctx.channel
            await ctx.send(embed=embed)
        except Exception as e:
            print(e)
    

async def setup(bot):
    await bot.add_cog(info(bot))