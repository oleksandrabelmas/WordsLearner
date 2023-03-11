from aiogram import executor

from bot import dp
import handlers
from psql import create_table


try:
    create_table()

except Exception as ex:
    print(ex)


handlers.register_input_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
