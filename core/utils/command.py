from aiogram import Bot, F, types
from aiogram.types import BotCommand, BotCommandScopeDefault,  InlineKeyboardButton, InlineKeyboardMarkup, Message
from core.keyboards.key import back

from core.middlewareas.libary import heroes_dict


# команды для бота


def find_key_by_value(dictionary, search_value):
    for key, values in dictionary.items():
        if search_value[1:] in values:
            return key
    return '404'


async def send_hero_link(message: Message, bot: Bot):
    hero = find_key_by_value(heroes_dict, message.text)
    await message.answer(hero)

async def send_hero_skin(hero, skin_name, message: Message, bot: Bot):
    await message.answer(hero)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Начать работу с ботом'),
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='faq', description='FAQ'),
        BotCommand(command='catalog', description='Каталог'),
        BotCommand(command='db', description='Каталог'),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())

async def faq(message: Message, bot: Bot):
    await message.answer("Типо вопросы я хз", reply_markup=back)

async def helps(message: Message, bot: Bot):
    await message.answer("Типо помощь я хз", reply_markup=back)

async def catalog(message: Message, bot: Bot):
    await message.answer("Типо каталог я хз", reply_markup=back)

