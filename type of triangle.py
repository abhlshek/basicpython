# a = int(input("Enter a\n"))
# b = int(input("Enter b\n"))
# c = int(input("Enter c\n"))
a, b, c = 1, 29, 30
# if a + b >= c and b + c >= a and c + a >= b:
#     print("correct")
# else:
#     print("false")

if a+b<c or a+c<b or b+c<a:
    print("false")
else:
    print("correct")


