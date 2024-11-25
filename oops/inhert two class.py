class Collage:
    def __init__(self, collagename, code, address):
        self.collagename = collagename
        self.code = code
        self.address = address

    def __str__(self):
        return "collagename{0},code{1},address{2}".format(self.collagename, self.code, self.address)


# class X(Y,Z):
class Student:
    def __init__(self, studentname, course, fee):
        self.studenrname = studentname
        self.course = course
        self.fee = fee

    def __str__(self):
        return "studentname{0},course{1},fee{2}".format(self.studenrname, self.course, self.fee)


class Teacher(Collage, Student):
    def __init__(self, collagename, code, address, studentname, course, fee, subject):
        Collage.__init__(self, collagename, code, address)
        Student.__init__(self, studentname, course, fee)
        self.subject = subject

    def __str__(self):
        return "{1} {2} subject{0}".format(self.subject, Collage.__str__(self), Student.__str__(self))


a = Collage("T.N Inter collage", 2307, "Saidpur")
print(a)
b = Student("Rohit", "MBA", 3500)
print(b)

c = Teacher("Gyn Bharti school", 450, "Ghazipur", "dhoni", "BCA", 2300, "Django")
print(c)
