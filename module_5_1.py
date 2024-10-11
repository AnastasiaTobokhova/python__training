# Пункты задачи:
#
# Создайте класс House.
# Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
# Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
# Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
# Создайте объект класса House с произвольным названием и количеством этажей.
# Вызовите метод go_to у этого объекта с произвольным числом.

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(f'Этаж {new_floor}')
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Эльбрус',30)
print(h1.name, h1.number_of_floors)

h1.go_to(2)
h1.go_to(35)