from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Додати слова')
        ],
        [
            KeyboardButton('Навчання')
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)


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


yesno = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Так'),
            KeyboardButton('Ні')
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
