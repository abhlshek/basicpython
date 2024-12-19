class Collage:
    def __init__(self, collagename, code, address):
        self.collagename = collagename
        self.code = code
        self.address = address

    def __str__(self):
        return "collagename={0},code={1},address{2}".format(self.collagename, self.address, self.code)


class Student:
    def __init__(self, name, course, fee):
        self.name = name
        self.course = course

        self.fee = fee

    def __str__(self):
        return "name={0},course={1},fee={2}".format(self.name, self.fee, self.course)


class Teacher(Collage, Student):
    def __init__(self, collagename, code, address, name, course, fee, subject):
        Collage.__init__(self, collagename, code, address)
        Student.__init__(self, name, course, fee)
        self.subject = subject

    def __str__(self):
        return "{1} {2} subject={0}".format(self.subject, Collage.__str__(self), Student.__str__(self))
        # return "{1} {2} subject{0}".format(self.subject, Collage.__str__(self), Student.__str__(self))


t1 = Collage("hpcg", "112", "varansi")
t2 = Student("rahul", "bca", "12200")
t3 = Teacher("t.n", 113, "Ghazipur", "rohit", "mca", 20000, "datascince")
print(t1)
print(t2)
print(t3)
