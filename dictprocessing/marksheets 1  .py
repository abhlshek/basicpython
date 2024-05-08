result = {1: ["neeraj", 33, 5, 66], 2: ["saurabh", 55, 66, 67], 3: ["sunil", 44, 55, 66]}
print(result)
while True:
    print('o,exit', '1,search', '2,create', '3,delete', '4 ,all')
    num = int(input("enter num\n"))
    if num == 0:
        print("exit")
        break
    elif num == 1:
        print("search")
        rolln = int(input("enter the roll"))
        search = result.get(rolln)
        print(search)
        if search is None:
            print("not found")
        else:
            total = search[1] + search[2] + search[3]
            print("total", total)
            per = total / 3
            print("per", per)
            if per >= 60:
                print("first")
            elif per >= 50:
                print("second")
            elif per >= 40:
                print("third")
            else:
                print("fail")
    elif num == 2:
        print("create")
        rolln = int(input("enter rolln\n"))
        name = input("enter name\n")
        math = int(input("enter math\n"))
        computer = int(input("enter computer\n"))
        python = int(input("enter python\n"))
        result[rolln] = (name, math, computer, python)

    elif num == 3:
        print("delete")
        rolln = int(input("enter rolln\n"))
        delete = result.pop(rolln)
        print(delete)
    elif num == 4:
        print(result)
