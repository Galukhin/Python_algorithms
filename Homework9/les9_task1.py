"""
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
    * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib
задача считается не решённой.
"""


def permutation(buf):
    """ генератор всех подстрок строки и возврат хэш подстрок
    :param buf:
    """
    length = len(buf)
    for l_len in range(1, length):
        for idx in range(length):
            if l_len + idx > length:
                break
            yield hash(buf[idx:(idx + l_len)])


def substring_unique(buf):
    """ последовательный анализ хэшей на уникальность и выдача длины списка уникальных
    :param buf:
    :return:
    """
    s_unique = []
    for tag in permutation(buf):
        if tag not in s_unique:
            s_unique.append(tag)
    return len(s_unique)


buf = input('Введите строку :')
print('Количество всех подстрок строки', len(list(permutation(buf))))
print('Количество различных подстрок строки', substring_unique(buf))
