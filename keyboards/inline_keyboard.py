from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


# ==========================
# ТУГМАҲОИ МАҲСУЛОТ
# ==========================

def product_keyboard(product_id):

    builder = InlineKeyboardBuilder()

    builder.row(

        InlineKeyboardButton(
            text="➖",
            callback_data=f"minus:{product_id}"
        ),

        InlineKeyboardButton(
            text="➕",
            callback_data=f"plus:{product_id}"
        )

    )

    builder.row(

        InlineKeyboardButton(
            text="🛒 Ба сабад",
            callback_data=f"add:{product_id}"
        )

    )

    return builder.as_markup()


# ==========================
# САБАД
# ==========================

def cart_keyboard():

    builder = InlineKeyboardBuilder()

    builder.row(

        InlineKeyboardButton(
            text="✅ Оформить заказ",
            callback_data="checkout"
        )

    )

    builder.row(

        InlineKeyboardButton(
            text="🗑 Тоза кардани сабад",
            callback_data="clear_cart"
        )

    )

    return builder.as_markup()


# ==========================
# ИДОРАКУНИИ МИҚДОР
# ==========================

def quantity_keyboard(product_id):

    builder = InlineKeyboardBuilder()

    builder.row(

        InlineKeyboardButton(
            text="➖",
            callback_data=f"minus:{product_id}"
        ),

        InlineKeyboardButton(
            text="➕",
            callback_data=f"plus:{product_id}"
        )

    )

    builder.row(

        InlineKeyboardButton(
            text="🛒 Ба сабад",
            callback_data=f"add:{product_id}"
        )

    )

    return builder.as_markup()


# ==========================
# АДМИН
# ==========================

def admin_order_keyboard(order_id):

    builder = InlineKeyboardBuilder()

    builder.row(

        InlineKeyboardButton(
            text="⏳ Қабул шуд",
            callback_data=f"pending:{order_id}"
        )

    )

    builder.row(

        InlineKeyboardButton(
            text="🍳 Тайёр мешавад",
            callback_data=f"cooking:{order_id}"
        )

    )

    builder.row(

        InlineKeyboardButton(
            text="🚚 Дар роҳ",
            callback_data=f"delivery:{order_id}"
        )

    )

    builder.row(

        InlineKeyboardButton(
            text="✅ Расонида шуд",
            callback_data=f"done:{order_id}"
        )

    )

    return builder.as_markup()