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


# Створюю таблицю зі всіма users
def create_table():
    
    connection.autocommit = True

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS users(
        id serial PRIMARY KEY,
        user_tg_id varchar(50)
        );"""
    )

    print('Table was successfully created')

#    if connection:
#        cursor.close()
#        connection.close()


# Функція перевіряє чи user зарєєстрований і якщо ні то створює йому таблицю зі словами
def create_user_table(user_id):

    connection.autocommit = True

    cursor.execute(
        f"""SELECT user_tg_id FROM users WHERE user_tg_id = '{user_id}';"""
    )
    # якщо None то user не зареєстрований, а якщо не None то нам похуй
    if cursor.fetchone() is None:

        # додаю user до бази данних
        cursor.execute(
            f"""
            INSERT INTO users (user_tg_id) VALUES({user_id});
            """
        )

        # створюю таблицю слів для user
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS user_{user_id}(
            id serial PRIMARY KEY,
            word varchar(100) NOT NULL,
            translation varchar(100) NOT NULL,
            status varchar(10) DEFAULT 'a'
            );"""
        )

    else:
        print('user exist')


def insert_words(user_id, word_list):
    print('SSSSSSSSSUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')

    connection.autocommit = True

    try:
        cursor.execute(
            f"""
            INSERT INTO user_{user_id} (word, translation) VALUES ('{word_list[0]}', '{word_list[1]}');
            """
        )

    except Exception as ex:
        print('ERROR', ex)




