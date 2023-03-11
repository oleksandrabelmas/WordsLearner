from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


choose_input = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Одне слово')
        ],
        [
            KeyboardButton('Група слів')
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)


add_or_cancel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Додати слова'),
            KeyboardButton('Меню')
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)


menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Додати слова')
        ],
        [
            KeyboardButton('Навчання')
        ],
        [
            KeyboardButton('Скинути мої слова')
        ],

    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

