# sub2/mland_gg_logic.py
import discord

def mland_gg_embed():
    embed = discord.Embed(
        title="메랜지지",
        description="메랜지지 사이트로 이동합니다.",
        url="https://mapleland.gg/",
        color=discord.Color.blurple()
    )
    embed.set_footer(text="출처: mapleland.gg")
    embed.set_thumbnail(url="https://mapleland.gg/favicon.png")  # 예시 썸네일
    return embed
