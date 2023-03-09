import psycopg2
from bots_data import *


# Ця частина коду повторюється у всіх функціях тому глобальна змінна
connection = psycopg2.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DB_NAME,
        )

cursor = connection.cursor()


def create_table():
    
    connection.autocommit = True

    # Хачу глабальную пірємєнную
    global cursor

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS users(
        user_tg_id varchar(50) PRIMARY KEY
        );"""
    )

    print('Table was successfully created')

    if connection:
        cursor.close()
        connection.close()


#def create_user_table(tgid):
#
#    try:
#        connection = psycopg2.connect(
#            host=HOST,
#            user=USER,
#            password=PASSWORD,
#            database=DB_NAME,
#        )
#        connection.autocommit = True
#        cursor = connection.cursor()
#        # створюємо табличку якщо немає
#        cursor.execute(
#            f"""
#            CREATE TABLE IF NOT EXISTS user_{tgid}(
#            id serial PRIMARY KEY,
#            word varchar(100),
#            translate_word varchar(100),
#            state varchar(10)
#            );"""
#        )
#
#    except Exception as ex:
#        print(ex)
#    finally:
#        if connection:
#            cursor.close()
#            connection.close()
