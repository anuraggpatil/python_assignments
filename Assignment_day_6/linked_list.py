
class Node():
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head_node = Node(None)
    
    def create_linkedlist(self, *args):
        temp_node = Node(None)
        for value in args:
            new_node = Node(value)
            if self.head_node.val == None:
                self.head_node = new_node
                temp_node = self.head_node
            else:
                temp_node.next = new_node
                temp_node = temp_node.next

    def print_ll(self):
        curr_node = self.head_node
        while curr_node != None:
            print(f'{curr_node.val}', end=' ')
            curr_node = curr_node.next
        print()
    
    def insert(self, value, position):
        new_node = Node(value)

        if position == 1: 
            new_node.next = self.head_node
            self.head_node = new_node
            return
            

        curr_node = self.head_node
        prev_node = Node(None)
        position -= 1
        while curr_node != None and position > 0:
            prev_node = curr_node
            curr_node = curr_node.next
            position -= 1
        
        if curr_node == None and position > 0:
            print('Enter a valid position')
            return
        
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def get(self, position):
        if position == 1:
            return self.head_node.val

        position -= 1
        curr_node = self.head_node
        while position>0 and curr_node.next!=None:
            curr_node = curr_node.next
            position -= 1
        
        return curr_node.val
    
    def set(self, value, position):
        if position == 1:
            self.head_node.val = value
            return
        
        position -= 1;
        curr_node = self.head_node
        while position>0 and curr_node.next != None:
            curr_node = curr_node.next
            position -= 1
        
        curr_node.val = value
        
    def remove(self, position):
        if position == 1:
            temp = self.head_node
            self.head_node = self.head_node.next
            return temp.val
        
        curr_node = self.head_node
        prev_node = Node(None)
        position -= 1
        while curr_node != None and position > 0:
            prev_node = curr_node
            curr_node = curr_node.next
            position -= 1
        
        if curr_node == None and position > 0:
            print('Enter a valid position')
            return
        
        prev_node.next = curr_node.next
        curr_node.next = None
        return curr_node.val
    
    def clear(self):
        self.head_node.val = None
        self.head_node.next = None

l1 = LinkedList()
l1.create_linkedlist(3, 2, 5, 1, 4, 6, 9, 8)

# l1.print_ll()

# l1.insert(15, 10)

# l1.print_ll()

# print(l1.get(8))

# l1.set(20, 3)

# l1.remove(1)

# l1.clear()

# l1.print_ll()





