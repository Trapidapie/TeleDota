from aiogram import Bot, Dispatcher, F
from aiogram.types import ContentType, Message
from aiogram.filters import Command
import asyncio
import logging

from core.middlewareas.settings import settings
from core.handlers.basic import get_start, get_photo, get_hello

async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, 'Hello, world!')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Bye, world!')

async def start():
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text == "start")
    dp.message.register(get_start, Command('start'))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())