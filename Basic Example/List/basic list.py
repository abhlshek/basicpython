l=[]
print(l)

l=[1,2,3,4]
print(l)
print(type(l))

l=list([1,2,3,4,5])
print(l)
print(len(l))

list1=[1,2,3,45,6,7,8,9,9]
print(list1[0])
print(list1[-1])
print(list1[4])


l=list([1,2,3,4,4,5])
n=len(l)
print(n)

for i in range(n):
    print(i)
    print(l[i],'=',l[-n+i])