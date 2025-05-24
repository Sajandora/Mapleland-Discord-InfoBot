import discord
import json
import os

# 🔄 전역 캐시 저장소
_cached_data = {}

# ✅ DB 초기 로딩 및 캐싱
def load_mapledb_data():
    global _cached_data
    if _cached_data:
        return _cached_data  # 이미 로드된 경우 캐시 반환

    base_path = os.path.dirname(__file__)
    categories = {
        "mob": os.path.join(base_path, "../data/mobs.json"),
        "item": os.path.join(base_path, "../data/items.json"),
        "map": os.path.join(base_path, "../data/maps.json")
    }

    for category, path in categories.items():
        try:
            with open(path, encoding='utf-8') as f:
                _cached_data[category] = json.load(f)
        except Exception as e:
            print(f"❌ {category.upper()} 로딩 오류: {e}")
            _cached_data[category] = []

    return _cached_data

# ✅ 임베드 생성 함수
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

# 🔎 검색 함수 (개선됨)
def search_mapledb_all(keyword):
    keyword = keyword.lower()
    data = load_mapledb_data()
    seen = set()
    results = []

    for category, entries in data.items():
        for entry in entries:
            name_ko = entry.get("name_ko", "")
            if keyword in name_ko.lower():
                unique_key = (name_ko, entry["code"], category)
                if unique_key in seen:
                    continue
                seen.add(unique_key)
                results.append({
                    "category": category,
                    "code": entry["code"],
                    "name_ko": name_ko,
                    "link": f"https://mapledb.kr/search.php?q={entry['code']}&t={category}"
                })

    # 🔽 이름 길이 순 정렬 (짧은 이름 우선)
    results.sort(key=lambda x: len(x["name_ko"]))

    return results
