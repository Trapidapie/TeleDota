from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

from core.middlewareas.libary import heroes_dict


# КНОПКИ И ВСЕ ЧТО С НИМИМ СВЯЗАНО

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Каталог📚'),
            KeyboardButton(text='FAQ❓'),
            KeyboardButton(text='/help'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие',
    selective=True
)

catalog_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Назад🔙'),
        ],
        []
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие',
    selective=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Назад🔙'),
        ],
    ]
)

for name_hero in heroes_dict:
    catalog_kb.keyboard.append([])
