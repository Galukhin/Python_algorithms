"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""
num = int(input('Введите число: '))
max_num = 0
max_sum = 0
while num:
    tmp_num = num
    tmp_sum = 0
    while num:
        tmp_sum += num % 10
        num //= 10
    if tmp_sum > max_sum:
        max_sum = tmp_sum
        max_num = tmp_num
    num = int(input('Введите следующее число. Для выхода нажмите 0: '))
print(f'Наибольшее по сумме цифр число: {max_num}, его сумма: {max_sum}')


