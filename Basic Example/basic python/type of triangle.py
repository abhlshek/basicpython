a = int(input('enter value of a'))
b = int(input('enter value of b'))
c = int(input('enter value of c'))
if a + b >= c and b + c >= a and c + a >= b:
    print('correct')
else:
    print('not correct')
