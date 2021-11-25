"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
(сортировка слиянием также недопустима).
"""

import random

m = 20

array = [random.randint(0, 10) for _ in range(2 * m + 1)]
print(array)


def get_median(array):
    result = None
    for i in range(len(array)):
        more_count = 0
        middle_count = 0
        less_count = 0
        for j in range(len(array)):
            if array[j] > array[i]:
                more_count += 1
            elif array[j] == array[i]:
                middle_count += 1
            else:
                less_count += 1
        if more_count + middle_count > less_count and less_count + middle_count > more_count:
            result = array[i]
            break
    return result


print(f'median = {get_median(array)}')
# Проверка:
array.sort()
print(f'checked median = {array[len(array) // 2]}')

"""
Данная функция не сортирует массив, а именно ищет медиану. Для каждого элемента массива считается количество
элементов больших данного элемента, равных ему, и меньших. Далее, если выполняется условие в операторе if,
данный элемент и является медианой.
Пояснение условия:
Дан массив [0, 1, 2, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7].
Тогда more_count = 4, middle_count = 6, less_count = 3.
И тогда выполнение именно представленного условия говорит о том, что значения в подмножестве middle_count
являются медианой.
Сложность такого алгоритма - O(n**2)
"""
