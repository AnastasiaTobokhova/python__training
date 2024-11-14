letters = ['r', 'e', 'd', 'u', 'c', 'e']

from functools import reduce

# store the result of your reduce function in the variable word

word = reduce(lambda x,y: x+y, letters)

# print word

print(word)

# собрать слово с помощью функции reduce