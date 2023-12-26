from aiogram import Bot
from aiogram.types import Message

from core.keyboards.key import main_kb
from core.utils.command import set_commands

async def start_com(message: Message, bot: Bot):
    await set_commands(bot)
    await message.answer("Привіт це для покупок есклюзивних товарів по грі дота 2,"
                         " можеш ознаоймитися з моїми функціями нижче НЕ РАБОТАЕТ СЕЙЧАС ТЕСТ", reply_markup=main_kb)

async def main_menu(message: Message, bot: Bot):
    await message.answer("Головне меню", reply_markup=main_kb)

