"""
Stack - Last in, First Out(LIFO) data structure
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()