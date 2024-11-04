def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError:
        return str(a) + str(b)
    else:
        return result

print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))     # Вывод: яблоко4215
print(add_everything_up(123.456, 7))         # Вывод: 130.456
