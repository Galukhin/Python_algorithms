"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""
n = int(input('Введите число первых членов последовательности: '))
idx = 1
el = 1
sum = 1
while idx < n:
    idx += 1
    el /= -2
    sum += el
print(sum)
