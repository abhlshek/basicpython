texi = {"up61": ("Dhoni", "VNS", 'LKO'), "up65": ("sachin", "ghazi", "vns"), "up70": ("virat", "mumbai", "ghazi")}
print(texi)
while True:
    print("0,exit", "1 booking", "2 cancel", "4 search","3 all")
    value = int(input("enter value=\n"))
    if value == 0:
        print("bye")
        break
    elif value == 2:
        print("cancel")
        texinum = input("enter texi num\n")
        cancel = texi.get(texinum)
        if cancel is not None:
            print(cancel)
            texi.pop(texinum)
        else:
            print("not found")

    elif value == 1:
        print("booking")
        texinum = input("enter texinum\n")
        name = input("enter name\n")
        src = input("enter going\n")
        dest = input("enter dest\n")
        texi[texinum] = (name, src, dest)

    elif value == 4:
        print("search")
        texinum = input("enter texi num\n")
        texiservice = texi.get(texinum)
        print(texiservice)

    elif value == 3:
        print(texi)