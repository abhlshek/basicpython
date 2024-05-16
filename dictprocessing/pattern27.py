n = 8
mid = (n+1)//2
for row in range(1, n + 1):
    for col in range(1, n + 1):
        condition = col == 4 or row == mid
        if condition:
            print(" *", end='')
        else:
            print("  ", end="")
    print()
