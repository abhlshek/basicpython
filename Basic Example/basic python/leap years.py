year=int(input("enter the year"))
if year%400==0 and year%4==0 and year%100==0:
    print("leapyear")
else:
    print("not leapyear")