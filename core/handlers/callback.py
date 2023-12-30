from aiogram import Bot
from aiogram.types import CallbackQuery
from core.handlers.pay import order, pre_checkout_q, successful_payment
# КАЛБЭК ТОЛЬКО

async def send_skin_link(call: CallbackQuery, bot: Bot):
    print(call.data.split('_'))
    await order(call.message, bot, call.data.split('_')[1], call.data.split('_')[2], int(call.data.split('_')[3]))