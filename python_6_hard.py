import math

# Родительский класс Figure
class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = False
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count

    # Проверка на валидность цвета
    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in [r, g, b])

    # Установка цвета с проверкой
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    # Получение цвета
    def get_color(self):
        return self.__color

    # Проверка на валидность сторон
    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    # Установка новых сторон с проверкой
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    # Получение сторон
    def get_sides(self):
        return self.__sides

    # Периметр (или длина для круга)
    def __len__(self):
        return sum(self.__sides)


# Класс Circle
class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color, circumference)
        self.__radius = circumference / (2 * math.pi)

    # Площадь круга
    def get_square(self):
        return math.pi * self.__radius ** 2


# Класс Triangle
class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)


    def get_square(self):
        s = len(self) / 2  # Полупериметр
        a, b, c = self.get_sides()
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


# Класс Cube
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, *(side,) * self.sides_count)

    # Объём куба
    def get_volume(self):
        side = self.get_sides()[0]  # Все стороны одинаковые
        return side ** 3


# Тестирование

# Круг с длиной окружности 10
circle1 = Circle((200, 200, 100), 10)

# Куб с ребром длиной 6
cube1 = Cube((222, 35, 130), 6)

# Изменение цветов
circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Изменение сторон
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())

# Периметр (или длина окружности для круга)
print(len(circle1))

# Объём куба
print(cube1.get_volume())
