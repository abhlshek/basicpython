ipl = {"rr": (9, 8), "kkr": (9, 6), "csk": (9, 5)}
teamname = input("enter teamname\n")
record = ipl.get(teamname)
print(record)
while True:
    print("0,exit", "1,create", "2,search", "3,delete", "4,all")
    num = int(input("enter num\n"))
    if num == 0:
        print("exit")
        break
    elif num == 1:
        print("create")
        key = input("enter key\n")
        total = int(input("enter num of match\n "))
        win = int(input("enter win\n"))
        ipl[key] = (total,win)

    elif num == 2:
        print("search")
        key = input("enter key\n")
        score = ipl.get(key)
        print(score)

        total = score[0]
        win = score[1]
        loss = total - win
        pts = total + win - loss
        print("num of match", total, "win", win, "loss", loss, "pts", pts)

    elif num == 3:
        print("delete")
        key = input("enter key\n")
        delete = ipl.pop(key)
        print(delete)
    elif num == 4:
        print(ipl)
