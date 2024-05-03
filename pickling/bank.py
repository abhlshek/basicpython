import pickle

# accountno:(name, balance)
accounts = {}
while True:
    print("1,save", "2 read", "3 create", "4 search", "0,exit", "5,credit", "6,debit")
    filename = "bank info.txt"
    num = int(input("enter num\n"))
    if num == 1:
        print("save")
        datafile = open(filename, "ab")
        pickle.dump(accounts, datafile)
        datafile.close()


    elif num == 2:
        print("read")
        datafile = open(filename, "rb")
        data = pickle.load(datafile)
        print(data)


    elif num == 3:
        print("create")
        account = int(input("enter account num\n"))
        name = input("enter name\n")
        balance = int(input("enter balance\n"))
        # accounts[account] = {"name": name, "balance": balance}
        # print(accounts)
        if balance <= 0:
            print("no bal")
        else:
            accounts[account] = {"name": name,"balance": balance}
            print(accounts)


    elif num == 4:
        print("search")
        account = int(input("enter account\n"))
        search = accounts.get(account)
        print(search)


    elif num == 5:
        print("credit")
        accountno = int(input("enter account\n"))
        search = accounts.get(accountno)
        print(search)
        if search is None:
            print("not found")
        else:
            credit = int(input("enter credit\n"))
            # search['balance'] += credit

            if credit <= 0:
                print("no bal")

            else:
                search["balance"] += credit


    elif num == 6:
        print("debit")
        accountno = int(input("enter accountno\n"))
        search = accounts.get(accountno)
        if account is None:
            print("not found")
        else:
            debit = int(input("enter debit\n"))
            if balance < debit:
                print("error")
            else:
                search["balance"] -= debit
    elif num == 0:
        print("exit")
        break
