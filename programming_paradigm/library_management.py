class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def check_out(self):
        self._is_checked_out  = True
    def return_book(self):
        self._is_checked_out = False
    def is_available(self):
        return not self._is_checked_out
    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
        self._books.append(book)
        print(f"Added book: {book}")
    def check_out_book(self,title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.is_available():
                    book.check_out()
                    print(f"Book checked out: {book}")
                    return
                else:
                    print(f"Sorry, '{title}' is already checked out.")
                    return
        print(f"Sorry, '{title}' not found in the library.")
    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if not book.is_available():
                    book.return_book()
                    print(f"Book returned: {book}")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Sorry, '{title}' not found in the library.")
    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"-{book}")
        else:
            print("no books are currently available.")         

