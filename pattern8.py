n = 4
for row in range(1, n + 1):
    for space in range(1, n + 1 - row):
        print(" ", end="")
    for col in reversed(range(1, row + 1)):
        print(chr(65 + col - 1), end="")
    for col in reversed(range(row, 1, -1)):
        print(chr(65 + col - 1), end="")
    print()
