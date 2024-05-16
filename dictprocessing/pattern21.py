n = 7
for row in range(1,n+1):
    for col in range(1,n+1):
        # condition =row + col >= n+1
        condition = row + col <= n+1
        if condition:
            print('*',end='')
        else:
            print('',end = "")
    print()