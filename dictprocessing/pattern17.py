n = 7
for i in range(1, n + 1):
    for j in range(1, n + 1):
        condition = i == 1 or j == 1 or i ==n or j ==n or i ==j
        if condition:
            print(0, end="")

        else:
            print(" ", end="")

    print()
