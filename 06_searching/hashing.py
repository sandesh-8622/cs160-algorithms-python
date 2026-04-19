"""
Hashing --> O(1) lookup using a hash function

Like school lockers:
- Key (student name) --> hash function --> locker number
- Store value at that locker number
- To find it: run same hash and go directly there

Python dicts use hashing internally - that's why they are O(1)
"""

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size  # 10 empty slots

    def hash(self, key):
        """Convert key to a slot number."""
        return len(key) % self.size

    def set(self, key, value):
        """Store key-value pair in the hash table."""
        slot = self.hash(key)
        self.table[slot] = value

    def get(self, key):
        """Get value by key."""
        slot = self.hash(key)
        return self.table[slot]

    def __str__(self):
        return str(self.table)

if __name__ == "__main__":
    ht = HashTable()
    ht.set("alice", 90)
    ht.set("bob", 85)
    ht.set("charlie", 92)
    print(ht.get("alice"))    # 90
    print(ht.get("bob"))      # 85
    print(ht)