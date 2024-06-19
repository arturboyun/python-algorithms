def dfs(graph, start, search, visited=None):
    if visited is None:
        visited = set()

    if search == start:
        return True

    if start in visited:
        return False

    visited.add(start)

    print(start)
    print(visited)

    for next in graph[start] - visited:
        if dfs(graph, next, search, visited):
            return True
    return False


graph = {
    "A": {"B", "C"},
    "B": {"A", "D", "E"},
    "C": {"A", "F"},
    "D": {"B"},
    "E": {"B", "F"},
    "F": {"C", "E", "G"},
    "G": {"F", "H"},
    "H": {"G", "I"},
    "I": {"H"},
}

a = dfs(graph, "A", "I")

print(a)
