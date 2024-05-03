# a = [16, 1, 9, 70]
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
#
# a = ["cat","dog","ball","apple"]
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

# a = ["cat","dog","ball","apple"]
# sortedarray = sorted(a)
# print("original array",a)
# print("sorted array",sortedarray)
# reversesortedarray = sorted(a,reverse=True)
# print("reverse sorted array",reversesortedarray)

a = ["cat","dog","ball","apple"]
# a.sort(key=len)
# print(a)
# a.sort(key=len,reverse=True)
# print(a)


# making oue own function                ???????

# def lastChar(s):
# return s[0]                     #first sort
# return s[len(s)-1]                # last sort
# a.sort(key=lastChar)
# print(a)

# using lambda

# a.sort(key=lambda x:x[len(x)-1],reverse=True)
# print(a)

# using the cmp funtion


# import functools as ft

# a< b -ve,  a=b 0, a>b +ve
def mycompare(a, b):
    if a%2!=0:
        return -1
    if a%2==0:
        return 1
    return 0

# return 0
# return b - a


# a = [1, 2, 3, 4, 5, 6]
# a.sort(key=ft.cmp_to_key(mycompare))
# print(a)

# positive ,negative,equal


# import functools as ft
# def mycompare(b,a):
#     if a%2==0:
#         return 1
#     if a%2!=0:
#         return -1
#     return 0
#
#
# a = [1,2,3,4,5,6]
# a.sort(key=ft.cmp_to_key(mycompare ))
# print(a)


#  the same thing using lembda

# import functools as ft
#
#
# def mycompare(a, b):
#     return b - a
#
#
# a = [1, 2, 3, 4, 5, 6]
# a.sort(key=ft.cmp_to_key(lambda a, b: a - b))
# print(a)
#
# generate a random array and sort it.
#
# from numpy import random
#
# a = list(random.randint(100, size=10))
# a.sort(key=ft.cmp_to_key(lambda a, b: a - b))
# print(a)
#
# another way of doing the same thing

# a = [random.randint(100) for x in range(10)]
# a.sort(key=ft.cmp_to_key(lambda a, b: a - b))
# print(a)
