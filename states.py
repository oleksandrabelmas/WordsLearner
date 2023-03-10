from aiogram.dispatcher.filters.state import State, StatesGroup


class InputStates(StatesGroup):
    add_select = State()
    add_words = State()

    input_one_word = State()
    input_groups_words = State()

    input_ukrainian_word = State()
    input_translation = State()


