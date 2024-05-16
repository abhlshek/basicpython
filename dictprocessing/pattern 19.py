n = 7
for row in range(1, n + 1):
    for col in range(1, n + 1):



        mid = (row + col)
        condition = (row + col == 5) or (row + col == 11) or (row - col == -3) or (row - col == 3)
        if condition:
            print('0', end="")
        else:
            print(' ', end="")
    print()
