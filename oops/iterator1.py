class Table:
    def __init__(self, a):
        self.n = a

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > 10:
            raise StopIteration
        value = self.n * self.i
        return value

    def __getitem__(self, i):
        return i * self.n


t1 = Table(4)
for i in t1:
    print(i)
print(t1[1])
