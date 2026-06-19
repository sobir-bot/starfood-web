import asyncio

from aiogram import Bot
from aiogram import Dispatcher

from config import TOKEN

from handlers.start import router as start_router
from handlers.menu import router as menu_router
from handlers.cart import router as cart_router
from handlers.order import router as order_router
from handlers.admin import router as admin_router


async def main():

    bot = Bot(token=TOKEN)

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(cart_router)
    dp.include_router(order_router)
    dp.include_router(admin_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())