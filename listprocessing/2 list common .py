l1 = [1,2,3,4]
l2 = [2,4,6,7]
common=[]
for i in l1:
    if i in l2 and not i in common:
        common.append(i)

print(common)