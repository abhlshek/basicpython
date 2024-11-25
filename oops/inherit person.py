# inheritance................................

class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def __str__(self):
        return "name {0},age {1},address {2}".format(self.name,self.age,self.address)

class Employee(Person):
    def __init__(self,name,age,address,post,salary):
        Person.__init__(self,name,age,address)
        self.post=post
        self.salary=salary
    def __str__(self):
        return "{2} post{0},salary{1}".format(self.post,self.salary,Person.__str__(self))
    
class Manager(Employee):
    def __init__(self,name,age,address,post,salary,secretary,department):
        Employee.__init__(self,name,age,address,post,salary)
        self.secretary=secretary
        self.department=department
    def __str__(self):
        return "{2} secretary{0},departmen{1}".format(self.secretary,self.department,Employee.__str__(self))
        

    
x=Person("Dhoni",38,"Varanasi")
print(x)
y=Employee('MS Dhoni',40,"Ranchi","developer",350)
print(y)

z=Manager("Sachin",35,"mumbai","web developer",500,y,"software developer")
print(z)