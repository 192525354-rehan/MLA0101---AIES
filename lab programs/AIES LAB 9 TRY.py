
# Water Jug Problem using BFS
from collections import deque

capacity1 = int(input("Enter capacity of jug 1: "))
capacity2 = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target amount: "))

def water_jug():
    start = (0, 0)
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == target or b == target:
            return path + [(a, b)]

        x = min(a, capacity2 - b)
        y = min(b, capacity1 - a)

        states = [
            (capacity1, b),  # Fill jug 1
            (a, capacity2),  # Fill jug 2
            (0, b),          # Empty jug 1
            (a, 0),          # Empty jug 2
            (a - x, b + x),  # Pour jug 1 into jug 2
            (a + y, b - y)   # Pour jug 2 into jug 1
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [(a, b)]))

    return None

if target < 0 or target > max(capacity1, capacity2):
    print("Target cannot be measured in either jug.")
else:
    result = water_jug()

    if result:
        print("Sequence of states (Jug 1, Jug 2):")
        for state in result:
            print(state)
    else:
        print("Target cannot be reached.")
