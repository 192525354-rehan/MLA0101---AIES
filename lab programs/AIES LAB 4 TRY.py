
import heapq

graph = {}
h = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")
    h[node] = int(input("Enter heuristic value: "))
    graph[node] = []

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = input("Enter edge (u v): ").split()
    graph[u].append(v)
    graph[v].append(u)

start = input("Enter start node: ")
goal = input("Enter goal node: ")

def best_first(start, goal):
    pq = [(h[start], start, [start])]
    visited = set()

    while pq:
        _, node, path = heapq.heappop(pq)

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    pq, (h[neighbor], neighbor, path + [neighbor])
                )

    return None

path = best_first(start, goal)

if path:
    print("Path found:", " -> ".join(path))
else:
    print("Goal not reachable")
