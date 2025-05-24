# main.py
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging

from mland_db.mland_db_logic import search_mapledb_all
from mland_db.mland_db_view import ResultView, build_results_embed, build_entry_embed

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("bot.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 환경 변수 로딩 및 토큰 체크
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if TOKEN is None:
    raise EnvironmentError("❌ DISCORD_BOT_TOKEN 환경 변수가 설정되지 않았습니다.")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

# ✅ 봇 시작 시 메시지
@bot.event
async def on_ready():
    logger.info(f"✅ 봇 실행됨: {bot.user}")

# ✅ 일반 메시지로 검색 처리
# ✅ 일반 메시지로 검색 처리
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    try:
        ctx = await bot.get_context(message)
        if ctx.valid:
            await bot.process_commands(message)
            return

        # 접두사 '!'로 시작하는 메시지는 검색으로 처리
        if message.content.startswith("!"):
            keyword = message.content[1:].strip()
            results = search_mapledb_all(keyword)  # ✅ 정렬도 중복 제거도 하지 않음

            if not results:
                await message.channel.send(f"🔍 `{keyword}`에 대한 정보를 찾을 수 없습니다.")
            elif len(results) == 1:
                await message.channel.send(embed=build_entry_embed(results[0]))
            else:
                await message.channel.send(
                    embed=build_results_embed(results, 0),
                    view=ResultView(user_id=message.author.id, results=results, current_page=0)
                )
    except Exception as e:
        logger.exception("❌ on_message 처리 중 예외 발생")
        await message.channel.send("⚠️ 요청을 처리하는 도중 오류가 발생했습니다.")

# ✅ 명령어 모듈 로딩
from mland_db.mland_db import setup as setup_mland_db
setup_mland_db(bot)

from mland_gg.mland_gg import setup as setup_mland_gg
setup_mland_gg(bot)

from help.help import setup as setup_help_command
setup_help_command(bot)

# ✅ 봇 실행
bot.run(TOKEN)
