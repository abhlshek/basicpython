d = dict()
# print(type(d))
while True:
    print("0 exit", "1 create", "2 delete", "3 search", "4 All")
    option = int(input("Option=\n"))
    if option == 0:
        print("Bye")
        break
    elif option == 1:
        print("Create")
        key = input("Enter Key\n")
        value = input("Enter Value\n")
        d[key] = value
    elif option == 2:
        print("delete")
        key = input("enter key\n")
        delete = d.pop(key)
        print(delete)
    elif option == 3:
        print("search")
        key = input("enter key\n")
        search = d.get(key)
        print(search)
    elif option == 4:
        print(d)


    elif option == 4:
        print(d)
    else:
        print("Bad option")
