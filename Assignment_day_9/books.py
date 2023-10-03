
class Book:

    def __init__(self, id, title, author, price, rating):
        self._id = id
        self._title = title
        self._author = author
        self._price = price
        self._rating = rating
        self._next = None
        self._previous = None

    def __str__(self):
        return f'Book [Title= {self._title}, Author= {self._author}, Rating= {self._rating}, Price= {self._price}]'

class BookList:
    def __init__(self):
        self._first=None
        self._last = None
    
    def _append(self, book):
        if self._last == None:
            self._first = book
            self._last = self._first
        else:
            self._last._next = book
            book._previous = self._last
            self._last = book
        
    def __getitem__(self, id):
        ptr = self._first
        while ptr:
            if ptr._id == id:
                return ptr
        raise IndexError(f'ID not found :{id}')
        


class Library:
    def __init__(self):
        self._last_id=0
        self._books = BookList()
    
    def _add_book(self, title, author, price, rating):
        self._last_id+=1
        book = Book(self._last_id, title, author, price, rating)
        self._books._append(book)
    
    def __get__(self, id):
        return self._books[id]
    
    def _book_by_id(self, id):
        book = self.__get__(id)
        if book:
            print(book)
        
    def _books_by_author(self, author):
        books_by_author = BookList()
        book = self._books._first
        while book:
            if book._author == author:
                books_by_author._append(book)
                print(book)
            book = book._next
    
    def _books_in_rating_range(self, start, end):
        books = BookList()
        book = self._books._first
        while book:
            if book._rating >= start and book._rating <= end:
                books._append(book)
                print(book)
            book = book._next

    def _books_in_price_range(self, start, end):
        books = BookList()
        book = self._books._first
        while book:
            if book._price >= start and book._price <= end:
                books._append(book)
                print(book)
            book = book._next
            
    
lib = Library()
lib._add_book('Harry Potter', 'J.K. Rowling', 1200, 8.2)
lib._add_book('Harry Potter: prisoner of azkaban', 'J.K. Rowling', 1500, 8.7)
lib._add_book('some random book', 'some random author', 800, 7.3)

# lib._book_by_id(1)
lib._books_by_author('J.K. Rowling')
# lib._books_in_price_range(1000, 2000)
# lib._books_in_rating_range(7, 8.5)




