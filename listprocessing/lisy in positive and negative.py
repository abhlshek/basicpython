list = [1,2,-3,-4,0]
# list = int(input("enter list\n"))
for i in list:
    if i >0:
        print("positive")
    # elif i<=0:
    #     print("negative")
    elif i == 0:
        print("zero")
    else:
        print("negative")