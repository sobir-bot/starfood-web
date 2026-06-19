from aiogram import Router
from aiogram.types import CallbackQuery

from data.products import products

router = Router()

# ==========================
# САБАД
# ==========================

cart = {}

# ==========================
# ИЛОВА БА САБАД
# ==========================

@router.callback_query(
    lambda c: c.data.startswith("add:")
)
async def add_to_cart(
    callback: CallbackQuery
):

    product_id = callback.data.split(":")[1]

    user_id = callback.from_user.id

    if user_id not in cart:
        cart[user_id] = {}

    if product_id not in cart[user_id]:

        cart[user_id][product_id] = 1

    else:

        cart[user_id][product_id] += 1

    await callback.answer(
        "✅ Ба сабад илова шуд"
    )


# ==========================
# ПЛЮС
# ==========================

@router.callback_query(
    lambda c: c.data.startswith("plus:")
)
async def plus_item(
    callback: CallbackQuery
):

    product_id = callback.data.split(":")[1]

    user_id = callback.from_user.id

    if user_id not in cart:
        cart[user_id] = {}

    if product_id not in cart[user_id]:
        cart[user_id][product_id] = 1
    else:
        cart[user_id][product_id] += 1

    await callback.answer("➕")


# ==========================
# МИНУС
# ==========================

@router.callback_query(
    lambda c: c.data.startswith("minus:")
)
async def minus_item(
    callback: CallbackQuery
):

    product_id = callback.data.split(":")[1]

    user_id = callback.from_user.id

    if (
        user_id in cart and
        product_id in cart[user_id]
    ):

        cart[user_id][product_id] -= 1

        if cart[user_id][product_id] <= 0:

            del cart[user_id][product_id]

    await callback.answer("➖")


# ==========================
# ТОЗА КАРДАНИ САБАД
# ==========================

@router.callback_query(
    lambda c: c.data == "clear_cart"
)
async def clear_cart(
    callback: CallbackQuery
):

    user_id = callback.from_user.id

    cart[user_id] = {}

    await callback.message.answer(
        "🗑 Сабад тоза карда шуд"
    )

    await callback.answer()


# ==========================
# НИШОН ДОДАНИ САБАД
# ==========================

def get_cart_text(user_id):

    if (
        user_id not in cart or
        not cart[user_id]
    ):

        return "🛒 Сабад холӣ аст"

    text = "🛒 Сабади шумо\n\n"

    total = 0

    for product_id, qty in cart[user_id].items():

        product = products[product_id]

        subtotal = product["price"] * qty

        total += subtotal

        text += (
            f"🍔 {product['name']}\n"
            f"💰 {product['price']} × {qty}\n"
            f"📦 Ҳамагӣ: {subtotal} смн\n\n"
        )

    text += (
        f"💵 Ҳамагӣ барои пардохт: "
        f"{total} смн"
    )

    return text


# ==========================
# СУММА
# ==========================

def get_total_price(user_id):

    total = 0

    if user_id not in cart:
        return 0

    for product_id, qty in cart[user_id].items():

        total += (
            products[product_id]["price"]
            * qty
        )

    return total