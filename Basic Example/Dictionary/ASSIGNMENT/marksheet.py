result = {10: ["mahesh", 10, 20, 40], 11: ["dhoni", 40, 50, 60], 12: ["raju", 60, 70, 80, 90], 13: ["ranu", 30, 66, 88]}
roll = int(input('enter roll num'))
search = result.get(roll)
print(search)
if search is None:
    print("not found")
else:
    total = search[1] + search[2] + search[3]
    print(total)
    per = total / 3
    print(per)
    if per >= 60:
        print("first")
    elif per >= 50:
        print("second")
    elif per >= 40:
        print("third")
    else:
        print("fail")
