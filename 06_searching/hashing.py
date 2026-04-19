"""

Hasing --> 0(1) lookup using a hash function

Like school lockers:
- Key (student name) --> hash function --> locker number
- Store value at that locker number
- To find it: run same hash and go directly there

Python dicts use hasing internally and that is hwy they are 0(1)
"""

class HashingTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size # 10 empty slots

        def hash(self, key):
            """convert key to a slot number."""
        return len(key) % self.size