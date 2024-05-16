n = 6
for row in range(1,n+1):
    for col in range(1,n+1):
        condition = col ==1 or row == col or col == n
        if condition:
            print("*",end="")
        else:
            print(" ",end="")
    print()