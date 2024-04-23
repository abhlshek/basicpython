upper = 100
lower = 1
maxprime = 0
print("prime number between", lower, "and", upper, "are")
for num in range(upper, lower - 1, -1):
    if maxprime != 0:
        break
    if num > 1:
        for i in range(2, num):
            if maxprime != 0:
                break
            if (num % i) == 0:
                # maxprime = num
                break
        else:
            maxprime=num
        # print(num)

print(maxprime)
