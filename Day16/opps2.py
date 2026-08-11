class Book:
    def __init__(self):
        self.title = ""
        self.price = 0

book1 = Book()
book2 = Book()

book1.title = "Python Basics"
book1.price = 450

book2.title = "Java Programming"
book2.price = 550

print(book1.title, book1.price)
print(book2.title, book2.price)
