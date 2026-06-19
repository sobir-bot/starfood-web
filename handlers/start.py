from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.contact_keyboard import contact_keyboard
from keyboards.location_keyboard import location_keyboard
from keyboards.main_keyboard import main_menu

from database.db import (
    add_user,
    save_phone,
    save_location
)

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    add_user(
        telegram_id=message.from_user.id,
        full_name=message.from_user.full_name
    )

    await message.answer(
        "🍔 Ба StarFood хуш омадед!\n\n"
        "📱 Рақами худро ирсол кунед.",
        reply_markup=contact_keyboard
    )


@router.message(F.contact)
async def get_contact(message: Message):

    save_phone(
        telegram_id=message.from_user.id,
        phone=message.contact.phone_number
    )

    await message.answer(
        "✅ Рақам қабул шуд.\n\n"
        "📍 Акнун локацияи худро фиристед.",
        reply_markup=location_keyboard
    )


@router.message(F.location)
async def get_location(message: Message):

    save_location(
        telegram_id=message.from_user.id,
        latitude=message.location.latitude,
        longitude=message.location.longitude
    )

    await message.answer(
        "✅ Локация қабул шуд.\n\n"
        "🍔 Барои фармоиш менюро кушоед.",
        reply_markup=main_menu
    )