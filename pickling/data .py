import pickle

d = dict()
filename = "states.txt"
print(d)
while True:
    print("0 exit", "1,save", "2 read", "3 create", "4,delete")
    num = int(input("enter num\n"))
    if num == 0:
        print("exit")
        break
    elif num == 1:
        print("save")
        datafile = open(filename, "ab")
        pickle.dump(d, datafile)  # save
        datafile.close()

    elif num == 2:
        print("read")
        datafile = open(filename, "rb")
        data = pickle.load(datafile)  # read
        print(data)

    elif num == 3:
        print("create")
        state = input("enter state\n")
        capital = input("enter capital\n")
        d[state] = capital
        print(d)
    elif num == 4:
        print("delete")
        state = input("enter state\n")
        delete = d.pop(state)
        print(delete)
        print(d)
