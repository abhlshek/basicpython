a=22
b=66
c=222
d=11
if a<=b and a<=c and a<=d:
    min=a
elif b<=c:
    min=b
elif c<=d:
    min=c
else:
    min=d
print(min)