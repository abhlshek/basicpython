num = int(input('enter num'))
list = []
for i in range(1, num + 1):
    element = int(input('enter element'))
    list.append(element)
    print(min(list))
