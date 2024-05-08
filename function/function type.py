# this function has two parameters


def add(a, b):
    print("a=", a, ",b=", b)


# both are parameters are necessary
# add(9),add(1,2,3) are error

# default value parameters

def d1add(a, b=0):  #b is 0 if not given
    print("a=", a, ",b=", b)


add(1, 2)
d1add(1, 2)
d1add(2)  # b is no


def d2add(a=0, b=0):
    print("a=", a, ",b=", b)


d2add(1, 2)
d2add(1)
d2add()
d2add(b=7)  # using name parameters


def f1(*args):  # pass a tuple as parameters
    print(type(args))
    for x in args:
        print(x, end=",")
    print()


def f2(**args):  # pass a dictionary as parameters
    print(type(args))
    for key in args:
        print(key, "=", args[key], end=",")
    print()


f1(0, 2, 3)
f2(a=1, b=2, c=3)


# return types
# python functions that do,t return value explicitly have none as return value

def r1():  #none as return
    pass


print(r1(), type(r1()))


def r2():
    return 0


print(r2(), type(r2()))


def r3():
    return 1, 2


print(r3(), type(r3()))
