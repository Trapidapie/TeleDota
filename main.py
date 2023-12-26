from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
import asyncio

from core.utils.command import send_hero_link
from core.admin.settings import settings
from core.handlers.basic import start_com, main_menu
from core.utils.command import faq, helps, catalog
from core.middlewareas.libary import query_name
from core.handlers.callback import send_skin_link


# майндатпай все понятно


async def start():
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()
    dp.message.register(start_com, Command('start'))
    dp.message.register(send_hero_link, Command(*query_name))
    dp.callback_query.register(send_skin_link, F.data.startswith('skin_'))
    dp.message.register(main_menu, F.text[:-1].lower() == 'назад')
    dp.message.register(faq, F.text[:-1].lower() == 'faq')
    dp.message.register(helps, Command('help'))
    dp.message.register(catalog, F.text[:-1].lower() == 'каталог')

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())