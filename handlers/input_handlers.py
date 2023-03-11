from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, CommandStart

from psql import *
from keyboards import choose_input, add_or_cancel, menu_kb
from states import InputStates


# Змінна для додавання слова та переклада
input_list = []


async def menu(message: types.Message):
    await message.answer(f'{message.from_user.first_name} оберіть варіант відповіді', reply_markup=menu_kb)
    create_user_table(message.from_user.id)
    await InputStates.add_select.set()


async def add_words(message: types.Message, state: FSMContext):
    await message.answer('Хочете ввести одне слово чи групу слів?', reply_markup=choose_input)
    await InputStates.add_words.set()


# Вводить слово українською
async def add_ukrainian_word(message: types.Message, state: FSMContext):
    await message.answer('Введіть слово українською')
    await InputStates.input_ukrainian_word.set()


# Вводить переклад
async def add_translation(message: types.Message, state: FSMContext):
    global input_list

    await message.answer('Введіть переклад')
    await InputStates.input_translation.set()
    # Додаю слова в глобальну змінну
    input_list.append(message.text)


# Додаю слова до бази данних
async def insert_word(message: types.Message, state: FSMContext):
    global input_list
    # Додаю слова в глобальну змінну
    input_list.append(message.text)

    await message.answer(f'Пара слів {input_list[0]} - {input_list[1]} успішно додана', reply_markup=add_or_cancel)
    # Додаю слова в базу данних
    insert_words(message.from_user.id, input_list)

    await state.set_state(None)
    # Очищую глобальну змінну
    input_list = []


def register_input_handlers(dp: Dispatcher):
    dp.register_message_handler(menu, CommandStart() | Text(equals='Меню'), state='*')
    dp.register_message_handler(add_words, Text(equals='Додати слова'), state='*')
    dp.register_message_handler(add_ukrainian_word, state=InputStates.add_words)
    dp.register_message_handler(add_translation, state=InputStates.input_ukrainian_word)
    dp.register_message_handler(insert_word, state=InputStates.input_translation)

