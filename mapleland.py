# main.py
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

from mland_db.mland_db_logic import search_mapledb_all
from mland_db.mland_db_view import ResultView, build_results_embed

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

# ✅ 봇 시작 시 메시지
@bot.event
async def on_ready():
    print(f"✅ 봇 실행됨: {bot.user}")

# ✅ 일반 메시지로 검색 처리
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    ctx = await bot.get_context(message)
    if ctx.valid:
        await bot.process_commands(message)
        return

    # 접두사 '!'로 시작하는 메시지는 검색으로 처리
    if message.content.startswith("!"):
        keyword = message.content[1:].strip()
        results = search_mapledb_all(keyword)

        if not results:
            await message.channel.send(f"🔍 `{keyword}`에 대한 정보를 찾을 수 없습니다.")
        elif len(results) == 1:
            entry = results[0]
            embed = discord.Embed(
                title=entry['name_ko'],
                description=f"[🔗 세부 정보 페이지로 이동하기]({entry['link']})",
                color=discord.Color.green()
            ).set_footer(text="출처: mapledb.kr")

            if entry['category'] == 'item':
                embed.set_thumbnail(url=f"https://maplestory.io/api/gms/62/item/{entry['code']}/icon?resize=2")
            elif entry['category'] == 'mob':
                embed.set_thumbnail(url=f"https://maplestory.io/api/gms/62/mob/{entry['code']}/render/stand")
            elif entry['category'] == 'map':
                embed.set_thumbnail(url=f"https://maplestory.io/api/gms/62/map/{entry['code']}/minimap?resize=2")

            await message.channel.send(embed=embed)
        else:
            await message.channel.send(
                embed=build_results_embed(results, 0),
                view=ResultView(user_id=message.author.id, results=results, current_page=0)
            )

# ✅ 명령어 모듈 로딩
from mland_db.mland_db import setup as setup_mland_db
setup_mland_db(bot)

from mland_gg.mland_gg import setup as setup_mland_gg
setup_mland_gg(bot)

from help.help import setup as setup_help_command
setup_help_command(bot)

# ✅ 봇 실행
bot.run(TOKEN)
