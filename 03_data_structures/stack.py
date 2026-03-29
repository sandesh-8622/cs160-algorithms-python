"""
WHAT I LEARNED FOR THE DSA CLASS TODAY:

class = a blueprint. Like Apple's blueprint for the iphone.
s = Stack() = the actual object built from that blueprint.

__init__ = runs automatically when you biold a new Stack.
            like a new iphone automatically comming up with empty storage.

self = refers to THIS specific object, not any oter.
        s1 = Stack() and s2 = Stack() are seprate, self keeps them separate.

self.items = [] = this Stack's own empty pile of plates. Starts as empty

push() = adds item ot the Top of the stack.
pop()  = removes item from the  TOP of the stack.
peek() = looks at the TOP item without removing it.
is_empty() = checks if the stack has no items. Returns True or False.
size() = counts how many items are in the stack.
len() = built in Python function tht counts items in a list.
len() = built in Python function that counts items in a list.
        len([10, 20, 30]) = 3, lens([]) = 0
        
__init__ = runs automatically when you build a  
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
    s.push(5)
    s.push(15)
    s.push(25)
    print(s.pop()) # 25
    print(s.peek())  # 15
    print(s.size()) # 2