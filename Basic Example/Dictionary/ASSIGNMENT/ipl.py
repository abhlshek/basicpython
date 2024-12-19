ipl = {"rr": (9, 8), "kk": (9, 6), "csk": (9, 5)}
teamname = input("enter name")
record = ipl.get(teamname)
print(record)
while True:
    print("0,exit", "1,create", "2,search", "3,delete", "4,all")
    num = int(input("enter num"))
    if num == 0:
        print("exit")
    elif num == 1:
        print("create")
        teamname = input("enter teamname")
        total = int(input("enter total"))
        win = int(input("enter win"))
        ipl[teamname] = (total, win)
    elif num == 2:
        print("search")
        teamname = input("enter teamname")
        score = ipl.get(teamname)
        print(score)
        total = score[0]
        win = score[1]
        loss = total - win
        pts = total + win - loss
        print("no of match", total, "win", win, "loss", loss, "pts", pts)
    elif num == 3:
        print("delete")
        delete = ipl.pop(teamname)
        print(delete)
    elif num == 4:
        print("all", ipl)
