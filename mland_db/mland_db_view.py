# mland_db_view.py
import discord

MAPLE_IO_BASE_URL = "https://maplestory.io/api/gms/62"
RESULTS_PER_PAGE = 10

# ✅ 단일 검색 결과 Embed 생성 함수
def build_entry_embed(entry):
    embed = discord.Embed(
        title=entry['name_ko'],
        description=f"[🔗 세부 정보 페이지로 이동하기]({entry['link']})",
        color=discord.Color.green()
    ).set_footer(text="출처: mapledb.kr")

    code = entry['code']
    category = entry['category']

    if category == 'item':
        embed.set_thumbnail(url=f"{MAPLE_IO_BASE_URL}/item/{code}/icon?resize=2")
    elif category == 'mob':
        embed.set_thumbnail(url=f"{MAPLE_IO_BASE_URL}/mob/{code}/render/stand")
    elif category == 'map':
        embed.set_thumbnail(url=f"{MAPLE_IO_BASE_URL}/map/{code}/minimap?resize=2")

    return embed

# ✅ 검색 결과 목록 Embed 생성 함수
def build_results_embed(results, current_page):
    page_results = results[current_page * RESULTS_PER_PAGE:(current_page + 1) * RESULTS_PER_PAGE]
    desc = "\n".join([f"**{i+1}.** {e['name_ko']} ({e['category']})" for i, e in enumerate(page_results)])
    return discord.Embed(
        title=f"🔍 검색 결과 (총 {len(results)}개 중 {current_page+1}페이지):",
        description=desc,
        color=discord.Color.blurple()
    ).set_footer(text="(버튼을 눌러 선택하세요)")

# ✅ 페이지 뷰 클래스
class ResultView(discord.ui.View):
    def __init__(self, user_id, results, current_page):
        super().__init__(timeout=None)
        self.user_id = user_id
        self.results = results
        self.current_page = current_page
        self.total_pages = (len(results) - 1) // RESULTS_PER_PAGE + 1
        self.refresh_buttons()

    def refresh_buttons(self):
        self.clear_items()
        page_results = self.results[self.current_page * RESULTS_PER_PAGE:(self.current_page + 1) * RESULTS_PER_PAGE]
        for i, entry in enumerate(page_results):
            self.add_item(ResultButton(label=str(i+1), entry=entry, user_id=self.user_id))

        if self.total_pages > 1:
            self.add_item(PageNavButton(label="◀", direction=-1, view=self))
            self.add_item(PageNavButton(label="▶", direction=1, view=self))

    async def update_message(self, interaction):
        embed = build_results_embed(self.results, self.current_page)
        self.refresh_buttons()
        await interaction.response.edit_message(embed=embed, view=self)

# ✅ 결과 선택 버튼
class ResultButton(discord.ui.Button):
    def __init__(self, label, entry, user_id):
        super().__init__(label=label, style=discord.ButtonStyle.primary)
        self.entry = entry
        self.user_id = user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("❌ 이 버튼은 해당 사용자만 사용할 수 있습니다.", ephemeral=True)
            return

        await interaction.response.edit_message(embed=build_entry_embed(self.entry), view=None)

# ✅ 페이지 이동 버튼
class PageNavButton(discord.ui.Button):
    def __init__(self, label, direction, view):
        super().__init__(label=label, style=discord.ButtonStyle.secondary)
        self.direction = direction
        self.view_obj = view

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.view_obj.user_id:
            await interaction.response.send_message("❌ 이 버튼은 해당 사용자만 사용할 수 있습니다.", ephemeral=True)
            return

        self.view_obj.current_page = (self.view_obj.current_page + self.direction) % self.view_obj.total_pages
        await self.view_obj.update_message(interaction)
