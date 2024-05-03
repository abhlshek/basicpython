result = {1: ["neeraj", 33, 5, 66], 2: ["saurabh", 55, 66, 67], 3: ["sunil", 44, 55, 66]}
print(result)
i = 1
n = 5
while i < n:
    rolln = int(input("enter the roll"))
    search = result.get(rolln)
    print(i)
    i += 1
    if search is None:
        print("not found")
    else:
        total = search[1] + search[2] + search[3]
        print("total", total)
        per = total / 3
        print("per", per)
        if per >= 60:
            print("first")
        elif per >= 50:
            print("second")
        elif per >= 40:
            print("third")
        else:
            print("fail")
