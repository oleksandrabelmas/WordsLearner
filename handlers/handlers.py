from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from psql import *


async def start(message: types.Message, state: FSMContext):
    await message.answer(f'Hi {message.from_user.first_name}')
    create_user_table(message.from_user.id)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'], state='*')
