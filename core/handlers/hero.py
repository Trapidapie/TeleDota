from aiogram import Bot
from aiogram.types import Message
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
        for set_name, set_info in data[hero_name].items():
            print(f"Set Name: {set_name}")
            print(f"Image: {set_info['img']}")
            print(f"Price: {set_info['price']}")
            print(f"Availability: {'Available' if set_info['availability'] else 'Not Available'}")
            print(f"Type: {set_info['type']}")
            print("-" * 30)