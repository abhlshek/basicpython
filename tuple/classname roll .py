classname = "Class 1"
rollno = 1
d = {(classname, rollno): "Dhoni"}
print(type(d))
print(d)
while True:
    print("0,exit", "1,create", "2,search", "3,delete", "4 all")
    num = int(input("enter number\n"))
    if num == 0:
        print("exit")
        break
    elif num == 1:
        print("create")
        classname = input("enter classname\n")
        rollno = int(input("enter rollno\n"))
        name = input("enter name\n")
        d[classname, rollno] = name
    elif num == 2:
        print("search")
        classname = input("enter classname\n")
        rollno = int(input("enter rollno"))
        search = d.get((classname,rollno))
        print(search)
    elif num == 3:
        print("delete")
        classname = input("enter classname\n")
        rollno = int(input("enter rolln\n"))
        delete = d.pop((classname,rollno))
        print(delete)
    elif num == 4:
        print(d)
