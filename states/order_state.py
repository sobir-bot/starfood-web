from aiogram.fsm.state import State
from aiogram.fsm.state import StatesGroup


class OrderState(StatesGroup):

    # Ном ва насаб
    waiting_name = State()

    # Телефон
    waiting_phone = State()

    # Локация
    waiting_location = State()

    # Тасдиқи заказ
    waiting_confirmation = State()