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
            temp = temp._next
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
        # n=list._first
        # for i in range(index):
        #     n=n._next
        #     if n==None:
        #         break
        # else:
        #     return n._value
        
    def set(list,index,value):
        n = list.get_node_at_index(index)
        if n==None:
            return
        else: 
            n._value = value
        # n=list._first
        # for i in range(index):
        #     n=n._next
        #     if n==None:
        #         break
        # else:
        #     n._value=value

    def insert(list, index, value):
        new_node = Node(value)

        if index == 0: 
            new_node.next = list._first
            list._first = new_node
            return
            

        # curr_node = list._first
        # index-=1
        # while curr_node != None and index > 0:
        #     curr_node = curr_node._next
        #     index -= 1


        curr_node = list.get_node_at_index(index)

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
        
        # curr_node = list._first
        # prev_node = None
        # while curr_node != None and index > 0:
        #     prev_node = curr_node
        #     curr_node = curr_node._next
        #     index -= 1

        curr_node = list.get_node_at_index(index)
        x = curr_node._previous
        y = curr_node._next
        
        x._next = y
        y._prev = x

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

