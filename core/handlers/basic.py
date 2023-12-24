from aiogram import Bot
from aiogram.types import Message

from core.keyboards.skins import main_kb

async def start_com(message: Message, bot: Bot):
    await message.answer("Привіт це для покупок есклюзивних товарів по грі дота 2, можеш ознаоймитися з моїми функціями нижче", reply_markup=main_kb)


