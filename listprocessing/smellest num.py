# a =[99,88,77,66,55,44,33,22,11]
# print("enter smellest num:",min(a))


# a =[7,9,5,3,9,1]
# a.sort()
# print("enter smallest num:",a[0])

# list = [33,88,2,0,6]
# list.sort()
# print("smellest no:",list[0])


# list = []
num =int(input("enter number of element in list:"))
list=[]
for i in range(1,num+1):
    element = int(input("enter the element"))
    list.append(element)
print("smellest num:",min(list))

