"""
Exam Prep Revision


THREE LAWS OF RECURSION

Every recursive function must follow these three rules.
If any one is broken, the function either crashes or runs forever.

Law 1   must have a base case
        a stopping condition, the point where it stops calling itself
        without this it runs forever and crashes your program

Law 2   must move toward the base case
        each time it calls itself, it must get closer to stopping
        if it never gets closer, it loops forever

Law 3   must call itself
        otherwise it is just a regular function, not recursive

Example that follows all three laws:

    def foo(a):
        if a <= 0:          law 1, base case, stop when a hits 0 or below
            return a + 2
        return foo(a - 3)   law 2 and 3, calls itself with a smaller number

Tracing foo(23):
    foo(23) calls foo(20)
    foo(20) calls foo(17)
    foo(17) calls foo(14)
    foo(14) calls foo(11)
    foo(11) calls foo(8)
    foo(8)  calls foo(5)
    foo(5)  calls foo(2)
    foo(2)  calls foo(-1)
    foo(-1) hits the base case, a <= 0 is true
    returns -1 + 2 = 1

    so foo(23) = 1

How to trace any recursive function:
    start with the input
    apply the recursive step each time
    stop when you hit the base case
    calculate the return value and work backwards


HASHING AND QUADRATIC PROBING

A hash table stores values using a hash function to find the slot.
Think of school lockers. You calculate which locker to use, you do not search.

Hash function:
    slot = value % table_size

Example with table size 20:
    27 % 20 = 7     so 27 goes in slot 7
    89 % 20 = 9     so 89 goes in slot 9
    2  % 20 = 2     so 2 goes in slot 2
    if the number is smaller than table size, the remainder is just the number

Collision:
    when two values map to the same slot
    46 % 20 = 6, but slot 6 is already taken by 26
    you need to find the next available slot

Linear probing:
    move one slot at a time until you find an empty one
    slot 6 taken, try 7, try 8, try 9...
    problem: creates clustering, everything bunches together

Quadratic probing:
    jump by square numbers instead of moving one by one
    this spreads things out and reduces clustering
    jump distances: 1 squared = 1, 2 squared = 4, 3 squared = 9, 4 squared = 16

Example, 46 lands on slot 6 but it is taken:
    start at 6
    jump 1 squared = 1, try slot 6 + 1 = 7, taken by 27
    jump 2 squared = 4, try slot 6 + 4 = 10, empty, put 46 here

Example, 9 lands on slot 9 but it is taken by 89:
    start at 9
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
    46 % 20 = 6     collision! slot 6 taken, jump to slot 10
    9  % 20 = 9     collision! slot 9 taken, jump to 10, taken, jump to 13, taken, jump to 18
    63 % 20 = 3     slot 3


INHERITANCE

One class can inherit from another.
The child class gets everything the parent class has.

Why it matters:
    if Dog and Cat both eat and sleep, you do not write that code twice
    write it once in Animal, let Dog and Cat inherit it

Example:

    class Animal:
        def __init__(self, name):
            self.name = name

        def eat(self):
            print(self.name + " is eating")

        def sleep(self):
            print(self.name + " is sleeping")

    class Dog(Animal):          Dog inherits from Animal
        def bark(self):
            print(self.name + " says woof!")

    class Cat(Animal):          Cat inherits from Animal
        def meow(self):
            print(self.name + " says meow!")

    my_dog = Dog("Rex")
    my_dog.eat()            Rex is eating, inherited from Animal
    my_dog.bark()           Rex says woof!, Dog's own method

    my_cat = Cat("Whiskers")
    my_cat.sleep()          Whiskers is sleeping, inherited from Animal
    my_cat.meow()           Whiskers says meow!, Cat's own method

Dog(Animal) means Dog inherits from Animal.
Dog gets eat() and sleep() for free without writing them again.
Dog can also have its own methods like bark() that Animal does not have.


STRING METHODS

Things you can do to a string using dot notation.

    word = "Sandesh"

    word.upper()                        SANDESH, all caps
    word.lower()                        sandesh, all lowercase
    word.replace("Sandesh", "Alex")     Alex, replaces the first with the second
    word.split(" ")                     splits into a list at each space

Note: len() is not a string method, it is a standalone function.
    len(word)       correct
    word.len()      wrong, this does not exist

Replace takes two arguments:
    first    what to find
    second   what to replace it with

    sentence = "I love cats"
    sentence.replace("cats", "dogs")    gives "I love dogs"

Split turns a string into a list:
    sentence = "hello world"
    sentence.split(" ")                 gives ["hello", "world"]
    len(sentence.split(" "))            gives 2, two words in the list


LIST METHODS

Things you can do to a list.

    nums = [3, 1, 2]

    nums.append(4)      adds 4 to the end           [3, 1, 2, 4]
    nums.sort()         sorts smallest to biggest   [1, 2, 3, 4]
    nums.reverse()      flips the order             [4, 3, 2, 1]
    nums.remove(3)      removes the value 3         [1, 2, 4]
    nums.pop()          removes the last item       [1, 2]
    len(nums)           count how many items        2

The difference between pop and remove:
    pop()       removes the last item, no argument needed
    pop(0)      removes the first item, you give it an index
    remove(x)   removes a specific value, you give it the value

    nums = [1, 2, 3, 4, 5]
    nums.pop()          removes 5, list is now [1, 2, 3, 4]
    nums.remove(3)      removes 3, list is now [1, 2, 4]

sort() vs reverse():
    sort()      organizes by value, smallest first
    reverse()   just flips whatever order it is in, no sorting

    nums = [3, 1, 2]
    nums.sort()         [1, 2, 3]
    nums.reverse()      [3, 2, 1]   flips the sorted result


ERROR HANDLING

try and except lets you catch errors instead of crashing.

    try:
        x = 10 / 0
    except:
        print("something went wrong")

try     attempt this
except  if it fails, do this instead of crashing

Specific errors:
    ZeroDivisionError   dividing by zero
    ValueError          wrong type of value, like converting "hello" to a number

    try:
        x = int("hello")
    except ZeroDivisionError:
        print("cant divide by zero")
    except ValueError:
        print("wrong value")

When you have multiple except blocks, Python runs the first one that matches.
In the example above, int("hello") causes a ValueError so that block runs.
The ZeroDivisionError block is skipped because that is not what happened.

int() converts something to a number:
    int("123")      works, gives 123
    int("45")       works, gives 45
    int("hello")    ValueError, hello can never be a number
"""


print("=== RECURSION TRACE ===")
def foo(a):
    if a <= 0:
        return a + 2
    return foo(a - 3)

print(foo(23))      # 1
print(foo(24))      # 0


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


print("=== STRING METHODS ===")
word = "Sandesh"
print(word.upper())
print(word.lower())
print(word.replace("Sandesh", "Alex"))
sentence = "hello world"
print(sentence.split(" "))


print("=== LIST METHODS ===")
nums = [3, 1, 2, 5, 4]
nums.sort()
print(nums)
nums.reverse()
print(nums)
nums.pop()
print(nums)
nums.remove(3)
print(nums)


print("=== ERROR HANDLING ===")
try:
    x = int("hello")
except ValueError:
    print("wrong value, hello is not a number")

try:
    y = 10 / 0
except ZeroDivisionError:
    print("cant divide by zero")