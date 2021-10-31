"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
from random import randint

my_list = [randint(1, 10) for _ in range(20)]
min_value = my_list[0]
max_value = my_list[0]
for itm in my_list:
    if itm < min_value:
        min_value = itm
    elif itm > max_value:
        max_value = itm
print(f'Исходный массив: {my_list}')
my_list[my_list.index(min_value)] = max_value
my_list[my_list.index(max_value)] = min_value
print(f'Измененный массив: {my_list}')
