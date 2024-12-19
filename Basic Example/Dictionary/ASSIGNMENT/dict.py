d = {}
print(d)
print(type(d))
while True:
    print("0,exit", "1,create", "2,delete", "3,search", "4,all")
    option = int(input("enter the option"))
    if option == 0:
        print("exit")
        break
    elif option == 1:
        print("create")
        key = input("enter key")
        value = int(input("enter value"))
        d[key] = value
    elif option == 2:
        print('delete')
        key = input("enter key")
        delete = d.pop(key)
        print(delete)
    elif option == 3:
        print('search')
        key = input("enter key")
        search = d.get(key)
        print(search)
    elif option == 4:
        print(d)
