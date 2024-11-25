class Currency:
    def __init__(self, r, p):
        self.totalpaise = r * 100 + p

    def adjust(self, n):
        if n < 10:
            return "0{0}".format(n)
        return str(n)

    def __str__(self):
        totalpaise = self.totalpaise
        if totalpaise >= 0:
            sign = ""
            print("Positive")
        else:
            sign = "-"
            totalpaise = -totalpaise
            print("Negative")

        r = totalpaise // 100
        r = self.adjust(r)

        p = totalpaise % 100
        p = self.adjust(p)
        return "{2}₹ {0}.{1}".format(r, p, sign)

    def __add__(self, other):
        # return 0
        return Currency(0, self.totalpaise + other.totalpaise)

    def __gt__(self, other):
        return self.totalpaise > other.totalpaise


c1 = Currency(-3, 5)
c2 = Currency(2, 8)
print(c1)
print(c2)
sum = c1 + c2
print("sum", sum)

if c1 > c2:
    print("Greater", c1)
else:
    print(c2)
# for x in c1:
# print(x)
