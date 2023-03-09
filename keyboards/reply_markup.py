from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Розпочати нагадування')
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
