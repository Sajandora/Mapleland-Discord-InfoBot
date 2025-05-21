import discord
from discord.ext import commands

def setup(bot):
    @bot.command(name="help", aliases=["도움", "도움말"])
    async def custom_help(ctx):
        embed = discord.Embed(
            title="📌 메이플 봇 도움말",
            description="사용 가능한 명령어 목록입니다.",
            color=discord.Color.gold()
        )
        embed.add_field(
            name="메랜디비",
            value="메이플랜드 DB 사이트로 이동합니다.\n"
            "•`!메랜디비`, `!메디비`, `!매랜디비`, `!매디비`, `!db`, `!유`",
            inline=False
        )
        embed.add_field(
            name="\u200b",
            value="몬스터, 아이템, 맵 세부 검색\n"
            "•`!(몬스터 or 아이템 or 맵 이름)`",
            inline=False
        )
        
        embed.add_field(name="\u200b", value="\u200b", inline=False)

        embed.add_field(
            name="!메랜지지",
            value="메랜지지 사이트로 이동합니다. \n"
            "•`!메랜지지`, `!메지지`, `!매랜지지`, `!매지지`, `!경매장`, `!거래`, `!검색`, '!시세'\n",
            inline=False
        )
        embed.add_field(
            name="\u200b",
            value="세부 아이템 검색 시 위의 명령어 + 아이템이름 작성\n"
            "•`!경매장 쏜즈`",
            inline=False
        )
         
        embed.set_footer(text="문의: 사잔도라")
        await ctx.send(embed=embed)
