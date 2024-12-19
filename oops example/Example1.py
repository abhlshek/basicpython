class Book:
    def __init__(self, book, subject, price):
        self.book = book
        self.subject = subject
        self.price = price

    def __str__(self):
        return "bookname={0},subject={1},price{2}".format(self.book, self.subject, self.price)

    a = bookname = ("python", "django", "100")
    print(a)
