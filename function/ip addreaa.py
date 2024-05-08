ipaddress = "123.221.1074.99"
problem = ''
parts = ipaddress.split(".")
iscorrect = True
# print(parts)
n = len(parts)
# print(n)
# print(n)
if n != 4:
    problem = "Only 4 parts not " + str(n)
    # print("Here")
    iscorrect = False
else:
    for part in parts:
        # print(part)
        try:
            part = int(part)
            if part < 0 or part > 255:      # ip address  part<0 or part>255:
                problem = "part<0 or part>255  "  + str(part)
                iscorrect = False
                break
            # print("ok")
        except:
            iscorrect = False
            break
            # print("error")
if iscorrect:
    print(ipaddress, "is correct")
else:
    print(ipaddress, "is not correct", problem)
