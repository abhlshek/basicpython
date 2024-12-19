result={1:["raju",33,44,55],2:["neeraj",33,77,99],3:["dhoni",22,33,44],4:["sachin",88,99,12]}
print(result)
while True:
    print("0,exit","1,create","2,search","3,delete","4,all")
    num=int(input("enter num"))
    if num==0:
        print("exit")
        break
    elif num==1:
        print("create")
        roll=int(input("enter roll"))
        name=input("enter name")
        math=int(input("enter marks in math"))
        english=int(input("enter marks in english"))
        python=int(input("enter marks in python"))
        result[roll]=(name,math,english,python)
    elif num==2:
        print("search")
        roll=int(input("enter roll no"))
        search=result.get(roll)
        print(search)
        if result is None:
            print("not found")
        else:
            total=search[1]+search[2]+search[3]
            per=total/4
            print("total",total)
            print("per",per)
            if per>=60:
                print("first")
            elif per>=50:
                print("second")
            elif per>=40:
                print("third")
            else:
                print("fail")
    elif num==3:
        print('delete')
        roll=int(input("enter roll"))
        delete=result.pop(roll)
        print(delete)
    elif num==4:
        print("all",result)