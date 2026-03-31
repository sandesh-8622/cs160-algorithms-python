"""
Deque means --> Double Ended Queue

you can add and remove from the BOTH Ends
Like a deck of cards - add or remove from top or bottom

add_front() = add to the front
add_rear() = add to the back
remove_front() = remove from the front
remove_rear() = remove from the back

Deque pronounced as (deck) --> is Stack + Queue combined. 
Most flexible of the three.
"""

class Deque:
    def __init__(self):
        self.items = []    # empty deque, nothing in it yet not 0(the most important)
    
    def add_front(self, item):
        """Add item to the front of the deque."""
        self.items.insert(0, item)  # this line was missing on my error code

    def add_rear(self, item):
        """Add item to the back of the deque"""
        self.items.append(item)   # this line was missing on my error code

    def remove_front(self):
        """Remove and return item from the front."""
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self.items.pop(0)
    
    def remove_rear(self):
        """Remove and return item from the back."""
        if self.is_empty():
            raise IndexError("remove from empty deque")
        return self.items.pop()
    
    def is_empty(self):
        """Return True if deque has no items."""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items in the deque."""
        return len(self.items)
    
    def __str__(self):
        return f"Deque (front -> back): {self.items}"
    
if __name__ == "__main__":
        d = Deque()

        print("Empty?", d.is_empty())  # True

        d.add_rear("bob")
        d.add_rear("charlie")
        d.add_front("alice")
        print(d)

        print("Remove front:", d.remove_front())  # alice
        print("Remove rear:", d.remove_rear())  # charlie
        print(d)  # ['bob']
        print("size", d.size())  # 1