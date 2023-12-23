from aiogram import Bot
from aiogram.types import Message

api = 'https://docs.stratz.com/swagger/v1/swagger.json'


async def start_com(message: Message, bot: Bot):
    await message.answer('Уебище я твою мать!')


