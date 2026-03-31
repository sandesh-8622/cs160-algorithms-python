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