
from collections import deque

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

start = input("Enter starting room: ").upper()
goal = input("Enter destination room: ").upper()

if start not in graph or goal not in graph:
    print("Invalid room")
else:
    path = bfs(graph, start, goal)

    if path:
        print("Shortest path:", " -> ".join(path))
        print("Number of steps:", len(path) - 1)
    else:
        print("No path found")
