list1=[1,2,3,4,5,6,7,8,9]
list2=[2,3,6,5,8,9]
common=[]
for i in list1:
    if i in list2 and not i in  common:
        common.append(i)
        print(common)