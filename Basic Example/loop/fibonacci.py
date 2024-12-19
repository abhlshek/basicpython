search = 143
result = "no"
if search == 0 or search == 1:
    result = "yes"
a, b = 0, 1
print(a, b)
c = a + b
while c < search and result == 'no':
    a = b
    b = c
    c = a + b
if c == search:
    result = 'yes'
print(result)
