from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🍔 Меню",
                web_app=WebAppInfo(
                    url="https://starfood-web.vercel.app"
                )
            )
        ],
        [
            KeyboardButton(text="📞 Тамос")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Менюро кушоед 🍔"
)