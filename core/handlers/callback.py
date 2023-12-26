from aiogram import Bot
from aiogram.types import CallbackQuery

# КАЛБЭК ТОЛЬКО

async def send_skin_link(call: CallbackQuery, bot: Bot):
    answer = "I LOVE YOU"
    await call.message.answer(answer)