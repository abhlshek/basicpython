math=int(input('enter marks in math'))
physic=int(input('enter marks in physic'))
hindi=int(input('enter marks in Hindi'))
total=math+physic+hindi
print(total)
per=total/3
print(per)
if per>=60:
    print('first')
elif per >=50:
    print('second')
elif per >= 45:
    print('third')
else:
    print('fail')
