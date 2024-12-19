vote = {"bjp": 0, "sp": 0, "bp": 0}
print(vote)
while True:
    print("0,exit", "1,bjp", "3,sp", "4,total", "5,greater vote")
    num = int(input("enter num"))
    if num == 0:
        print("exit")
        break
    elif num == 1:
        print("bjp")
        noofvote = vote.get("bjp")
        print(noofvote)
        noofvote += 1
        vote["bjp"] = noofvote
    elif num == 2:
        print("sp")
        noofvote = vote.get("sp")
        print(noofvote)
        noofvote += 1
        vote["sp"] = noofvote
    elif num == 3:
        print("bp")
        noofvote = vote.get("bp")
        print(noofvote)
        noofvote += 1
        vote["bp"] = noofvote
    elif num == 4:
        print('total', vote)
    elif num == 5:
        print("greater")
        bjp = vote.get("bjp")
        sp = vote.get("sp")
        bp = vote.get("bp")
        if bjp > sp and bjp > bp:
            winner = "bjp"
            vote = "bjp"
        elif sp > bjp and sp > bp:
            winner = "sp"
            vote = "sp"
        elif bp > bjp and bp > sp:
            winner = "bp"
            vote = "bp"
        print(winner)
        print(vote)
