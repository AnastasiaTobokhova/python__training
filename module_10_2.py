# Задача "За честь и отвагу!":
#
# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
# Атрибут name - имя рыцаря. (str)
# Атрибут power - сила рыцаря. (int)
# А также метод run, в котором рыцарь будет сражаться с врагами:
# При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
# Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
# В процессе сражения количество врагов уменьшается на power текущего рыцаря.
# По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
# После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
# Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.
# Пункты задачи:
#
# Создайте класс Knight с соответствующими описанию свойствами.
# Создайте и запустите 2 потока на основе класса Knight.
# Выведите на экран строку об окончании битв.

import threading
import time

# Общее количество врагов
total_enemies = 100
# Блокировка для синхронизации доступа к общему ресурсу
enemies_lock = threading.Lock()


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        global total_enemies
        print(f"{self.name}, на нас напали!")

        while total_enemies > 0:
            # Задержка на 1 секунду
            time.sleep(1)

            # Защита критической секции с общими данными
            with enemies_lock:
                if total_enemies > 0:
                    total_enemies -= self.power
                    self.days += 1
                    if total_enemies < 0:
                        total_enemies = 0
                    print(f"{self.name}, сражается {self.days} день(дня)..., осталось {total_enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} день(дня)!")


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения обоих потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражений
print("Все битвы закончились!")