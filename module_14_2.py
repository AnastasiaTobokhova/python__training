# Задача "Средний баланс пользователя":
#
# Для решения этой задачи вам понадобится решение предыдущей.
# Для решения необходимо дополнить существующий код:
# Удалите из базы данных not_telegram.db запись с id = 6.
# Подсчитать общее количество записей.
# Посчитать сумму всех балансов.
# Вывести в консоль средний баланс всех пользователей.

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

# Заполняем таблицу 10 записями циклом for
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

# Выводим результаты в заданном формате
for row in results:
    print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")

# Удаляем запись с id = 6
cursor.execute("DELETE FROM Users WHERE id = 6")

# Подсчитываем общее количество записей
cursor.execute("SELECT COUNT(*) FROM Users")
count = cursor.fetchone()[0]
print(f"Общее количество записей: {count}")

# Суммируем все балансы
cursor.execute("SELECT SUM(balance) FROM Users")
sum_balance = cursor.fetchone()[0]
print(f"Сумма всех балансов: {sum_balance}")

# Вычисляем средний баланс
average_balance = sum_balance / count if count > 0 else 0
print(f"Средний баланс: {average_balance:.2f}")

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
