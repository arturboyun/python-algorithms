from collections import deque


def bfs(graph, start):
    """
    Выполняет поиск в ширину (BFS) в графе, начиная с вершины start.

    :param graph: Словарь, представляющий граф в виде списка смежности.
                  Ключи - вершины, значения - списки соседних вершин.
    :param start: Вершина, с которой начинается обход.
    :return: Список вершин в порядке их посещения.
    """
    visited = set()  # Множество посещённых вершин
    queue = deque([start])  # Очередь для BFS, начиная с начальной вершины
    order_of_visit = []  # Порядок посещения вершин

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            order_of_visit.append(vertex)
            # Добавляем всех непосещённых соседей в очередь
            queue.extend(
                neighbour for neighbour in graph[vertex] if neighbour not in visited
            )

    return order_of_visit


# Пример использования:
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

start_vertex = "A"
print("Порядок посещения вершин:", bfs(graph, start_vertex))