from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from urllib.parse import quote
import re

def get_card_keyboard(ad: dict, webapp_base_url: str, user_id: int = 0) -> InlineKeyboardMarkup:
    clean_price = re.sub(r"[^\d]", "", str(ad.get("price", "0"))) or "0"
    params = f"?user_id={user_id}&title={quote(ad['title'])}&price={clean_price}&img={quote(ad.get('image') or '')}&url={quote(ad['url'])}"
    webapp_url = f"{webapp_base_url}{params}"

    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📊 Рассчитать маржу", 
                web_app=WebAppInfo(url=webapp_url)
            )
        ],
        [
            InlineKeyboardButton(
                text="🔗 Открыть на Kufar", 
                url=ad["url"]
            )
        ],
        [
            InlineKeyboardButton(
                text="📝 Полное описание", 
                callback_data=f"full_desc:{ad['id']}"
            )
        ]
    ])