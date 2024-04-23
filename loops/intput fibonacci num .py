search = 143
result = "No"
if search == 0 or search == 1:
    result = "Yes"

a, b = 0, 1
print(a, b)
c = a + b
while c < search and result == "No":
    a = b
    b = c
    c = a + b
if c == search:
    result = "Yes"
print(result)
