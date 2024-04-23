a, b = 8, 13
print(a, b)
c = a - b
while c > 0:
    print(c)
    a = b
    b = c
    c = a - b
print(c)
