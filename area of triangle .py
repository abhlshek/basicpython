a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))

s = (a + b + c) / 2
# print(s)3

# s = int(input("enter s"))
area = (s * (s - a) * (s - b) * (s - c))
area = area ** .5
print(area)
