
def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

start = input("Enter starting room: ").upper()

if start not in graph:
    print("Invalid room")
else:
    print("DFS Traversal:")
    visited = set()
    dfs(graph, start, visited)
    print()
