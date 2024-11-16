# 1 написать функцию которая возвращает функцию повторения двух первых символов
# 2 создать массив функций и применить все функции поочередно к аргументу
# 3 применить все функции поочередно к массиву аргументов

animal = 'мишка'
animals = ['зайка', 'мишка', 'бегемотик']

# 1
def gen_repeat(n):
    def repeat(animal):
        return(animal[:2] + '-') * n + animal
    return repeat

test_1 = gen_repeat(1)
test_2 = gen_repeat(2)

print(test_1(animal))
# вывод ми-мишка
print(test_2(animal))
# вывод ми-ми-мишка

# 2
repetitions = [gen_repeat(n) for n in range(1,4)]
print(repetitions)

result = [func(animal) for func in repetitions]
print(result)
# ['ми-мишка', 'ми-ми-мишка', 'ми-ми-ми-мишка']

# 3
fin_result = [func(x) for func in repetitions for x in animals]
print(fin_result)
# ['за-зайка', 'ми-мишка', 'бе-бегемотик',
# 'за-за-зайка', 'ми-ми-мишка', 'бе-бе-бегемотик',
# 'за-за-за-зайка', 'ми-ми-ми-мишка', 'бе-бе-бе-бегемотик']

# Задача(декораторы)- есть функция, которая возвращает результат введения числа а в степень b
# Нужно ускорить ее чтобы она не делала повторение вычисления

# декоратор созданный для ускорения
def memoize_func(f):
    mem = {}
    def wrapper(*args):
        print(f'Выполнение функции с аргументами = {args}, внутренняя память = {mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f'Функция выполнилась, ответ = {mem[args]}'
        else:
            return f'Функция уже была выполнена раньше, ответ = {mem[args]}'
    return wrapper

# функция из условия задачи
@memoize_func
def function(a, b):
    print(f'Выполняем функцию с аргументами ({a}, {b})')
    return a ** b


print(function(3,5), '\n')
print(function(3,4), '\n')
print(function(3,2), '\n')
print(function(3,5), '\n')
print(function(3,4), '\n')
print(function(3,5), '\n')

