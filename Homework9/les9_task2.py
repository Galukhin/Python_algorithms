"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter


class Node:
    def __init__(self, freq, value, left=None, right=None):
        self.freq = freq
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        """ форма при печати
        :return:
        """
        return f'\n({self.value}:{self.freq}, left={self.left}, right={self.right})'
        # return f'Node(freg={self.freq}, value={self.value}, left={self.left}, right={self.right})'

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        """ перегрузка оператора сложения для вершин
        :param other:
        :return:
        """
        # в результируещей вершине складывается тольоко частоты
        return Node(self.freq + other.freq, None, left=self, right=other)

    @staticmethod
    def has_path(root, value, path):
        """ воспроизводит путо до листа с символом
        :param root:
        :param value:
        :param path: возвращает путь
        :return:
        """
        if not root:
            return False
        if root.value == value:
            return True
        if Node.has_path(root.left, value, path):
            path.append('0')
            return True
        if Node.has_path(root.right, value, path):
            path.append('1')
            return True
        return False


def build_tree(alphabet):
    """ по частотному словарю строит дерево
    :param alphabet:
    :return:
    """
    # преобразование словаря в узлы
    tree = [Node(value, key) for key, value in alphabet.items()]

    while 1:
        # сортировка на каждом шаге
        tree.sort(key=lambda item: item.freq)
        # остался один узел
        if len(tree) < 2:
            break
        #  сложение двух узлов
        node = tree[0] + tree[1]
        # по старые удаляем
        del tree[0]
        del tree[0]
        # добавление в начало
        tree = [node] + tree
    return tree


def codec_houf(buf):
    """ главная функция
    1. построение частотного словаря
    2. создание деревва
    3. построение словаря для кодирования
    :param buf:
    :return:
    """
    alphabet = Counter(buf)
    tree = build_tree(alphabet)[0]
    for key in alphabet.keys():
        path = []
        Node.has_path(tree, key, path)
        alphabet[key] = ''.join(path[:])
    return dict(alphabet)


if __name__ == '__main__':
    phrase = 'beep boop beer!'
    # phrase = input("Введите фразу :")
    print('Фраза : ', phrase)
    codec = codec_houf(phrase)
    print("Алфавит: ", codec)
    sec = [codec[sym] for sym in phrase]
    print("Фраза по символам: ", sec)
    print("Фраза закодированная в HEX форме: ", hex(int(''.join(sec), base=2)))
