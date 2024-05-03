texi = {1: ("Dhoni", "VNS", 'LKO'), 2: ("sachin", "ghazi", "vns"), 3: ("virat", "mumbai", "ghazi")}
print(texi)
while True:
    print("0,exit", "1 booking", "2 cancel", "4 search")
    value = int(input("enter value=\n"))
    if value == 0:
        print("bye")
        break
    elif value == 2:
        print("cancel")
        texinum = int(input("enter texi num\n"))
        taxi = texi.get(texinum)
        if taxi is not None:
            print(taxi)
            texi.pop(texinum)
        else:
            print("not found")

    elif value == 1:
        print("booking")
        texinum = int(input("enter texinum\n"))
        name = input("enter name\n")
        src = input("enter going\n")
        dest = input("enter dest\n")
        texi[texinum] = (name, src, dest)

    elif value == 4:
        print("search")
        texinum = int(input("enter texi num\n"))
        texiservice = texi.get(texinum)
        print(texiservice)
