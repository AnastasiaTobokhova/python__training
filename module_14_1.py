# Задача "Первые пользователи":
#
# Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3.
# Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
# Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:
# id - целое число, первичный ключ
# username - текст (не пустой)
# email - текст (не пустой)
# age - целое число
# balance - целое число (не пустой)
# Заполните её 10 записями:
# User1, example1@gmail.com, 10, 1000
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 1000
# ...
# User10, example10@gmail.com, 100, 1000
# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
# User1, example1@gmail.com, 10, 500
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 500
# ...
# User10, example10@gmail.com, 100, 1000
# Удалите каждую 3ую запись в таблице начиная с 1ой:
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 500
# User5, example5@gmail.com, 50, 500
# ...
# User9, example9@gmail.com, 90, 500
#
# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>

import sqlite3

# Создаем файл базы данных и подключаемся к ней
conn = sqlite3.connect("not_telegram.db")
cursor = conn.cursor()

# Создаем таблицу Users, если она еще не создана
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
""")

# Заполняем таблицу 10 записями
for i in range(1, 11):
    username = f"User{i}"
    email = f"example{i}@gmail.com"
    age = i * 10
    balance = 1000
    cursor.execute("INSERT OR REPLACE INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (username, email, age, balance))

# Обновляем balance у каждой 2-й записи начиная с 1-й
cursor.execute("""
UPDATE Users SET balance = 500 WHERE id % 2 = 1
""")

# Удаляем каждую 3-ю запись начиная с 1-й
cursor.execute("""
DELETE FROM Users WHERE id % 3 = 0
""")

# Выбираем все записи, где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
results = cursor.fetchall()


for row in results:
    print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")


conn.commit()
conn.close()
