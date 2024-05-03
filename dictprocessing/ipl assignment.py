ipl = {"rr": (9, 8), "kkr": (9, 6), "csk": (9, 5)}
# print(ipl)
while True:
    print("1,rr", "2,kkr", "3,csk")
    num = int(input("enter num\n"))
    if num == 1:
        # print("rr")
        teamname = input("enter teamname\n")
        rr = ipl.get(teamname)
        print(rr)
    elif num == 2:
        print("kkr")
        teamname = input("enter teamname\n")
        kkr = ipl.get(teamname)
    elif num == 3:
        print("csk")
        teamname = input("enter teamname\n")
        csk = ipl.get(teamname)

    for key in ipl.keys():
        score = ipl[key]

        # print(key, score )
        print(key)
    teamname = key
    total = score[0]

    win = score[1]

    loss = total - win

    pts = total + win - loss

    print("num of match", total, "win", win, "loss", loss, "pts", pts)
