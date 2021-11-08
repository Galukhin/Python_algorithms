"""
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом
(не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.

les2_task3.py
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
если введено число 3486, надо вывести 6843.
"""

import cProfile
import random


def rev(func, n):
    """
    Вызов функции для тестирования и генерация случайного числа
    :param func:
    :param n: количество разрядов
    :return:
    """
    num = random.randint(10 ** (n - 1), 10 ** n)
    return num, func(num)


def reverse1(n):
    """
    Преобразование числа в обратное по порядку входящих в него цифр.
    Рекурсивный подход
    :param n:
    :return:
    """
    nn = n % 10
    rank = n // 10
    if rank == 0:
        return str(nn)
    else:
        return str(nn) + reverse1(rank)


def reverse2(n):
    """
    Преобразование числа в обратное по порядку входящих в него цифр.
    Итерационный подход
    :param n:
    :return:
    """
    result = ''
    while n > 0:
        result += str(n % 10)
        n //= 10
    return result


def reverse3(n):
    """
    Преобразование числа в обратное по порядку входящих в него цифр.
    Подход на основе срезов массивов
    :param n:
    :return:
    """
    return str(n)[-1::-1]


def test_reverse1(n):
    return rev(reverse1, n)


def test_reverse2(n):
    return rev(reverse2, n)


def test_reverse3(n):
    return rev(reverse3, n)


# cProfile.run('test_reverse1(10)')
# 20 function calls (11 primitive calls) in 0.002 seconds
# 10/1    0.000    0.000    0.000    0.000 les4_task1.py:32(reverse1)

# cProfile.run('test_reverse1(100)')
# 111 function calls (12 primitive calls) in 0.001 seconds
# 100/1    0.000    0.000    0.000    0.000 les4_task1.py:32(reverse1)

# cProfile.run('test_reverse1(500)')
# 513 function calls (14 primitive calls) in 0.002 seconds
# 500/1    0.002    0.000    0.002    0.002 les4_task1.py:32(reverse1)

""" 
Остальные функции не имеет смысла оценивать через cProfile, т.к. cProfile представляет интерес для оценки количества
вызываемых функций, а время их исполнения в данном примере все равно очень мало.
reverse1 - рекурсивная функция, и мы видим, что количество вызываемых функций практически равно входному параметру n.
При вызове остальных функций через cProfile, количество вызываемых функций останется неизменным.
Изменится лишь время исполнения. А его удобнее оценивать через timeit.
"""

# "les4_task1.test_reverse1(10)"
# 100 loops, best of 5: 21.5 usec per loop

# "les4_task1.test_reverse1(100)"
# 100 loops, best of 5: 93.2 usec per

# "les4_task1.test_reverse1(500)"
# 100 loops, best of 5: 709 usec per loop

# "les4_task1.test_reverse1(1000)"
# RecursionError: maximum recursion depth exceeded while getting the str of an object

# "les4_task1.test_reverse2(10)"
# 100 loops, best of 5: 9.82 usec per loop

# "les4_task1.test_reverse2(100)"
# 100 loops, best of 5: 79.7 usec per loop

# "les4_task1.test_reverse2(500)"
# 100 loops, best of 5: 586 usec per loop

# "les4_task1.test_reverse2(1000)"
# 100 loops, best of 5: 1.85 msec per loop

# "les4_task1.test_reverse3(10)"
# 100 loops, best of 5: 4.32 usec per loop

# "les4_task1.test_reverse3(100)"
# 100 loops, best of 5: 6.92 usec per loop

# "les4_task1.test_reverse3(500)"
# 100 loops, best of 5: 28.3 usec per loop

# "les4_task1.test_reverse3(1000)"
# 100 loops, best of 5: 76.6 usec per loop

"""
Выводы:
Рекурсивный алгоритм является самым худшим - у него и самое долгое время работы, и он имеет ограничение на 
глубину вызовов.
Итерационный подход быстрее рекурсивного и не имеет ограниченичения по параметру n, но самым быстрым является 
алгоритм на основе срезов массивов.
"""
