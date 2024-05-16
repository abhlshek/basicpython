n = 5
for row in reversed(range(1,n+1)):
    for space in range(1,n+1-row):
        print(" ",end="")
    for star in range(1,2*row):
        print('*',end="")
    print()


for row in range(1,n+1):
    for space in range(1,n+1-row):
        print(" ",end="")
    for star in range(1,2*row):
        print("*",end="")
    print()
