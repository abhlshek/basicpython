class Book:
    def __init__(self,bookname,subject,price) -> None:
        print("Constructor")
        self.bookname=bookname
        self.subject=subject
        self.price=price
        
    def __str__(self) -> str:
        return "I am book"
    


b=Book("Basic C","C",100)
print(b)
c=Book("subject java","java",200)
print(c)