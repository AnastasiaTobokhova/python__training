# практика импортирования функций сортировки из пакета и их использование
from sort.softfunc import bubble_sort, insertion_sort, selection_sort

data_1 = [9,7,4,5,6,2,1,3]
data_2 = [9,4,5,7,2,3,1,5,8,6]
data_3 = [9,4,5,6,2,4,6,8,7,6,2,1,3]

print(bubble_sort(data_1))
print(bubble_sort(data_2))
print(bubble_sort(data_3))
print(insertion_sort(data_1))
print(insertion_sort(data_2))
print(insertion_sort(data_3))
print(selection_sort(data_1))
print(selection_sort(data_2))
print(selection_sort(data_3))
