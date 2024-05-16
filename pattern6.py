n = 5
for row in range(1, n + 1):
    for space in range(1, n + 1 - row):
        print(" ", end="")
    for star in range(1, 2 * row):
        # print(chr(65+row-1), end="")
        print(chr(65+star-1),end="")
    print()

