import discord
from discord.ext import commands
from mland_db.mland_db_logic import mland_db_embed

def setup(bot):
    @bot.command(name="메랜디비", aliases=["메디비", "매랜디비", "매디비", "db", "유"])
    async def maple_db(ctx):
        embed = mland_db_embed()
        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="사이트 바로가기", url="https://mapledb.kr/"))
        await ctx.send(embed=embed, view=view)
