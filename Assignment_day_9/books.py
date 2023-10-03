
class Book:

    def __init__(self, id, title, author, price, rating):
        self._id = id
        self._title = title
        self._author = author
        self._price = price
        self._rating = rating

    def __str__(self):
        return f'Book [Title= {self._title}, Author= {self._author}, Rating= {self._rating}, Price= {self._price}]'

class Library:
    def __init__(self):
        self._last_id=0
        self._books=[]
    
    def _add_book(self, title, author, price, rating):
        self._last_id+=1
        book = Book(self._last_id, title, author, price, rating)
        self._books.append(book)
        return book
    
    def __get__(self, id):
        for book in self._books:
            if book._id == id:
                return book
        return None
    
    def _book_by_id(self, id):
        book = self.__get__(id)
        if book:
            print(book)
        
    def __print_book_list(self, books):
        for book in books:
            print(book)

    def _books_by_author(self, author):
        books = []
        for book in self._books:
            if book._author == author:
                books.append(book)
        self.__print_book_list(books)
    
    def _books_in_rating_range(self, start, end):
        books = []
        for book in self._books:
            if book._rating >= start and book._rating <= end:
                books.append(book)
        self.__print_book_list(books)
    
    def _books_in_price_range(self, start, end):
        books = []
        for book in self._books:
            if book._price >= start and book._price <= end:
                books.append(book)
        self.__print_book_list(books)
    
lib = Library()
lib._add_book('Harry Potter', 'J.K. Rowling', 1200, 8.2)
lib._add_book('Harry Potter: prisoner of azkaban', 'J.K. Rowling', 1500, 8.7)
lib._add_book('some random book', 'some random author', 800, 7.3)

# lib._book_by_id(1)
# lib._books_by_author('J.K. Rowling')
# lib._books_in_price_range(1000, 2000)
lib._books_in_rating_range(7, 8.5)




