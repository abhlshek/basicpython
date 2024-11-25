totalpaisa=105
if totalpaisa>=0:
    sign=""
    print("POSITIVE")
else:
    sign="-"
    print("NEGATIVE")
    totalpaisa=-totalpaisa

r=totalpaisa//100
p=totalpaisa%100
print("{2}Rs {0}.{1}".format(r,p,sign))
