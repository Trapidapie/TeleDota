from aiogram import Bot, F, types
from aiogram.types import BotCommand, BotCommandScopeDefault, Message
from core.keyboards.key import back
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Начать работу с ботом'),
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='faq', description='FAQ'),
        BotCommand(command='catalog', description='Каталог'),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())

async def faq(message: Message, bot: Bot):
    await message.answer("Типо вопросы я хз", reply_markup=back)

async def helps(message: Message, bot: Bot):
    await message.answer("Типо помощь я хз", reply_markup=back)

async def catalog(message: Message, bot: Bot):
    await message.answer("Типо каталог я хз", reply_markup=back)

