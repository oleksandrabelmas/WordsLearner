from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text


async def start(message: types.Message, state: FSMContext):
    await message.answer(f'Hi {message.from_user.first_name}')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'], state='*')
