# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list.append(10)
# print(type(list), list)
#
# list =['raju','shivam','sonu']
# list.append('sushil')
# print(list)
#
# list1=[1,2,3,4]
# list2=[5,6,7,8,9]
# list1.append(list2)
# print(list1)


# list1=[1,2,3,4,5]
# list2=[6,7,8]
# list3=['raju','nilesh','manish']
# list1.append(list2+list3)
# print(list1)

list1=[1,3,5,7,9]
list2=[2,4,6,8,0]
list1.extend(list2)
list1.append(list2)
print(list1)
