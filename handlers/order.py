from aiogram import Router, F
from aiogram.types import Message
import json

from config import ADMIN_ID

from database.db import get_user

router = Router()


@router.message(F.web_app_data)
async def webapp_order(message: Message):

    try:

        data = json.loads(message.web_app_data.data)

        user = get_user(message.from_user.id)

        phone = user[3]
        latitude = user[4]
        longitude = user[5]

        text = (
            "🔥 ЗАКАЗИ НАВ\n\n"

            f"👤 {message.from_user.full_name}\n"

            f"📱 {phone}\n"

            f"📍 https://maps.google.com/?q={latitude},{longitude}\n\n"

            "🛒 Маҳсулот:\n\n"
        )

        for item in data["items"]:

            text += (
                f"🍔 {item['name']}\n"
                f"📦 {item['qty']} дона\n"
                f"💰 {item['sum']} смн\n\n"
            )

        text += f"💵 Ҳамагӣ: {data['total']} смн"


        await message.bot.send_message(
            ADMIN_ID,
            text
        )


        await message.answer(
            "✅ Заказ қабул шуд!\n\n"
            "📞 Оператори мо ба зудӣ бо шумо тамос мегирад."
        )

    except Exception as e:

        print("ORDER ERROR:", e)

        await message.answer(
            "❌ Хатогӣ ҳангоми фиристодани заказ."
        )