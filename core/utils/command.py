from aiogram import Bot, F, types
from aiogram.types import BotCommand, BotCommandScopeDefault, InlineKeyboardButton, InlineKeyboardMarkup, Message, FSInputFile
from core.keyboards.key import back

from core.middlewareas.libary import heroes_dict
from core.middlewareas.libary import skins

from core.filters.classes import Skin
# команды для бота


def find_key_by_value(dictionary, search_value):
    for key, values in dictionary.items():
        if search_value[1:] in values:
            return key
    return '404'


async def send_hero_link(message: Message, bot: Bot):
    hero = find_key_by_value(heroes_dict, message.text)
    for skin in skins[hero]:
        inline_kb_full = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text="Купить", callback_data=f"skin_{hero}_{skin}_{skins[hero][skin]['price']}"),
        ]])
        item = Skin(hero, f'img/hero/sets/{hero}/{skin.lower().replace(' ', '_')}_icon.png', skins[hero][skin]["price"],
                    skins[hero][skin]["rarity"], skins[hero][skin]["availability"], skins[hero][skin]["type"])

        photo = FSInputFile(f"./img/hero/sets/{hero}/{skin.lower().replace(' ', '_')}_icon.png")
        await bot.send_photo(message.chat.id, photo,
                             caption=f"Цена: {item.price}\nРедкость:"
                             f"{item.rarity}\n Доступность: {item.availability}\n"
                             f"Тип: {item.skin_type}", reply_markup=inline_kb_full)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Начать работу с ботом'),
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='faq', description='FAQ'),
        BotCommand(command='catalog', description='Каталог'),
        BotCommand(command='db', description='Каталог'),
        BotCommand(command='pay', description='Купить скин'),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())


async def faq(message: Message, bot: Bot):
    await message.answer("Типо вопросы я хз", reply_markup=back)


async def helps(message: Message, bot: Bot):
    await message.answer("Типо помощь я хз", reply_markup=back)


async def catalog(message: Message, bot: Bot):
    await message.answer("Типо каталог я хз", reply_markup=back)
