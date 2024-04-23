n = int(input("enter n "))
result = "Prime"
limit = int(n ** .5)
# print("Limit ", limit)
r = range(2, limit + 1, 1)

for i in r:
    # print(i)
    if n % i == 0:
        result = "Not prime"
        break

print(result)
