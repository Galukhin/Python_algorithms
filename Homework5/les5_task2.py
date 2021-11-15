"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
"""
from collections import deque

a = input('Введите первое шестнадцатеричное число: ')
b = input('Введите второе шестнадцатеричное число: ')


def hex_apply(a, b):
    a = deque(a.upper())
    b = deque(b.upper())

    hex_tuple = tuple('0123456789ABCDEF')

    a.extendleft('0' * (max(len(a), len(b)) - len(a)))  # Выравнивание нулями
    b.extendleft('0' * (max(len(a), len(b)) - len(b)))

    result = deque()
    overflow = 0
    for _ in range(len(a)):
        tmp = hex_tuple.index(a.pop()) + hex_tuple.index(b.pop()) + overflow
        result.extendleft([hex_tuple[tmp % 16]])
        overflow = tmp // 16

    if overflow:
        result.extendleft(['1'])

    return result


def hex_multiply(a, b):
    a = deque(a.upper())
    b = deque(b.upper())
    spam = deque()

    hex_tuple = tuple('0123456789ABCDEF')

    for i in range(len(a)):
        tmp_res = deque()
        overflow = 0
        b_ = b.copy()
        for _ in range(len(b_)):
            tmp = hex_tuple.index(a[i]) * hex_tuple.index(b_.pop()) + overflow
            tmp_res.extendleft([hex_tuple[tmp % 16]])
            overflow = tmp // 16
        if overflow:
            tmp_res.extendleft([hex_tuple[overflow]])
        tmp_res.extend('0' * (len(a) - 1 - i))
        spam.append(tmp_res)

    result = deque('0')
    for itm in spam:
        result = hex_apply(''.join(result), ''.join(itm))

    return result


print(''.join(hex_apply(a, b)))
print(''.join(hex_multiply(a, b)))
