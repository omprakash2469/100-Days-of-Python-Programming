class Library:
    def __init__(self):
        self.total_books = 0
        self.books = []
    
    def add_book(self, book_name):
        self.books.append(book_name)
        return "Added Successfully!"
    
    def get_books(self):
        return self.books

    def no_of_books(self):
        return len(self.books)


b1 = Library()

while(True):

    print("""\n1 - Get all books
2 - Add new book 
3 - Exit\n""")
    ch = int(input('Enter choice : '))

    if ch == 1:
        print("Total number of books:", len(b1.get_books()))
        print(b1.get_books())
    elif ch == 2:
        book_name = input("Enter book name: ")
        b1.add_book(book_name)
        print("====== Successfully added new book")
    elif ch == 3:
        print("See you again!")
        break
    else:
        print("Invalid selection")