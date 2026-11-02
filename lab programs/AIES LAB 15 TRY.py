
# Family Knowledge Representation

parent = {
    ("John", "Alice"),
    ("John", "Bob"),
    ("Alice", "Carol"),
    ("Bob", "David")
}

def is_parent(x, y):
    return (x, y) in parent

def is_sibling(x, y):
    return any(
        is_parent(p, x) and is_parent(p, y) and x != y
        for p, child in parent
    )

def is_grandparent(x, y):
    return any(
        is_parent(x, p) and is_parent(p, y)
        for p, child in parent
    )

name1 = input("Enter first person: ").strip().title()
name2 = input("Enter second person: ").strip().title()

if is_parent(name1, name2):
    print(name1, "is the parent of", name2)
elif is_sibling(name1, name2):
    print(name1, "and", name2, "are siblings")
elif is_grandparent(name1, name2):
    print(name1, "is the grandparent of", name2)
else:
    print("No known relationship")
