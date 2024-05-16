name = "sushilyadav"
n = len(name)
print(n)
for row in range(n + 1):

    for col in range(row):
        # print(name[col], end="")
        print(name[n-1-col],end="")
    print()
