
# Crypt Arithmetic: TWO + TWO = FOUR
from itertools import permutations

letters = "TWOFUR"

for p in permutations(range(10), len(letters)):
    d = dict(zip(letters, p))

    # First digits cannot be zero
    if d['T'] == 0 or d['F'] == 0:
        continue

    two = 100 * d['T'] + 10 * d['W'] + d['O']
    four = (1000 * d['F'] + 100 * d['O']
            + 10 * d['U'] + d['R'])

    if two + two == four:
        print("TWO =", two)
        print("FOUR =", four)
        print("Solution:", two, "+", two, "=", four)
        break
else:
    print("No solution found")
