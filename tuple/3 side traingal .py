marks = 4, 7, 1
print(type(marks))
a = marks[0]
b = marks[1]
c = marks[2]
s = (a + b + c) / 2
print(s)
area = (s * (s - a) * (s - b) * (s - c)) ** .5
print(area)
