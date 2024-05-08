votes = {"bjp": 0, "sp": 0, "bp": 0}
print(votes)
while True:
    print("0,exit", "1,bjp", "2,sp", "3,bp", "4,total", "5, greater vote")
    num = int(input("enter num\n"))
    if num == 0:
        print("bye")
        break
    elif num == 1:
        print("bjp")
        noofvotes = votes.get("bjp")
        print(noofvotes)
        noofvotes += 1
        votes["bjp"] = noofvotes


    elif num == 2:
        print("sp")
        noofvotes = votes.get("sp")
        print(noofvotes)
        noofvotes += 1
        votes["sp"] = noofvotes


    elif num == 3:
        print("bp")
        noofvotes = votes.get("bp")
        print(noofvotes)
        noofvotes += 1
        votes["bp"] = noofvotes


    elif num == 4:
        print("total", votes)

    elif num == 5:
        print("greater")
        bjp = votes.get("bjp")

        sp = votes.get("sp")

        bp = votes.get("bp")

        if bjp > sp and bjp > bp:
            winner = "bjP"
            votes = bjp
        elif sp > bjp and sp > bp:
            winner = "sp"
            votes = sp
        elif bp > bjp and bp > sp:
            winner = "bp"
            votes = bp

        print("winner", winner)
        print("votes", votes)
