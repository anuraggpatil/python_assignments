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
        if self._first==None: # list is empty
            self._first=Node(value)
            self._tail = self._first
        else: # add to the end of a non-empty list
            n=self._first
            while n._next:
                n=n._next
            n._next=Node(value, previous=n)
            self._tail = n._next

    #def info(self):
    def __str__(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            str+=f'{n._value}\t'
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

        new_node=Node(value,previous=x,next=y)
        
        if x:
            x._next=new_node
        else:
            self._first=new_node

        y._previous=new_node

    def remove(self, index):
        n=self.__locate(index)
        
        x= n._previous
        y= n._next

        if x:
            x._next=y
        else:
            self._first=y

        if y:
            y._previous=x
        return n._value
    
    def add_to_end(self, val):
        new_node = Node(val)
        if self._tail == None:
            self._first = new_node
            self._tail = self._first
        else:
            self._tail._next = new_node
            new_node._previous = self._tail