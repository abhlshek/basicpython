table = 1, 10
i = table[0]
n = table[1]
while i <= n:
    print((3 * i))
    i += 1

n = 3
table = []
for i in range(1, 11):
    table.append(n * i)
print(tuple(table))
