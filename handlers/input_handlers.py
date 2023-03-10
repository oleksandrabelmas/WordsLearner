from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from psql import *
from keyboards import start_kb, choose_input, yesno
from states import InputStates


# Змінна для додавання слова та переклада
input_list = []


async def start(message: types.Message):
    await message.answer(f'Hi {message.from_user.first_name}', reply_markup=start_kb)
    create_user_table(message.from_user.id)
    await InputStates.add_select.set()


async def add_words(message: types.Message, state: FSMContext):
    await message.answer('Хочете ввести одне слово чи групу слів?', reply_markup=choose_input)
    await InputStates.add_words.set()


async def add_ukrainian_word(message: types.Message, state: FSMContext):
    await message.answer('Введіть слово українською')
    await InputStates.input_ukrainian_word.set()


async def add_translation(message: types.Message, state: FSMContext):
    await message.answer('Введіть переклад')
    await InputStates.input_translation.set()

    input_list.append(message.text)


async def insert_word(message: types.Message, state: FSMContext):
    input_list.append(message.text)
    await message.answer(f'Пара слів {input_list[0]} - {input_list[1]} успішно додана')
    insert_words(message.from_user.id, input_list)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'], state='*')
    dp.register_message_handler(add_words, Text(equals='Додати слова'), state=InputStates.add_select)
    dp.register_message_handler(add_ukrainian_word, state=InputStates.add_words)
    dp.register_message_handler(add_translation, state=InputStates.input_ukrainian_word)
    dp.register_message_handler(insert_word, state=InputStates.input_translation)

