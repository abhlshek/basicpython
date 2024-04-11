yearmonth = int(input("Enter the yearmonth number"))

if yearmonth in (1, 3, 5, 7, 8, 10, 12):
    print(31)
elif yearmonth in (4, 6, 9, 11):
    print(30)
elif yearmonth == 2:
    year = int(input("Enter the year"))
    if (year % 400 == 0) or (year % 4 == 0) and  (year % 100 != 0):
        print(29)
    else:
        print(28)


else:

    print("Error")
