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


class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous
        
class LinkedList:
    def __init__(self, *args):
        self._first=None
        self._last = None
        self.append(*args)

    def append(self, *args):
        for value in args:
            self._append(value)


    def _append(self, value):
        if not isinstance(value, Book):
            value = Node(value)
        if self._first == None:
            self._first = value
            self._last = self._first
        else:
            self._last._next = value
            value._previous = self._last
            self._last = value

    #def info(self):
    def __str__(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            if isinstance(n, Node):
                str+=f'{n._value}\t'
            else:
                str+=f'{n._title}\t'
            n=n._next
        str+=")"
        return str

    #def size(self):
    def __len__(self):
        c=0
        n=self._first
        while n:
            c+=1
            n=n._next
        return c

    def __contains__(self, item):
        ptr = self._first
        while ptr:
            if ptr._value == item:
                return True
            ptr = ptr._next
        return False

    def __locate(self,index):
        if index>=len(self):
            raise IndexError(f'Invalid Index :{index}')
        
        n=self._first
        for i in range(index):
            n=n._next
            
        return n


             
    #def get(self,index):
    def __getitem__(self,index):
        n=self.__locate(index)
        return n._value  #if n else None
    

    #def set(self,index,value):
    def __setitem__(self,index,value):
        n=self.__locate(index)
        n._value=value

    def insert(self, index, value):
        y=self.__locate(index)
        x=y._previous 
        if not isinstance(value, Book):
            value=Node(value,previous=x,next=y)
        
        if x:
            x._next=value
        else:
            self._first=value

        y._previous=value

    def remove(self, index):
        n=self.__locate(index)

        if self._first == self._last:
            self._first = None
            self._last = None
            return n._value
        
        x= n._previous
        y= n._next

        if x:
            x._next=y
        else:
            self._first=y

        if y:
            y._previous=x
        else:
            self._last = self._last._previous
            self._last._next = None
        return n._value
    
    def count(self, element):
        count = 0
        ptr = self._first
        while ptr:
            if ptr._value == element: count+=1
            ptr = ptr._next
        return count
    
    
    def find_primes(self):
        primes = LinkedList()
        n = self._first
        while n:
            if isinstance(n, Node) and is_prime(n._value):
                primes.append(n._value)
            n = n._next
        return primes
    
    def find_evens(self):
        evens = LinkedList()
        n = self._first
        while n:
            if isinstance(n, Node) and n._value%2 == 0:
                evens.append(n._value)
            n = n._next
        return evens
    
    def _book_by_id(self, id):
        ptr = self._first
        while ptr:
            if isinstance(ptr, Book) and ptr._id == id:
                return ptr
            ptr = ptr._next
        return None
    
    def _books_by_author(self, author):
        books = LinkedList()
        ptr = self._first
        while ptr:
            if isinstance(ptr, Book) and ptr._author == author:
                new_book = Book(ptr._id, ptr._title, ptr._author, ptr._price, ptr._rating)
                books.append(new_book)
            ptr = ptr._next
        return books

    def _books_in_rating_range(self, min, max):
        books = LinkedList()
        ptr = self._first
        while ptr:
            if isinstance(ptr, Book) and ptr._rating>= min and ptr._rating<= max:
                new_book = Book(ptr._id, ptr._title, ptr._author, ptr._price, ptr._rating)
                books.append(new_book)
            ptr = ptr._next
        return books

    def _books_in_price_range(self, min, max):
        books = LinkedList()
        ptr = self._first
        while ptr:
            if isinstance(ptr, Book) and ptr._price>= min and ptr._price<= max:
                new_book = Book(ptr._id, ptr._title, ptr._author, ptr._price, ptr._rating)
                books.append(new_book)
            ptr = ptr._next
        return books

def is_prime(val):
    if val<2: return False
    else:
        i = 2
        while i < val:
            if val%i == 0:
                return False
            i+=1
        return True
    
book1 = Book(12, 'harry', 'jk rowling', 1200, 8.2)
list = LinkedList(2, 3, book1, 1, 4)
print(list)
even = list.find_evens()
print(even)
print(list._book_by_id(12))

book2 = Book(54, 'Harry Potter', 'J.K. Rowling', 1200, 8.2)
book3 = Book(10, 'Harry Potter: prisoner of azkaban', 'J.K. Rowling', 1500, 8.7)
book4 = Book(99, 'some random book', 'some random author', 800, 7.3)

list.append(12, book4, 7, book3, book2, 9, 5)

print(list)


books = list._books_in_rating_range(7, 8)
print(books)

    