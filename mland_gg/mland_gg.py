# sub2/mland_gg.py
import discord
from discord.ext import commands
from mland_gg.mland_gg_logic import mland_gg_embed
import json
import os

# ✅ 아이템 JSON 불러오기 (경로 조정 필요시 수정)
with open(os.path.join(os.path.dirname(__file__), "../data/items.json"), encoding="utf-8") as f:
    item_data = json.load(f)

item_dict = {item["name_ko"]: item["code"] for item in item_data}

# ✅ 명령어 등록 함수
def setup(bot):

    # 메이플랜드 안내 + 검색 명령어 통합
    @bot.command(name="메랜지지", aliases=["메지지", "매랜지지", "매지지", "경매장", "거래", "검색", "시세"])
    async def maple_gg(ctx, *, keyword: str = None):
        if not keyword:
            embed = mland_gg_embed()
            embed.color = discord.Color.orange()
            embed.set_thumbnail(url="https://maplestory.io/api/gms/62/npc/1061001/icon?resize=3")
            view = discord.ui.View()
            view.add_item(discord.ui.Button(label="사이트 바로가기", url="https://mapleland.gg/"))
            await ctx.send(embed=embed, view=view)
            return

        matched = [(name, code) for name, code in item_dict.items() if keyword in name]

        if not matched:
            await ctx.send(f"❌ `{keyword}`에 해당하는 아이템을 찾을 수 없습니다.")
            return

        if len(matched) == 1:
            name, code = matched[0]
            embed = discord.Embed(
                title=name,
                description=f"[🧭 mapleland.gg 에서 보기](https://mapleland.gg/item/{code})",
                color=discord.Color.orange()
            )
            embed.set_thumbnail(url=f"https://maplestory.io/api/gms/200/item/{code}/icon?resize=2")
            embed.set_footer(text="출처: mapleland.gg")
            view = discord.ui.View()
            view.add_item(discord.ui.Button(label="🧭 사이트로 이동", url=f"https://mapleland.gg/item/{code}"))
            await ctx.send(embed=embed, view=view)

        else:
            shown = matched[:10]  # 최대 10개까지 버튼 생성
            description = "\n".join(
                [f"**{i+1}.** {name}" for i, (name, code) in enumerate(shown)]
            )
            embed = discord.Embed(
                title=f"🔍 `{keyword}` 검색 결과 (총 {len(matched)}개)",
                description=description,
                color=discord.Color.orange()
            ).set_footer(text="클릭 시 mapleland.gg 로 이동합니다")

            view = discord.ui.View()
            for i, (name, code) in enumerate(shown):
                view.add_item(discord.ui.Button(
                    label=f"{i+1}. {name}",
                    url=f"https://mapleland.gg/item/{code}",
                    style=discord.ButtonStyle.link
                ))

            await ctx.send(embed=embed, view=view)
