"""
Определить, какое число в массиве встречается чаще всего.
"""
my_list = list(map(int, input('Введите массив целых чисел через пробел: ').split()))
uniq_val = list(set(my_list))
my_dict = {i: 0 for i in uniq_val}
for itm in my_list:
    my_dict[itm] += 1
max_count_idx = my_list[0]
for itm in my_dict:
    if my_dict[itm] > my_dict[max_count_idx]:
        max_count_idx = itm
print(f'Чаще всего в массиве встречается число {max_count_idx}')
