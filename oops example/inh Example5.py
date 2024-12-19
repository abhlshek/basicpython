class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return "name={0},age={1},address={2}".format(self.name, self.age, self.address)


class Employee(Person):
    def __init__(self, name, age, address, post, salary):
        Person.__init__(self, name, age, address)
        self.post = post
        self.salary = salary

    def __str__(self):
        return "{2}post={0},salary={1}".format(self.post, self.salary, Person.__str__(self))


class Manager(Employee):
    def __init__(self, name, age, address, post, salary, secretary, department):
        Employee.__init__(self, name, age, address, post, salary)
        self.secretary = secretary
        self.department = department

    def __str__(self):
        return "{2} secretary {0},department {1}".format(self.secretary, self.department, Employee.__str__(self))


t2 = Manager("rahul", 66, "bhihar", "peoin", 550, "neeraj", "cs")
print(t2)

t1 = Employee("ccc", 44, "saidpur", "maneger", 34500)
print(t1)
