n = 7
mid = (n + 1) // 2
for row in range(1, n + 1):
    for col in range(1, n + 1):

        condition = (row + col >= mid + 1) and (row + col <= mid + n) and (row - col <= mid - 1) and (
                col - row <= mid - 1) and (row >= mid)
        if condition:
            print(" *", end="")
        else:
            print("  ", end="")
    print()
