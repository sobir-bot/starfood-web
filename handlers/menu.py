from aiogram import Router
from aiogram.types import Message, FSInputFile

from data.products import products

from keyboards.inline_keyboard import (
    product_keyboard,
    cart_keyboard
)

from handlers.cart import get_cart_text

router = Router()


# ==========================
# ФУНКСИЯИ УМУМӢ
# ==========================

async def show_category(
    message: Message,
    category: str,
    emoji: str
):
    found = False

    for product_id, product in products.items():

        if product["category"] == category:

            found = True

            photo = FSInputFile(
                product["photo"]
            )

            await message.answer_photo(
                photo=photo,
                caption=(
                    f"{emoji} {product['name']}\n\n"
                    f"💰 Нарх: {product['price']} смн"
                ),
                reply_markup=product_keyboard(product_id)
            )

    if not found:

        await message.answer(
            "❌ Маҳсулот ёфт нашуд."
        )


# ==========================
# БУРГЕРҲО
# ==========================

@router.message(lambda m: m.text == "🍔 Бургерҳо")
async def burgers(message: Message):

    await show_category(
        message,
        "🍔 Бургерҳо",
        "🍔"
    )


# ==========================
# ПИЦЦА
# ==========================

@router.message(lambda m: m.text == "🍕 Пицца")
async def pizza(message: Message):

    await show_category(
        message,
        "🍕 Пицца",
        "🍕"
    )


# ==========================
# ТВИСТЕРҲО
# ==========================

@router.message(lambda m: m.text == "🌯 Твистерҳо")
async def twisters(message: Message):

    await show_category(
        message,
        "🌯 Твистерҳо",
        "🌯"
    )


# ==========================
# КРИЛЫШКАҲО
# ==========================

@router.message(lambda m: m.text == "🍗 Крилышкаҳо")
async def wings(message: Message):

    await show_category(
        message,
        "🍗 Крилышкаҳо",
        "🍗"
    )


# ==========================
# ХОТ ДОГҲО
# ==========================

@router.message(lambda m: m.text == "🌭 Хот-Догҳо")
async def hotdogs(message: Message):

    await show_category(
        message,
        "🌭 Хот-Догҳо",
        "🌭"
    )


# ==========================
# ГАРНИРҲО
# ==========================

@router.message(lambda m: m.text == "🍟 Гарнирҳо")
async def garnish(message: Message):

    await show_category(
        message,
        "🍟 Гарнирҳо",
        "🍟"
    )


# ==========================
# ҚАҲВА
# ==========================

@router.message(lambda m: m.text == "☕ Қаҳва")
async def coffee(message: Message):

    await show_category(
        message,
        "☕ Қаҳва",
        "☕"
    )


# ==========================
# НӮШОКИҲО
# ==========================

@router.message(lambda m: m.text == "🥤 Нӯшокиҳо")
async def drinks(message: Message):

    await show_category(
        message,
        "🥤 Нӯшокиҳо",
        "🥤"
    )


# ==========================
# СОУСҲО
# ==========================

@router.message(lambda m: m.text == "🧂 Соусҳо")
async def sauces(message: Message):

    await show_category(
        message,
        "🧂 Соусҳо",
        "🧂"
    )


# ==========================
# КОМБО
# ==========================

@router.message(lambda m: m.text == "🎁 Комбо")
async def combo(message: Message):

    await show_category(
        message,
        "🎁 Комбо",
        "🎁"
    )


# ==========================
# KIDS MENU
# ==========================

@router.message(lambda m: m.text == "🧒 Kids Menu")
async def kids_menu(message: Message):

    await show_category(
        message,
        "🧒 Kids Menu",
        "🧒"
    )


# ==========================
# ТАМОС
# ==========================

@router.message(lambda m: m.text == "📞 Тамос")
async def contacts(message: Message):

    await message.answer(
        "📞 Телефон: +992992997770\n\n"
        "📍 Спитамен"
    )


# ==========================
# САБАД
# ==========================

@router.message(lambda m: m.text == "🛒 Сабад")
async def show_cart(message: Message):

    text = get_cart_text(
        message.from_user.id
    )

    await message.answer(
        text,
        reply_markup=cart_keyboard()
    )


# ==========================
# ЗАКАЗҲОИ МАН
# ==========================

@router.message(lambda m: m.text == "📦 Заказҳои ман")
async def my_orders(message: Message):

    await message.answer(
        "📦 Таърихи заказҳо баъдтар ба SQLite пайваст мешавад."
    )