from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

contact_keyboard = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(
                text="📱 Ирсоли рақам",
                request_contact=True
            )
        ]

    ],

    resize_keyboard=True
)