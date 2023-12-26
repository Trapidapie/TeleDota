from aiogram import Bot, types
from aiogram.types import Message, FSInputFile, InputFile,  InlineKeyboardButton, InlineKeyboardMarkup
from core.middlewareas.libary import dota2_heroes_dict
import json

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


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
        catalog_kb = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='Назад🔙'),
                ],
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
            input_field_placeholder='Выберите действие',
            selective=True
        )
        j = 2
        for i in data[hero_name]:
            try:
                catalog_kb.keyboard[j//2].append(KeyboardButton(text=i, callback_data=f'{hero_name}_{i}'
                                                                .replace(" ", "_")))
            except IndexError:
                catalog_kb.keyboard.append([])
                catalog_kb.keyboard[j//2].append(KeyboardButton(text=i, callback_data=f'{hero_name}_{i}'
                                                                .replace(" ", "_")))
            j += 1
        await message.answer(f'Герой {hero_name}', reply_markup=catalog_kb)

async def send_hero_skin(hero, skin_name, message: Message, bot: Bot):
    await message.answer(hero)