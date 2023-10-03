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
            self._last = self._first
        else: # add to the end of a non-empty list
            new_node =  Node(value)
            self._last._next = new_node
            new_node._previous = self._last
            self._last = new_node

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

    def _get_mid_in_ll(self):
        slow = self._first
        fast = self._first
        while fast and fast._next:
            fast = fast._next
            fast = fast._next
            slow = slow._next
        
        return slow
    
    def _merge(list1, list2):
        merged_list = LinkedList()
        p1 = list1._first
        p2 = list2._first
        while p1 and p2:
            if p1._value<=p2._value:
                merged_list.append(p1._value)
                p1 = p1._next
            else:
                merged_list.append(p2._value)
                p2 = p2._next
        
        if p1:
            merged_list._last._next = p1
            p1._previous = merged_list._last
            merged_list._last = p1
        if p2:
            merged_list._last._next = p2
            p2._previous = merged_list._last
            merged_list._last = p2
        
        return merged_list

    def _merge_sort(self, start, end):
        if start == end:
            l = LinkedList(start._value)
            return l
        
        mid = self._get_mid_in_ll()

        l1 = self._merge_sort(start, mid._previous)
        l2 = self._merge_sort(mid, end)
        return LinkedList._merge(l1, l2)

    def sort(self):
        start = self._first
        end = self._last
        return self._merge_sort(start, end)


list = LinkedList(2, 3, 1, 9, 6, 7)

list2 = LinkedList(3,2)
l3 = list.sort()
# print(l3._first._value, l3._last._value)
# print(l3._get_mid_in_ll()._value)
# print(l3._get_mid_in_ll() == l3._last)

# list2.append(2,3)
ptr = l3._first
while ptr:
    print(ptr._value, end=' ')
    ptr = ptr._next