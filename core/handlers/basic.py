from aiogram import Bot
from aiogram.types import Message

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Hello, world!')

async def get_photo(message: Message, bot: Bot):
    await message.answer('Hello, world!')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')

async def get_hello(message: Message, bot: Bot):
    await message.answer('Уебище я твою мать!')
