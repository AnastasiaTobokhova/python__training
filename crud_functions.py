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
    conn.commit()
    conn.close()

def populate_products():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    products = [
        (1, 'Продукт 1', 'Описание 1', 100),
        (2, 'Продукт 2', 'Описание 2', 200),
        (3, 'Продукт 3', 'Описание 3', 300),
        (4, 'Продукт 4', 'Описание 4', 400)
    ]
    # Проверяем, есть ли уже данные в таблице
    cursor.execute('SELECT COUNT(*) FROM Products')
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.executemany('INSERT INTO Products VALUES (?, ?, ?, ?)', products)
        conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products
