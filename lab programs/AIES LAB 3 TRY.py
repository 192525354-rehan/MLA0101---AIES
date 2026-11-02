
import heapq

def ucs(graph, start, goal):
    pq = [(0, start, [start])]
    visited = {}

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited and visited[node] <= cost:
            continue

        visited[node] = cost

        if node == goal:
            return path, cost

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (cost + weight, neighbor, path + [neighbor])
                )

    return None, None

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 5)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

start = input("Enter source: ").upper()
goal = input("Enter destination: ").upper()

if start not in graph or goal not in graph:
    print("Invalid node")
else:
    path, cost = ucs(graph, start, goal)

    if path:
        print("Least-cost path:", " -> ".join(path))
        print("Minimum cost:", cost)
    else:
        print("No path found")
