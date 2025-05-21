import discord
import json
import os

def mland_db_embed():
    embed = discord.Embed(
        title="메이플랜드 데이터베이스",
        description="메이플랜드 데이터베이스 사이트로 이동합니다.",
        url="https://mapledb.kr/",
        color=discord.Color.green()
    )
    embed.set_footer(text="출처: mapledb.kr")
    embed.set_thumbnail(url="https://mapledb.kr/Assets/image/favicon/apple-touch-icon.png")
    return embed

# 🔎 JSON 파일 기반 검색 함수
def search_mapledb_all(keyword):
    base_path = os.path.dirname(__file__)  # mland_db_logic.py 기준 상대 경로
    categories = {
        "mob": os.path.join(base_path, "../data/mobs.json"),
        "item": os.path.join(base_path, "../data/items.json"),
        "map": os.path.join(base_path, "../data/maps.json")
    }

    results = []

    for category, path in categories.items():
        try:
            with open(path, encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"❌ {category.upper()} 로딩 오류: {e}")
            continue

        for entry in data:
            if keyword in entry.get("name_ko", ""):
                results.append({
                    "category": category,
                    "code": entry["code"],
                    "name_ko": entry["name_ko"],
                    "link": f"https://mapledb.kr/search.php?q={entry['code']}&t={category}"
                })

    return results
