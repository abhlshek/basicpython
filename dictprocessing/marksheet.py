result = {10: ["MS Dhoni", 78, 89, 45], 11: ["virat", 72, 89, 44], 12: ["sachin", 66, 55, 77],
          13: ["sushil", 44, 85, 95]}
print(result)
rolln = int(input("enter the roll"))
search = result.get(rolln)

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
