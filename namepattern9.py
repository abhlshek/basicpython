name = "DHONI"
n = len(name)
print(n)
for i in range(n + 1):

    for col in range(i):
        print(name[n-1-col], end="")
        # print(name[col], end="")
    print()
