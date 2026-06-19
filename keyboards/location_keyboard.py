from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

location_keyboard = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(
                text="📍 Ирсоли локация",
                request_location=True
            )
        ]

    ],

    resize_keyboard=True
)