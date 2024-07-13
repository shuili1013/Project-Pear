from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
from pysaucenao import SauceNao, PixivSource

class saucenao(Cog_Extension):
    
    @bot.hybrid_command(
    name="saucenao",
    description="透過saucenao api 來以圖搜圖"
    )
    
    async def sauce(self, ctx, img_url: str):
        if not img_url:
            await ctx.send("訊息中完全沒有附帶圖片")
            return
        
        sauce = SauceNao(api_key="YOUR API")

        results = await sauce.from_url(img_url)
        len(results)
        results.short_remaining  # 3 (per 30 seconds limit)
        results.long_remaining
        results[0].type  # pixiv
        isinstance(results[0], PixivSource)  # True
        
        try:
            results = await sauce.from_url(img_url)
        except:
            return
        
        first_result = results[0]

        if isinstance(first_result, PixivSource):
            author_url = first_result.author_url
        else:
            author_url = "非Pixiv結果無法顯示"

        embed = discord.Embed(
            title="SauceNAO 搜圖結果",
            color=discord.Color.blurple()
        )

        embed.set_thumbnail(url=results[0].thumbnail)

        embed.add_field(name="Title", value=results[0].title, inline=False)
        embed.add_field(name="Author", value=results[0].author_name, inline=False)
        if author_url:
            embed.add_field(name="Author Link", value=f"[Link]({author_url})", inline=False)
        embed.add_field(name="Similarity", value=results[0].similarity, inline=False)
        embed.add_field(name="Sauce", value=f"[Link]({results[0].url})", inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(saucenao(bot))