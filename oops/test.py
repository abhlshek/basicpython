from bank import Union
print(Union)
account=Union (101,"dhoni",1000)
accounts={account.accountno:account,102:Union(102,"sachin",300),103:Union(103,"subham",500)}
while True:
    print("0,exit","1,search","2 credit","3 debit")
    num=int(input("enter num"))
    if num==0:
        print("exit")
        break
    elif num==1:
        print("search")
        account=int(input("enter account num"))
        search=accounts.get(account)
        print(search)
    
    elif num==2:
        print("credit")
        account=int(input("enter account no"))
        search=accounts.get(account)
        print(search)
        if search is None:
            print("not found")
        else:
            credit=int(input("enter credit "))
            print(search)
            if credit<=0:
                print("invalid")
            else:
               search.balance += credit
    elif num==3:
        print("debit")
        account=int(input("enter account num"))
        search=accounts.get(account)
        print(search)
        if search is None:
            print("not found")
        else:
            debit=int(input("enter debit"))
            if debit<=0:
                print("invalid")
            else:
                search.balance -= debit


