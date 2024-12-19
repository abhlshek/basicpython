# l1 = [1, 2, 3, 4, 5, 3, 2, 9, 7, 8, 6, 9, 6, 5]
# l2 = []
# for i in l1:
#     if i not in l2:
#         l1.append(i)
#     else:
#         print(i, end="")


# a = [1, 1, 1, 2, 6, 5, 4, 4, 4, 3, 3]
# l1 = []
# for i in a:
#     if i not in l1:
#         l1.append(i)
#     else:
#         print(i, end='')


a = [1, 1, 1, 2, 6, 5, 4, 4, 4, 3, 3]
print(a)
a.sort()
print(a)
b=[a[0]]
n=len(a)
print(n)
print(b)

for i in range(1,n):
    if a[i] != a[i-1]:
        b=b+[a[i]]
print(b)
