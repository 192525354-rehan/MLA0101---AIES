
import heapq

def greedy_best_first(graph, heuristic, start, goal):
    pq = [(heuristic[start], start, [start])]
    visited = set()

    while pq:
        h, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (heuristic[neighbor], neighbor, path + [neighbor])
                )

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'F': 3,
    'G': 0
}

start = input("Enter starting rack: ").upper()
goal = input("Enter destination rack: ").upper()

if start not in graph or goal not in graph:
    print("Invalid rack")
else:
    path = greedy_best_first(graph, heuristic, start, goal)

    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found")
