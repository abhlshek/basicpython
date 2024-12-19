classroom = 'class 1'
rollno = 1
d = {(classroom, rollno): "dhoni"}
print(d)
print(type(d))
while True:
    print("0,exit", "1,create", "2,search", "3,delete", "4,all")
    num = int(input("enter value of number"))
    if num == 0:
        print('exit')
        break
    elif num == 1:
        print("create")
        classname = int(input("enter classname"))
        rollno = int(input("enter rollno"))
        name = input('enter name')
        d[classname, rollno] = name
    elif num == 2:
        print('search')
        classname = int(input('enter classname'))
        rollno = int(input("enter rollno"))
        search = d.get(classname, rollno)
        print(search)

    elif num == 3:
        print('delete')
        classname = int(input('enter classname'))
        rollno = int(input("enter rollno"))
        delete = d.pop((classname, rollno))
        print(delete)

    elif num == 4:
        print("recorde", d)
