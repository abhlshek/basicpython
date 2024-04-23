l = [1,2,3, 5, 7, 1, 5, 3]
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i, end=',')
