"""
Queue - First in, First Out(FIFO) data structure
Think of it like a McDonald's line:
-First person in line gets served first
- New people join at the BACK
- people leave from the FRONT
- First In First Out (FIFO)

Real world examples:
-Mc Donald's line
-Printer queue (first document sent = first printed)
-Customer service calls (first caller = first served)

self.items = [] = the empty line, nobody in it yet"""

class Queue:
    def __init__(self):
        self.items = []   # empty line, nobody in it yet

    def enqueue(self, item):
        """Add item to the BACK of the queue (join the line)."""
        self.items.append(item) # this is an error i had to fix

    def dequeue(self):
        """Remove and return item from the FRONT (first person served)"""
        if self.is_empty():
            raise IndexError("dequeue from empty quueue")
        return self.items.pop(0)
    
    def peek(self):
        """Look at the front item without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]
    
    def is_empty(self):
        """Return True if queue has no items."""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items in the queue."""
        return len(self.items)
    
    def __str__(self):
        return f"Queue(front -> back): {self.items}"
    
if __name__ == "__main__":
    q = Queue()

    print("Empty?", q.is_empty()) # True

    q.enqueue("allice")
    q.enqueue("bob")
    q.enqueue("charlie")
    print(q) # Queue (front -> back): ['alice', 'bob']

    print("peek:", q.peek()) # alice
    print("Dequeue:", q.dequeue()) # alice
    print(q) # Queue (front ->back):['bob', 'charlie']
    print("Size:", q.size()) # 2
