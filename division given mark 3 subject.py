math = int(input("enter the mark math"))
physic = int(input("enter the mark physic"))
computer = int(input("enter the mark computer"))
total = math + physic + computer
per = total / 3
print("total")
print("per")
if per >= 60:
    print("first division")
elif per >= 50:
    print("second division")
elif per >= 40:
    print("third division")
else:
    print("fail")
