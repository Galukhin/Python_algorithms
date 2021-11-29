"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
import random


def gen_graph(num, cohesion):
    """ Генерация связанного графа
    :param num: Количество вершин
    :param cohesion: Связоность в вершине, выбирается случайно от 2 до cohesion [2,4]
    :return:
    """
    graph = {}
    for n in range(num):
        # кандидаты переходов
        roots = list(range(num))
        # исключить текущую
        del roots[n]
        graph[n] = set(random.sample(roots, random.choice([2, cohesion])))
    return graph


def dfs(graph, start=0, visited=None):
    """ обход графа поиском вглубину
    :param graph: граф
    :param start: стартовая вершина
    :param visited: фиксация посещений
    :return:
    """
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:  # исключить уже посещенные
        # вглубь по очередной вершине
        dfs(graph, next, visited)
    return visited


g = gen_graph(10, 2)
# сильно связанный граф
# g = gen_graph(10,4)

print(g)
print(dfs(g))
