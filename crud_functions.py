import sqlite3


def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Продукт{i}', f'Описание{i}', f'{i * 100}'))
        connection.commit()  # сохраняем состояние
    connection.close()  # закрываем соединение
    print('Таблица Products создана')

    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email  TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')

    print('Таблица Users создана')
    connection.commit()  # сохраняем состояние
    connection.close()


# которая возвращает все записи из таблицы Products
def get_all_product():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")

    return cursor.fetchall()


def add_user(username, email, age):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    # проверка на существование пользователя
    check_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))

    if check_user.fetchone() is None:
        cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                       (username, email, age, 1000))
        connection.commit()


def is_included(username):  # проверка на существование пользователя
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    check_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    if check_user.fetchone() is None:
        return False
    else:
        return True
