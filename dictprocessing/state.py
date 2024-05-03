statescapitals = {"up": "lucknow", "mp": "bhopal", "bihar": "patna"}
print(statescapitals)
while True:
    print("0 exit", "1 search", "3 create","4 all","5 delete")
    value = int(input("value=\n"))
    if value == 0:
        print("bye")
        break
    elif value == 1:
        print("search")
        statename = input("enter state=\n")
        state = statescapitals.get(statename)
        print(state)
    elif value == 3:
        print("create")
        state = input("enter state\n")
        capital = input("enter capital\n")
        statescapitals[state] = capital
    elif value == 4:
        print(statescapitals)
    elif value == 5:
        print("delete")
        state = input("enter state")
        delete = statescapitals.pop(state)
        print("delete")


#         trsinno:[src,dest]

