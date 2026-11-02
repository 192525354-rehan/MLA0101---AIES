
# Minimax Algorithm

tree = {}

n = int(input("Enter number of child nodes: "))

for i in range(n):
    node = input("Enter parent node: ").strip()
    children = input("Enter child nodes separated by space: ").split()
    tree[node] = children

values = {}
m = int(input("Enter number of leaf nodes: "))

for i in range(m):
    node = input("Enter leaf node: ").strip()
    value = int(input("Enter value: "))
    values[node] = value

def minimax(node, is_max):
    if node not in tree:
        return values[node]

    scores = [minimax(child, not is_max)
              for child in tree[node]]

    if is_max:
        return max(scores)
    else:
        return min(scores)

root = input("Enter root node: ").strip()

result = minimax(root, True)
print("Best value:", result)
