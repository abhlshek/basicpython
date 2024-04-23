r = range(1, 8, 1)
a, b = 0, 1
print(a, b, end=" ")  #single line ,end=""
for i in r:
    c = a + b
    a = b
    b = c
    print(c, end=" ")
