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

