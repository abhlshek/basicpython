# def function(*,x):
#     print(x)
# function(x=3)
#
#
# def function(x):
#     print(x)
# function(x=2)
#
#
# def  function(*,x):
#     print(x)
# function(6)


def function(a,b,/,*,c,d):
    print(a+b+c+d)
function(5,6,c=7,d=8)