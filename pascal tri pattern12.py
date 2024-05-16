def pascal(y, x):
    if x == 1:
        return 1
    if y == x:
        return 1
    return pascal(y - 1, x) + pascal(y - 1, x - 1)


n = 5
for row in range(1, n + 1):
    for space in range(1, n + 1 - row):
        print(" ", end="")
    for col in range(1, row + 1):
        value = pascal(row, col)
        print(value, end=" ")

    print()
