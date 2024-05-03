import pickle

companys = {"maruti": ("swift", "white", 2016), "mahindra": ("scorpio", "black", 2004), "tata": ("safari", "red", 2000)}
print(companys)
while True:
    print("0,exit", "1,create", "2,save", "3,read", "4,delete")
    num = int(input("enter num\n"))
    if num == 0:
        print("exit")
        break
    elif num == 1:
        print("create")
        carcompany = input("enter carcompany\n")
        carname = input("enter carname\n")
        colur = input("enter colur\n")
        date = int(input("enter date"))
        companys[carcompany] = (carname, colur, date)
    elif num == 2:
        print("save")
        datafile = open("car colour date.txt", "ab")
        pickle.dump(companys, datafile)
        datafile.close()
    elif num == 3:
        print("read")
        datafile = open("car colour date.txt", 'rb')
        data = pickle.load(datafile)
        print(data)
    elif num == 4:
        print("delete")
        carcompany = input("enter carcompany\n")
        delete = companys.pop(carcompany)
        print(delete)
        print(companys)
