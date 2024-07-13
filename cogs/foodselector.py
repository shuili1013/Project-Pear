import discord
from discord.ext import commands
from discord.ext.commands import bot 
from discord import app_commands
from core.any import Cog_Extension
import random

class FoodSelector(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="foodselector", description="選擇一種食物類型 機器人將會推薦你吃些甚麼")
    async def choose_food(self, interaction: discord.Interaction):
        
        options = {
            "日式": ["丸龜製麵", "すき家", "吉野家", "CoCo壹番屋","一蘭拉麵"],
            "速食": ["麥當勞", "薩利亞", "漢堡王", "KFC","摩斯漢堡"],
            "台灣小吃": ["鹽酥雞", "臭豆腐", "肉圓", "雞排","珍珠奶茶","蔥油餅","地瓜球"]
        }

        view = discord.ui.View()

        select = discord.ui.Select(
            placeholder="選擇一種食物類型 owo!",
            min_values=1,
            max_values=1,
            options=[
                discord.SelectOption(label="日式", description="推薦你一家日式餐廳"),
                discord.SelectOption(label="速食", description="推薦你一家速食餐廳"),
                discord.SelectOption(label="台灣小吃", description="推薦你一種台灣小吃")
            ]
        )

        async def select_callback(interaction: discord.Interaction):
            selected_option = select.values[0]
            if selected_option in options:
                choice = random.choice(options[selected_option])
                await interaction.response.send_message(f"你選擇了 {selected_option} ,我推薦你吃 {choice}")

        select.callback = select_callback
        view.add_item(select)

        await interaction.response.send_message("請選擇一種食物類型：", view=view)

async def setup(bot):
    await bot.add_cog(FoodSelector(bot))