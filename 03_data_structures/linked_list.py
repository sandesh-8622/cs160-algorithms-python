"""
linked list is a chain of Nodes
Each Node has data and a pointer to the next Node.
[data|next] -> [data|next] -> [data|None]
                                    ^
                                    |
                                    |
                            end of the list
"""

class Node:
    def __init__(self, data):
        self.data = data    # this is the actual value
        self.next = None # pointer to next node, starts as None
class LinkedList:
    def __init__(self):
        self.head = None   # this is start of the chain, which is empty at first
    
    def append(self, data):
        """ Add a new node to the end of the list."""
        new_node = Node(data)   # create a new node
        
        if self.head is None:    # if the list is empty
            self.head = new_node   # new node becomes the head
            return
        
        current = self.head   # start at the beginning
        while current.next:    # until the last node
            current = current.next  # move to next node
        current.next = new_node  # attach a new node at the end