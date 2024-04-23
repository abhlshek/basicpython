a = 20
b = 12
c = 15
d = 20
if a >= b and a >=c and a >= d :
    max = a
elif b >= c:
    max = b
elif c >= d:
    max = c
else:
    max = c
print(max)

if a <= b and a <= c and a <= d:
    min = a
elif b <= c:
    min = b
elif c <= d:
    min = c
else:
    min = d
print(min)
