import pickle

import pickle

d = dict()
print(d)
filename = state.txt
while True:
    print("o,exit", "1.save", "2,read", "3,create", "4,delete")
    num = int(int(input("enter num")))
    if num == 0:
        print("exit")
    elif num == 1:
        print("save")
        datafile = open(filename, 'ab')
        pickle.dump(d, filename)
        datafile.close()
    elif num == 2:
        print("read")
        datafile = open(filename, 'rb')
        data = pickle.load(datafile)
        print(data)
    elif num == 3:
        state = input("enter state name")
        capital = input("enter capital name")
        d[state] = capital
    elif num == 4:
        state = input("enter state name")
        delete = d.pop(state)
        print(delete)
