"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
"""
from collections import deque


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    start_vertex = start # Копирую start, т.к. он меняется в цикле, а для нахождения путей нужна первая вершина

    cost[start] = 0
    min_cost = 0
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    # Находим список путей по списку parent
    parent[start_vertex] = start_vertex # Начальный элемент не добавлялся в список parent.
    # Чисто технически у него нет родителя, но в видео в примере, как должна выглядеть таблица,
    # путь до начального элемента представляется этим самым элементом.
    ways = [deque() for _ in range(length)]
    for i in range(length):
        if parent[i] == -1:
            continue
        j = i
        if j != start_vertex:
            ways[i].appendleft(j)
        while parent[j] != start_vertex:
            ways[i].appendleft(parent[j])
            j = parent[j]
        ways[i].appendleft(start_vertex)

    return cost, ways

graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

start = 0
cost, ways = dijkstra(graph, start)
print(f'Кратчайшие расстояния от старта: {cost}')
print('Пути:')
for itm in ways:
    print(list(itm))
