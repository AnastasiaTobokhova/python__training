import sqlite3

DB_NAME = "initiate.db"


def initiate_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER
        );
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        );
    ''')

    conn.commit()
    conn.close()


def add_user(username, email, age):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?, ?, ?, 1000);
    ''', (username, email, age))
    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user is not None


def get_all_products():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products


def populate_products():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    products = [
        (1, 'Продукт 1', 'Описание 1', 100),
        (2, 'Продукт 2', 'Описание 2', 200),
        (3, 'Продукт 3', 'Описание 3', 300),
        (4, 'Продукт 4', 'Описание 4', 400)
    ]
    cursor.executemany('INSERT OR IGNORE INTO Products VALUES (?, ?, ?, ?)', products)
    conn.commit()
    conn.close()

