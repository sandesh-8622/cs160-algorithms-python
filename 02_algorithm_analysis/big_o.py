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

# O(log n) --> logarithmic time
# cuts the problem in HALF  each time
# like opening dictionary to the middle, then half again

def binary_search(items, target):
    low = 0
    high = len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return True
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(get_first(numbers))           # O(1)
    print(find_item(numbers, 3))        # O(n)
    print(find_duplicates(numbers))     # O(n^2)
    print(binary_search(numbers, 3))    # O(log n) --> True
    print(binary_search(numbers, 99))   # O(log n) --> False