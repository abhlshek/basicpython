# l = [1,1,1,2,3,3,4]
# l1 = []
# for i in l:
#     if i in not l1:
#         l1.append(i)
#     else:
#         print(i,end=',')


list = [1,1,1,2,3,3,4]
print(list)
list.sort()
print(list)
n = len(list)
b = [list[0]]
print(n)
print(b)
for i in range(1,n):
    if list[i] != list[i-1]:
        b =b+[list[i]]
print(b)




