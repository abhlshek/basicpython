n = 7
for row in range(1, n + 1):
    for col in range(1, n + 1):
        # condition = row + col == n+1
        # condition = row + col >= n+1
        # condition = row + col <= n+1
        condition = row + col ==5


        if condition:
            print('0', end="")
        else:
            print(' ', end="")
    print()
