"""
Exam Prep Revision
Topics covered in exam practice sessions


THREE LAWS OF RECURSION

Every recursive function must follow these three rules.
Break any one and it either runs forever or crashes.

Law 1   must have a base case
        the stopping condition
        without this the function runs forever

Law 2   must move toward the base case
        each call must get closer to stopping
        if it never gets closer it loops forever

Law 3   must call itself
        otherwise it is just a regular function

Example:

    def foo(a):
        if a <= 0:          law 1, base case
            return a + 2
        return foo(a - 3)   law 2 and 3, calls itself with smaller number

Tracing foo(23):
    starts at 23
    23, 20, 17, 14, 11, 8, 5, 2, -1
    -1 hits the base case because -1 <= 0
    returns -1 + 2 = 1
    so foo(23) = 1

Tracing foo(24):
    24, 21, 18, 15, 12, 9, 6, 3, 0
    0 hits the base case because 0 <= 0
    returns 0 + 2 = 2
    so foo(24) = 2

foo does NOT violate any laws because:
    it has a base case          if a <= 0
    it moves toward it          subtracts 3 each time
    it calls itself             foo(a - 3)


HASHING AND QUADRATIC PROBING

A hash table stores values using a hash function to find the slot.
Think of school lockers. You calculate the locker number, you do not search.

Hash function:
    slot = value % table_size

Example with table size 20:
    27 % 20 = 7     slot 7
    89 % 20 = 9     slot 9
    93 % 20 = 13    slot 13
    2  % 20 = 2     slot 2, if number is smaller than table size remainder is the number itself

Collision happens when two values map to the same slot.
    26 % 20 = 6
    46 % 20 = 6     collision! slot 6 already taken

Linear probing:
    move one slot at a time until you find an empty one
    problem: creates clustering, everything bunches together

Quadratic probing:
    jump by square numbers to spread things out
    1 squared = 1
    2 squared = 4
    3 squared = 9
    4 squared = 16

Example, 46 lands on slot 6 but slot 6 is taken by 26:
    jump 1 squared = 1, try slot 6 + 1 = 7, taken by 27
    jump 2 squared = 4, try slot 6 + 4 = 10, empty, put 46 here

Example, 9 lands on slot 9 but slot 9 is taken by 89:
    jump 1 squared = 1, try slot 9 + 1 = 10, taken by 46
    jump 2 squared = 4, try slot 9 + 4 = 13, taken by 93
    jump 3 squared = 9, try slot 9 + 9 = 18, empty, put 9 here

Full example inserting [27, 89, 93, 26, 2, 54, 72, 46, 9, 63] into size 20 table:
    27 % 20 = 7     slot 7
    89 % 20 = 9     slot 9
    93 % 20 = 13    slot 13
    26 % 20 = 6     slot 6
    2  % 20 = 2     slot 2
    54 % 20 = 14    slot 14
    72 % 20 = 12    slot 12
    46 % 20 = 6     collision, jump to slot 10
    9  % 20 = 9     collision, jump to 10, taken, jump to 13, taken, jump to 18
    63 % 20 = 3     slot 3


BINARY SEARCH

Only works on sorted lists.
Always guess the middle. If too high go left. If too low go right.
Like the guessing game where someone says higher or lower.

Example searching for 23 in [10, 20, 23, 29, 42, 58, 60, 62, 67, 72, 74, 77, 89, 95, 98]:

    midpoint is 62
    23 < 62 so throw away right half
    left half is [10, 20, 23, 29, 42, 58, 60]

    midpoint is 29
    23 < 29 so throw away right half
    left half is [10, 20, 23]

    midpoint is 20
    23 > 20 so throw away left half
    right half is [23]

    found 23!

Comparisons made: 62, 29, 20, 23

Big O: O(log n) because you cut the list in half each time
for 1000 items binary search takes at most 10 steps
linear search takes up to 1000 steps


TREE TRAVERSAL

Three ways to visit every node in a tree.
The only difference is when you visit the root.

Easy way to remember:
    PREschool comes BEFORE school, so root comes FIRST
    INorder, root is IN the middle
    POSTman delivers AFTER you order, so root comes LAST

Preorder   root, left, right   root first
Inorder    left, root, right   root middle, gives sorted order on a BST
Postorder  left, right, root   root last

Example tree:
            D
           / \
          B   E
         / \
        A   C

Inorder (left to right):    A B C D E
Preorder (root first):      D B A C E
Postorder (root last):      A C B E D

Secret weapons for exam questions:
    postorder last letter = root
    preorder first letter = root

If you are given inorder and postorder and need to find preorder:
    last letter of postorder = root
    find root in inorder to split left and right sides
    repeat for each subtree


SORTING ALGORITHMS

Insertion Sort
    pick up one number at a time and insert it in the correct position
    like sorting cards in your hand
    Big O: O(n) best case, O(n squared) worst case

    [40, 13, 80, 77, 24]
    step 1: 13 < 40, move 13 before 40        [13, 40, 80, 77, 24]
    step 2: 80 > 40, stays                    [13, 40, 80, 77, 24]
    step 3: 77 < 80, move left, 77 > 40, stop [13, 40, 77, 80, 24]
    step 4: 24 slides all the way to second   [13, 24, 40, 77, 80]

Bubble Sort
    compare two neighbors at a time
    swap if left is bigger than right
    big numbers bubble up to the end each round
    Big O: O(n squared)

    [3, 1, 2]
    compare 3 and 1, swap      [1, 3, 2]
    compare 3 and 2, swap      [1, 2, 3]
    done

Selection Sort
    find the smallest number, put it at the front
    repeat for the rest of the list
    Big O: O(n squared)

    [5, 3, 8, 1]
    smallest is 1, swap with 5     [1, 3, 8, 5]
    smallest is 3, already first   [1, 3, 8, 5]
    smallest is 5, swap with 8     [1, 3, 5, 8]
    done

Merge Sort
    split the list in half repeatedly until single items
    merge the halves back together in sorted order
    Big O: O(n log n) always

    [3, 1, 4, 2]
    split into [3, 1] and [4, 2]
    sort each: [1, 3] and [2, 4]
    merge back: compare front items each time [1, 2, 3, 4]

Quick Sort
    pick a pivot (usually first number)
    put everything smaller to the left
    put everything bigger to the right
    pivot is now in its permanent position
    repeat for left and right sides
    Big O: O(n log n) average

    L = [40, 13, 80, 77, 25, 24, 12, 62, 85, 54]

    pivot = 40
    smaller: [13, 25, 24, 12]
    bigger:  [80, 77, 62, 85, 54]
    result:  [13, 25, 24, 12] [40] [80, 77, 62, 85, 54]
    40 is in permanent place

    now pivot = 80 in right side
    smaller: [77, 62, 54]
    bigger:  [85]
    result:  [13, 25, 24, 12] [40] [77, 62, 54] [80] [85]
    80 is in permanent place

    now pivot = 77 in remaining right side
    smaller: [62, 54]
    bigger:  none
    result:  [13, 25, 24, 12] [40] [62, 54] [77] [80] [85]
    77 is in permanent place

Speed ranking from fastest to slowest:
    O(n)        insertion sort best case
    O(n log n)  merge sort, quicksort, heapsort
    O(n squared) bubble sort, selection sort, insertion sort worst case


INHERITANCE

One class can inherit from another.
The child class gets everything the parent has.

    class Animal:
        def __init__(self, name):
            self.name = name

        def eat(self):
            print(self.name + " is eating")

    class Dog(Animal):
        def bark(self):
            print(self.name + " says woof!")

    my_dog = Dog("Rex")
    my_dog.eat()        Rex is eating, inherited from Animal
    my_dog.bark()       Rex says woof!, Dog's own method

Dog(Animal) means Dog inherits from Animal.
Dog gets eat() for free without writing it again.
"""


print("=== RECURSION ===")
def foo(a):
    if a <= 0:
        return a + 2
    return foo(a - 3)

print(foo(23))      # 1
print(foo(24))      # 2


print("=== BINARY SEARCH ===")
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

nums = [10, 20, 23, 29, 42, 58, 60, 62, 67, 72]
print(binary_search(nums, 23))      # True
print(binary_search(nums, 99))      # False


print("=== SORTING ===")
def bubble_sort(items):
    n = len(items)
    for i in range(n):
        for j in range(n - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

print(bubble_sort([5, 3, 8, 1, 4]))    # [1, 3, 4, 5, 8]


print("=== INHERITANCE ===")
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " is eating")

class Dog(Animal):
    def bark(self):
        print(self.name + " says woof!")

class Cat(Animal):
    def meow(self):
        print(self.name + " says meow!")

my_dog = Dog("Rex")
my_dog.eat()
my_dog.bark()

my_cat = Cat("Whiskers")
my_cat.eat()
my_cat.meow()