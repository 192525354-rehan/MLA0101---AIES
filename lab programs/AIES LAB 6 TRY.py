
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
    u, v, cost = input("Enter edge (u v cost): ").split()
    cost = int(cost)
    graph[u].append((v, cost))
    graph[v].append((u, cost))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {}

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node in best and best[node] <= g:
            continue

        best[node] = g

        if node == goal:
            return g, path

        for neighbor, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + h[neighbor]

            if neighbor not in best or new_g < best[neighbor]:
                heapq.heappush(
                    pq, (new_f, new_g, neighbor, path + [neighbor])
                )

    return None

result = astar(start, goal)

if result:
    cost, path = result
    print("Optimal path:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("Goal not reachable")
