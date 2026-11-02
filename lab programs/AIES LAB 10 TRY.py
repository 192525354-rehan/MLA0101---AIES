
# Towers of Hanoi

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter number of disks: "))

if n <= 0:
    print("Enter a positive number of disks.")
else:
    print("Sequence of moves:")
    hanoi(n, 'A', 'B', 'C')
    print("Total moves:", 2**n - 1)
