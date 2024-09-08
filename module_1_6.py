#словарь

my_dict = {'Anastasia': 1997,
           'Alyona': 1998,
           'Alex': 2001,
           'Ivan': 2004}
print(my_dict)
print(my_dict.get('Anastasia'))
print(my_dict.get('Max', 'Такого ключа нет'))
print(my_dict)
my_dict.update({'Masha': 1999,
                'Misha': 2002})
print(my_dict)
a = my_dict.pop('Alex')
print(my_dict)
print(a)
print(my_dict)

#множества

my_set = {1,1,2,2,'peach','lemon','peach','lemon'}
print(my_set)
my_set.add(3)
my_set.add('sun')
print(my_set)
my_set.remove(1)
print(my_set)





