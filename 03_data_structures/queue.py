"""
Queue - First In, First Out (FIFO) data structure

What I have learned so far:

FIFO = First In First Out
Like a McDonald's line - first person in line gets served first.

enqueue() = add to the BACK of the line (new person joins)
dequeue() = remove from the FRONT of the line (first person served)
peek()    = just LOOK at the front person, they don't leave
is_empty() = is the line empty?
size()    = how many people in the line?

positions in a list start from 0:
["alice", "bob", "charlie"]
    0        1        2

pop(0)    = remove from front (dequeue uses this)
pop()     = remove from back (stack uses this)
items[0]  = look at front without removing (peek uses this)
items[-1] = look at back without removing (stack peek uses this)

---> here when learning difference between Stack and Queue,
Stack = LIFO = plates piled up = remove from TOP
for eg, in stack of plates the last plate that is kept is first out but dont mistak in python code as
1
2
3
4
5
here the stack of plate is 5 not one as it looks as stack of plate but, 
5 because it came at the very last.
Queue = FIFO = McDonald's/coffee counter line = remove from FRONT
for eg, someone who comes to the lines first gets their first turn 
"""

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
