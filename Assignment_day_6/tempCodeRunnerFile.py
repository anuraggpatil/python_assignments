        new_node = Node(value)

        if position == 1: 
            new_node.next = self.head_node
            self.head_node = new_node
            return
            

        curr_node = self.head_node
        prev_node = Node(None)
        position -= 1
        while curr_node.next != None and position > 0:
            prev_node = curr_node
            curr_node = curr_node.next
            position -= 1
        
        if curr_node.next == None and position > 0:
            print('Enter a valid position')
            return
        
        new_node.next = prev_node.next
        prev_node.next = new_node
        


l1 = LinkedList()
l1.create_linkedlist(3, 2, 5, 1, 4, 6, 9, 8)

l1.print_ll()

l1.insert(15, 9)