"""

Big O notation - meansuring algorithm spped

O(1) -->  constant time
O(log n) -->  logarithmic time
O(n) --> linear time
O(n log n) -->  linerathmic time
O(n^2) -->  quadratic time

Rule: we always care about the WORST CASE
"""

# O(1) - constant time
# no matter how big the list, always same speed
def get_first(items):
    return items[0]

# O(n) - linear time
# speed grows with input size
def find_item(items, target):
    for item in items:
        if item == target:
            return True
    return False

# O(n^2) - quadratic time
# loop inside a loop
def find_duplicates(items):
    for i in range(len(items)):
        for j in range(len(items)):
            if i != j and items[i] == items[j]:
                return True
    return False

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(get_first(numbers))           # O(1)
    print(find_item(numbers, 3))        # O(n)
    print(find_duplicates(numbers))     # O(n^2)