
# Alpha-Beta Pruning Algorithm

tree = {}

n = int(input("Enter number of parent nodes: "))

for i in range(n):
    node = input("Enter parent node: ").strip()
    children = input("Enter child nodes separated by space: ").split()
    tree[node] = children

values = {}
m = int(input("Enter number of leaf nodes: "))

for i in range(m):
    node = input("Enter leaf node: ").strip()
    values[node] = int(input("Enter leaf value: "))

def alphabeta(node, alpha, beta, is_max):
    if node not in tree:
        return values[node]

    if is_max:
        best = float('-inf')
        for child in tree[node]:
            best = max(best, alphabeta(child, alpha, beta, False))
            alpha = max(alpha, best)

            if beta <= alpha:
                break
        return best

    else:
        best = float('inf')
        for child in tree[node]:
            best = min(best, alphabeta(child, alpha, beta, True))
            beta = min(beta, best)

            if beta <= alpha:
                break
        return best

root = input("Enter root node: ").strip()

result = alphabeta(root, float('-inf'), float('inf'), True)

print("Best value:", result)
