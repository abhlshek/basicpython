a = [1, 1, 1, 1, 2, 6, 5, 4, 4, 4, 3, 3]
print(a)
a.sort()
print(a)
b = [a[0]]
n = len(a)
print(n)
print(b)
for i in range(1, n):
    if a[i] != a[i - 1]:
        b = b + [a[i]]
print(b)
