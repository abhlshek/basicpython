n = 4
for row in range(1, n + 1):
    for space in range(1, n + 1 - row):
        print(" ", end="")
    for col in range(1, row+1):
        print(col, end="")
    for col in reversed(range(1, row)):
        print(col, end="")
    print()
