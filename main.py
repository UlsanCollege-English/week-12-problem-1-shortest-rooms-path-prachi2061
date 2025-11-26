from collections import deque

def bfs_shortest_path(graph, start, goal):
    if start not in graph or goal not in graph:
        return []

    if start == goal:
        return [start]

    visited = set([start])
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == goal:
                    return new_path
                queue.append(new_path)
                visited.add(neighbor)

    return []
