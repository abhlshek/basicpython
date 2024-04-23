n = int(input("enter the element list"))
l = []
for i in range(n):
    element = int(input("enter element num"))
    l.append(element)
print("my list", l)
sorted_list = l.sort()
print("sorted list", l)
min_element = l[0]
print("min_element",min_element)
max_element = l[-1]
print("max_element",max_element)
second_largest = l[-2]
print("second_largest",second_largest)
