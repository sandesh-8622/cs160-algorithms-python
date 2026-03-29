"""
Stack - Last in, First Out(LIFO) data structure
Think of it like plates piled up:
- You can only add to the top (push)
- You can only remove from the top (pop)
- You can only look at the top (peek)
- Last plate in = first plate out (lifo)
Real world example: Ctrl+z undo button in any software

To understand it very simple manner
self.items = []
is the empty pile of plates before anyone puts anything on it

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
    
    def peek(self):
        """Return top item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Return True if stack has no items."""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items in the stack."""
        return len(self.items)
    
    def __str__(self):
        return f"Stack (top -> bottom): {self.items[::-1]}"
if __name__ == "__main__":
    s = Stack()

    print("Empty?", s.is_empty())  # True, no plates yet

    s.push(10)
    s.push(20)
    s.push(30)
    print(s) # [30,20, 10] --> 30 is on top

    print("Peek:", s.peek())  # 30 --> removed from top
    print("Pop:", s.pop())
    print(s)   # [20, 10] --> 30 is gone