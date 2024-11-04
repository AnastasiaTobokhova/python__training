def add_everything_up(a,b):
    return a + b

try:
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))
except TypeError as exp:
    print(f'Что-то пошло не так {exp}')
except SyntaxError as exp_2:
    print(f'Что-то пошло не так {exp_2}')