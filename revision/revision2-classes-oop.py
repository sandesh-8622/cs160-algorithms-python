"""
Python Revision 2
Everything learned in the second session

CLASSES AND OBJECTS

    a class is a blueprint
    an object is the actual thing built from that blueprint

    class Dog:                          blueprint called Dog
        def __init__(self, name):       runs automatically when you create a dog
            self.name = name            store name on THIS specific dog

        def bark(self):                 something the dog can DO
            print(self.name + " says woof!")

    dog1 = Dog("Rex")                   build one dog named Rex
    dog2 = Dog("Buddy")                 build another dog named Buddy
    dog1.bark()                         Rex says woof!
    dog2.bark()                         Buddy says woof!

    self means THIS specific object, not any other
    dog1 and dog2 are separate, self keeps their data separate

    properties = what the object IS     stored with self.something = value
    functions  = what the object DOES   defined with def


WHILE LOOPS

    while keeps going as long as the condition is true
    for loops a fixed number of times
    while loops until something becomes false

    x = 5
    while x > 0:
        print(x)
        x = x - 1          prints 5 4 3 2 1

    always update the variable inside or it loops forever
    != means not equal to
    while n != 1 means keep going until n equals 1


ERROR HANDLING

    try and except lets you catch errors instead of crashing

    try:
        x = 10 / 0
    except:
        print("cant divide by zero!")

    try     attempt this code
    except  if something goes wrong, run this instead of crashing

    you can catch specific errors too

    try:
        x = int("hello")
    except ZeroDivisionError:
        print("cant divide by zero!")
    except ValueError:
        print("wrong value!")

    ZeroDivisionError   you divided by zero, impossible in math too
    ValueError          wrong type of value, like converting "hello" to a number

    int() converts something to a number
        int("123")      works, gives 123
        int("hello")    ValueError, hello can never be a number


F-STRINGS

    f-strings are a cleaner way to put variables inside strings

    name = "Sandesh"
    score = 100

    print(f"{name} scored {score} points!")     clean way
    print(name + " scored " + str(score))       messy way

    both do the same thing, f-strings are just easier to read
    put f before the quote, put variables inside {}


STRING METHODS

    things you can DO to a string

    name = "Sandesh"

    name.upper()                    SANDESH, all caps
    name.lower()                    sandesh, all lowercase
    name.replace("Sandesh", "John") John, replaces text
    name.split(" ")                 splits into a list by space
    len(name)                       7, number of characters

    note: len() is a function not a method, no dot needed


RECURSION

    a function that calls itself
    two rules every recursive function needs

    rule 1  base case, when to STOP, without this it runs forever
    rule 2  recursive case, call yourself with a smaller problem

    def countdown(n):
        if n == 0:          base case, stop here
            return
        print(n)
        countdown(n - 1)    call yourself with smaller number

    countdown(3) prints 3 2 1 then stops

    iterative vs recursive
        iterative means using a loop to repeat something
        recursive means function calls itself
        both give the same result, just different ways of writing it

    base case is everything, no base case = runs forever


TREES

    data organized like a family tree
    each node can have a left child and a right child only (binary tree)

            10
           /  \\
          5    15
         / \\
        3   7

    root    top node, no parent, that is 10
    leaf    node with no children, that is 3, 7, 15
    child   node below another node

    binary search tree rule
        everything to the LEFT is smaller
        everything to the RIGHT is bigger

    searching in a BST is fast because you always know which way to go
    no need to check every node


MERGE SORT AND BIG O

    merge sort splits the list in half, sorts each half, merges back
    this gives O(n log n) time complexity

    why log n levels
        you keep dividing by 2 until you hit 1 item
        8 items gives 8 then 4 then 2 then 1, that is 3 steps
        log2(8) = 3, so log n levels

    why n log n total
        each level costs n work (you touch every item once)
        there are log n levels
        total = n times log n = O(n log n)

    O(n log n) is much faster than O(n squared) for large lists
"""


print("=== CLASSES ===")
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " says woof!")

dog1 = Dog("Rex")
dog2 = Dog("Buddy")
dog1.bark()
dog2.bark()


print("=== WHILE LOOP ===")
x = 5
while x > 0:
    print(x)
    x = x - 1


print("=== ERROR HANDLING ===")
try:
    x = int("hello")
except ValueError:
    print("wrong value! hello is not a number")


print("=== F-STRING ===")
name = "Sandesh"
score = 100
print(f"{name} scored {score} points!")


print("=== STRING METHODS ===")
word = "sandesh"
print(word.upper())
print(word.replace("sandesh", "shiva"))


print("=== RECURSION ===")
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)