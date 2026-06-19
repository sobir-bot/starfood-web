from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from config import (
    ADMIN_ID,
    ORDER_PENDING,
    ORDER_COOKING,
    ORDER_DELIVERY,
    ORDER_DONE
)

from database.db import (
    get_orders,
    update_order_status,
    get_total_orders,
    get_total_users,
    get_total_sales
)

from keyboards.inline_keyboard import (
    admin_order_keyboard
)

router = Router()


# ==========================
# ҲАМАИ ЗАКАЗҲО
# ==========================

@router.message(Command("orders"))
async def orders(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    orders_list = get_orders()

    if not orders_list:

        await message.answer(
            "📦 Заказ вуҷуд надорад"
        )

        return

    for order in orders_list:

        order_id = order[0]
        user_id = order[1]
        total_price = order[2]
        status = order[3]
        latitude = order[4]
        longitude = order[5]
        created_at = order[6]

        text = (
            f"📦 Заказ №{order_id}\n\n"
            f"👤 User ID: {user_id}\n"
            f"💰 Сумма: {total_price} смн\n"
            f"📌 Статус: {status}\n"
            f"📅 Сана: {created_at}\n\n"
            f"📍 https://maps.google.com/?q={latitude},{longitude}"
        )

        await message.answer(
            text,
            reply_markup=admin_order_keyboard(order_id)
        )


# ==========================
# ОМОР
# ==========================

@router.message(Command("stats"))
async def stats(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    total_orders = get_total_orders()
    total_users = get_total_users()
    total_sales = get_total_sales()

    await message.answer(

        f"📊 StarFood Statistics\n\n"

        f"👥 Ҳамагӣ мизоҷон: {total_users}\n"
        f"📦 Ҳамагӣ заказҳо: {total_orders}\n"
        f"💰 Ҳамагӣ фурӯш: {total_sales} смн"
    )


# ==========================
# ҚАБУЛ ШУД
# ==========================

@router.callback_query(
    lambda c: c.data.startswith("pending:")
)
async def pending(
    callback: CallbackQuery
):

    order_id = int(
        callback.data.split(":")[1]
    )

    update_order_status(
        order_id,
        ORDER_PENDING
    )

    await callback.answer(
        "⏳ Заказ қабул шуд"
    )


# ==========================
# ТАЙЁР МЕШАВАД
# ==========================

@router.callback_query(
    lambda c: c.data.startswith("cooking:")
)
async def cooking(
    callback: CallbackQuery
):

    order_id = int(
        callback.data.split(":")[1]
    )

    update_order_status(
        order_id,
        ORDER_COOKING
    )

    await callback.answer(
        "🍳 Заказ тайёр мешавад"
    )


# ==========================
# ДАР РОҲ
# ==========================

@router.callback_query(
    lambda c: c.data.startswith("delivery:")
)
async def delivery(
    callback: CallbackQuery
):

    order_id = int(
        callback.data.split(":")[1]
    )

    update_order_status(
        order_id,
        ORDER_DELIVERY
    )

    await callback.answer(
        "🚚 Курьер дар роҳ аст"
    )


# ==========================
# РАСОНИДА ШУД
# ==========================

@router.callback_query(
    lambda c: c.data.startswith("done:")
)
async def done(
    callback: CallbackQuery
):

    order_id = int(
        callback.data.split(":")[1]
    )

    update_order_status(
        order_id,
        ORDER_DONE
    )

    await callback.answer(
        "✅ Заказ расонида шуд"
    )