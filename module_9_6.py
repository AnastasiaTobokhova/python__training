# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
#
# Пункты задачи:
#
# Напишите функцию-генератор all_variants(text).
# Опишите логику работы внутри функции all_variants.
# Вызовите функцию all_variants и выполните итерации.

def all_variants(text):
    length = len(text)
    for i in range(length):
        for j in range(i + 1, length + 1):
            yield text[i:j]


a = all_variants("abc")
for i in a:
    print(i)
