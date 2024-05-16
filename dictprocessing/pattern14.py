n = 5
h = 2 * n + 1
for row in range(1, n + 1):
    for star in range(1, row + 1):
        print("*", end="")
    for space in range(h - 2 * row + 1):
        print(" ", end="")

    for star in range(1, row + 1):
        print("*", end="")
    print()

for i in range(1, 2 * n + 3):
    print('*', end="")
print()

for row in reversed(range(1, n + 1)):
    for star in range(1, row + 1):
        print("*", end="")
    for space in range(h - 2 * row + 1):
        print(" ", end="")

    for star in range(1, row + 1):
        print("*", end="")
    print()
