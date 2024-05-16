n = 5
for row in range(1, n + 1):
    for col in range(1, row + 1):
        # print(chr(65 + row - 1), end="")
        # print(chr(65 + col - 1), end=" ")
        print(chr(65 + col - 1), end=" ")
    print()
