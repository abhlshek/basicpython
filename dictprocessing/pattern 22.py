n = 7
mid = (n + 1) // 2
for row in range(1, n + 1):
    for col in range(1, n + 1):

        condition = (row <= mid) and (row == col) or col == 1 or col == n or (row + col == n + 1 and row <= mid)
        if condition:
            print('*', end='')
        else:
            print(" ", end="")
    print()
