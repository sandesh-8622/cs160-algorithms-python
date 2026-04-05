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
        self.data = data    # the actual value
        self.next = None    # pointer to next node, starts as None

class LinkedList:
    def __init__(self):
        self.head = None    # start of the chain, empty at first

    def append(self, data):
        """Add a new node to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a new node to the front of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete the first node with the given data."""
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        """Return True if data is in the list."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def __str__(self):
        """Print the linked list as a chain."""
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) + " -> None"

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.append(15)
    ll.prepend(1)
    print(ll)
    ll.delete(10)
    print(ll)
    print("Search 5:", ll.search(5))
    print("Search 99:", ll.search(99))