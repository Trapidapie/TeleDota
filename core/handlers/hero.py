from aiogram import Bot, types
from aiogram.types import Message, FSInputFile, InputFile,  InlineKeyboardButton, InlineKeyboardMarkup
from core.middlewareas.libary import dota2_heroes_dict
import json

with open('lib.json', 'r') as file:
    data = json.load(file)


def find_key_by_value(dictionary, search_value):
    for key, values in dictionary.items():
        if search_value[1:] in values:
            return key
    return '404'

async def send_hero_link(message: Message, bot: Bot):
    hero_name = message.text.split()[0]
    hero_name = find_key_by_value(dota2_heroes_dict, hero_name)
    if hero_name == '404':
        await message.answer('Герой не найден')
    else:
        await message.answer('Герой найден')
