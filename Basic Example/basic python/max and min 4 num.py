a = 10
b = 20
c = 30
d = 40
if a >= b and a >= c and a >= d:
    max = a
elif b >= c and b >= d and b >= a:
    max = b
elif c <= b and c <= a and c <= d:
    max = c
else:
    max = d
print("max",max)

# min 4 number

if a<=b and a<=c and a<=d:
    min=a
elif b<=c and b<=a and b<=d:
    min=b
elif c<=a and c<=b and c<=d:
    min=c
else:
    min=d
print("min",min)
