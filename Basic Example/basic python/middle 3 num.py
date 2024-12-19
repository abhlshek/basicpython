a = 1
b = 2
c = 3
if a <= b and a >= c or a <= c and a >= b:
    mid = a
elif b <= c and b >= a or b >= c and b <= a:
    mid = b
else:
    mid = c

print(mid)
