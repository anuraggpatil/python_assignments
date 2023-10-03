class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous

class LinkedList:
    def __init__(self):
        self._first=None

    def get_node_at_index(self, index):
        temp = self._first
        for i in range(index):
            if not temp == None:
                temp = temp._next
            else: break
        return temp

    def append(self, value):
        if self._first==None: # list is empty
            self._first=Node(value)
        else: # add to the end of a non-empty list
            n=self._first
            while n._next:
                n=n._next
            n._next=Node(value, previous=n)

    def info(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            str+=f'{n._value}\t'
            n=n._next
        str+=")"
        return str

    def size(self):
        c=0
        n=self._first
        while n:
            c+=1
            n=n._next
        return c
        
    def get(list,index):
        n = list.get_node_at_index(index)
        if n==None:
            return
        else: return n._value
        
    def set(list,index,value):
        n = list.get_node_at_index(index)
        if n==None:
            return
        else: 
            n._value = value

    def insert(list, index, value):
        new_node = Node(value)

        if index == 0: 
            new_node.next = list._first
            list._first = new_node
            return

        curr_node = list.get_node_at_index(index)

        if curr_node == None: return

        x = curr_node._previous
        curr_node._previous = new_node
        new_node._next = x._next
        new_node._previous = x
        x._next = new_node

    def remove(list, index):
        if index == 0:
            temp = list._first
            list._first = list._first._next
            return 

        curr_node = list.get_node_at_index(index)

        if curr_node == None: return

        x = curr_node._previous
        y = curr_node._next
        
        x._next = y
        y._prev = x

    def find_primes(self):
        primes = LinkedList()
        n = self._first
        while n:
            if is_prime(n._value):
                primes.append(n._value)
            n = n._next
        return primes
    
    def find_evens(self):
        evens = LinkedList()
        n = self._first
        while n:
            if n._value%2 == 0:
                evens.append(n._value)
            n = n._next
        return evens


def is_prime(val):
    if val<2: return False
    else:
        i = 2
        while i < val:
            if val%i == 0:
                return False
            i+=1
        return True

l2=LinkedList()
for i in range(5):
    l2.append(i)
    
for i in range(l2.size()):
    l2.set(i, i*10)

print(l2.get(2))

l2.insert(2, 9)

print(l2.info())

l2.remove(3)

print(l2.info())

