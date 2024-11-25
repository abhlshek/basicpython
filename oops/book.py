class Book:
    def __init__(self,bookname,subject,price) -> None:
        print("Constructor")
        self.bookname=bookname
        self.subject=subject
        self.price=price
    def __str__(self) -> str:
        return "Book Name= {0},book subject={1},book price={2}".format(self.bookname,self.subject,self.price)

        # return self.bookname + self.subject + str(self.price)


b=Book("Basic C","C",100)
print(b)

c=Book("basic java","java",200)
print(c)



class Bank:
    def __init__(self):
        print("Constructor")
        self.name=input("enter name")
        self.city=input("enter city")
        self.phoneno=input("enter phone number")
    def __str__(self):
        return "costomer name{0},bank city{1},bank phoneno{2}".format(self.name,self.city,self.phoneno)
    
a=Bank()
b=Bank()




