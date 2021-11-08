"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и
попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:
sieve(2)
3
prime(4)
7
sieve(5)
11
prime(1)
2
Примечание по профилированию кода: для получения достоверных результатов при замере времени
необходимо исключить/заменить функции print() и input() в анализируемом коде.
С ними вы будете замерять время вывода данных в терминал и время, потраченное пользователем,
на ввод данных, а не быстродействие самого алгоритма.
"""
import cProfile


def prime(num):
    n = 10 ** 6

    def is_prime(n):
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        return d * d > n

    count = 0
    res = 0
    for elem in range(2, n):
        if is_prime(elem):
            count += 1
            if count == num:
                res = elem
                break
    return res


def sieve(num):
    n = 10 ** 6
    si = [i for i in range(n)]
    si[1] = 0
    for i in range(2, n):
        if si[i] != 0:
            j = i * 2
            while j < n:
                si[j] = 0
                j += i
    count = 0
    res = 0
    for elem in si:
        if elem != 0:
            count += 1
            if count == num:
                res = elem
                break
    return res


"""
cProfile.run('prime(100)')
         544 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 les4_task2.py:27(prime)
      540    0.001    0.000    0.001    0.000 les4_task2.py:30(is_prime)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

"""
cProfile.run('prime(500)')
         3574 function calls in 0.009 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.002    0.002    0.009    0.009 les4_task2.py:27(prime)
     3570    0.008    0.000    0.008    0.000 les4_task2.py:30(is_prime)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
cProfile.run('prime(1000)')
         7922 function calls in 0.027 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.027    0.027 <string>:1(<module>)
        1    0.004    0.004    0.027    0.027 les4_task2.py:27(prime)
     7918    0.024    0.000    0.024    0.000 les4_task2.py:30(is_prime)
        1    0.000    0.000    0.027    0.027 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
cProfile.run('sieve(100)')
         5 function calls in 0.969 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.017    0.017    0.969    0.969 <string>:1(<module>)
        1    0.817    0.817    0.952    0.952 les4_task2.py:47(sieve)
        1    0.135    0.135    0.135    0.135 les4_task2.py:49(<listcomp>)
        1    0.000    0.000    0.969    0.969 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
cProfile.run('sieve(500)')
         5 function calls in 0.906 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.017    0.017    0.906    0.906 <string>:1(<module>)
        1    0.768    0.768    0.889    0.889 les4_task2.py:47(sieve)
        1    0.120    0.120    0.120    0.120 les4_task2.py:49(<listcomp>)
        1    0.000    0.000    0.906    0.906 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
cProfile.run('sieve(1000)')
         5 function calls in 0.969 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.016    0.016    0.969    0.969 <string>:1(<module>)
        1    0.818    0.818    0.953    0.953 les4_task2.py:47(sieve)
        1    0.135    0.135    0.135    0.135 les4_task2.py:49(<listcomp>)
        1    0.000    0.000    0.969    0.969 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
"les4_task2.prime(100)"
100 loops, best of 5: 615 usec per loop
"""

"""
"les4_task2.prime(500)"
100 loops, best of 5: 6.7 msec per loop
"""

"""
"les4_task2.prime(1000)"
100 loops, best of 5: 19 msec per loop
"""

"""
"les4_task2.sieve(100)"
10 loops, best of 5: 855 msec per loop
"""

"""
"les4_task2.sieve(500)"
10 loops, best of 5: 906 msec per loop
"""

"""
"les4_task2.sieve(1000)"
10 loops, best of 5: 900 msec per loop
"""

"""
Выводы:
Сложность алгоритма решета не зависит от входных данных, но выполняется очень долго. Это происходит из-за того,
что "решето" долго заполняется простыми числами.
Второй алгоритм быстрее, но имеет квадратичную сложность. Также возрастает количество вызываемых функций, 
но это не рекурсивный вызов, поэтому ограничений нет.
"""
