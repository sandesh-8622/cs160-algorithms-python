"""
Python Basics Revision
Sandesh Bhandari


PRINT AND VARIABLES

print() shows something on the screen.

    print("hello")          shows: hello
    print(2 + 3)            shows: 5
    print("hello" + "world") shows: helloworld, no space

If you want a space you have to put it in yourself.
    print("hello" + " " + "world")     hello world
    print("hello world")               hello world
Both work the same way.

A variable is a box that stores a value.
    name = "Sandesh"        stores the text Sandesh
    age = 20                stores the number 20
    x = 5                   stores 5

The = sign means store, not check.
    x = 5       put 5 in x
    x == 5      check if x equals 5, these are different things

Variables can be overwritten. The box only holds one thing at a time.
    x = 5
    x = 10
    print(x)    prints 10, the 5 is gone


MATH OPERATORS

    +       addition            5 + 3 = 8
    -       subtraction         5 - 3 = 2
    *       multiplication      5 * 3 = 15
    /       division            10 / 2 = 5.0     always gives a decimal
    //      floor division      10 // 2 = 5      whole number only
    %       remainder           10 % 3 = 1       leftover after dividing
    **      exponent            2 ** 3 = 8

Division always gives a decimal even if the answer is a whole number.
    10 / 2 = 5.0    not 5
    10 // 2 = 5     use this if you want a whole number

The % operator gives the remainder.
    10 % 3 = 1      because 10 divided by 3 is 3 with 1 left over
    10 % 2 = 0      because 10 divides evenly by 2
    11 % 2 = 1      because 11 does not divide evenly by 2

This is how you check if a number is even or odd.
    if num % 2 == 0     even
    if num % 2 == 1     odd


IF ELIF ELSE

Used to make decisions. Python checks conditions top to bottom
and stops at the first one that is true.

    if x > 10:
        print("big")
    elif x > 5:
        print("medium")
    else:
        print("small")

elif means else if. A second check if the first one was false.
else runs when nothing above it was true.

Every if, elif, and else needs a colon at the end.
The code inside needs to be indented.

    if x > 0:       colon here
        print(x)    indented, belongs to the if


COMPARISON OPERATORS

These go inside if statements.

    ==      equal to            x == 5
    !=      not equal to        x != 5
    >       greater than        x > 5
    <       less than           x < 5
    >=      greater or equal    x >= 5
    <=      less or equal       x <= 5


FOR LOOPS

Repeats code a fixed number of times.

    for i in range(5):
        print(i)

    prints: 0 1 2 3 4

range() always starts from 0 unless you tell it otherwise.
The last number is never included.

    range(5)        gives 0 1 2 3 4
    range(1, 6)     gives 1 2 3 4 5
    range(0, 5)     same as range(5)
    range(2, 8)     gives 2 3 4 5 6 7

The variable name does not matter. i is just a habit from old programmers.
    for i in range(5)       works
    for b in range(5)       works the same way
    for banana in range(5)  also works

Quotes vs no quotes inside the loop:
    print('i')      prints the letter i every time
    print(i)        prints the actual number stored in i

You can also loop through a list directly.
    fruits = ["apple", "banana", "mango"]
    for fruit in fruits:
        print(fruit)

    prints apple, then banana, then mango on separate lines


WHILE LOOPS

Repeats as long as a condition is true.
Unlike for loops which repeat a fixed number of times,
while loops keep going until something becomes false.

    x = 5
    while x > 0:
        print(x)
        x = x - 1

    prints: 5 4 3 2 1

Walk through it:
    x = 5, is 5 > 0? yes, print 5, x becomes 4
    x = 4, is 4 > 0? yes, print 4, x becomes 3
    x = 3, is 3 > 0? yes, print 3, x becomes 2
    x = 2, is 2 > 0? yes, print 2, x becomes 1
    x = 1, is 1 > 0? yes, print 1, x becomes 0
    x = 0, is 0 > 0? no, stop

Always update the variable inside the loop or it runs forever.
    != means not equal to
    while n != 1    keep going until n equals 1

Counting up with while:
    x = 1
    while x < 6:
        print(x)
        x = x + 1

    prints: 1 2 3 4 5


LISTS

Stores multiple values in one variable.

    fruits = ["apple", "banana", "mango"]

Positions start from 0.
    fruits[0]   apple
    fruits[1]   banana
    fruits[2]   mango
    fruits[-1]  mango, shortcut for the last item

Useful list operations:
    len(fruits)             gives 3, how many items
    fruits.append("grape")  adds grape to the end
    fruits.pop()            removes and returns the last item
    fruits.pop(0)           removes and returns the first item

Building a list in a loop:
    nums = []
    for i in range(5):
        nums.append(i)
    print(nums)     gives [0, 1, 2, 3, 4]

Adding up all values in a list:
    nums = [1, 2, 3, 4, 5]
    total = 0
    for num in nums:
        total = total + num
    print(total)    gives 15

total starts at 0 because nothing has been added yet.
It is like a scoreboard before the game starts.


FUNCTIONS

A reusable block of code. Writing the function does not run it.
You have to call it separately.

    def greet():
        print("hello!")

    greet()     this actually runs it

Think of it like a recipe. Writing the recipe does not cook the food.
You have to actually cook it.

Functions can take parameters, variables that get their value when called.

    def greet(name):
        print("hello " + name)

    greet("Sandesh")    prints: hello Sandesh
    greet("Alex")       prints: hello Alex

Functions can return values.

    def add(x, y):
        return x + y

    result = add(3, 4)
    print(result)       prints 7

The difference between print inside and return:
    print inside    shows something on screen but gives nothing back
    return          sends the value back so you can store or use it

    def add(x, y):
        print(x + y)        shows 7 on screen, function gives back nothing

    def add(x, y):
        return x + y        gives 7 back so you can store it in a variable

Functions must be defined above the code that calls them.
Always define first, use later.

    def add(x, y):
        return x + y

    if __name__ == "__main__":
        print(add(3, 4))    this works, add is defined above


DICTIONARIES

Stores key value pairs. Like a real dictionary where the word is the key
and the definition is the value.

    person = {
        "name": "Sandesh",
        "age": 20
    }

    person["name"]          gives Sandesh
    person["age"]           gives 20
    person["age"] = 21      updates the value to 21
    len(person)             gives 2

The difference from a list:
    list uses numbers to access items      fruits[0]
    dictionary uses keys to access items   person["name"]

Looping through a dictionary gives you the keys, not the values.
    for key in person:
        print(key)          prints name, then age

To get the values you need one more step.
    for key in person:
        print(person[key])  prints Sandesh, then 20


ERROR HANDLING

Lets you catch errors instead of crashing the program.

    try:
        x = 10 / 0
    except:
        print("cant divide by zero")

try means attempt this code.
except means if something goes wrong, run this instead of crashing.

You can catch specific errors too.

    try:
        x = int("hello")
    except ZeroDivisionError:
        print("cant divide by zero")
    except ValueError:
        print("wrong value")

ZeroDivisionError happens when you divide by zero.
ValueError happens when you give the wrong type of value.

    int("123")      works, gives 123
    int("hello")    ValueError because hello can never be a number

int() converts something to a number.
If it cannot be converted, you get a ValueError.


F-STRINGS

A cleaner way to put variables inside strings.

    name = "Sandesh"
    score = 100

    print(f"{name} scored {score} points")

    prints: Sandesh scored 100 points

Put f before the opening quote. Put variables inside curly braces.
This is cleaner than using + to join strings.

    print(name + " scored " + str(score) + " points")  messy
    print(f"{name} scored {score} points")              clean


STRING METHODS

Things you can do to a string.

    word = "sandesh"

    word.upper()                    SANDESH
    word.lower()                    sandesh
    word.replace("sandesh", "alex") alex
    word.split(" ")                 splits into a list at each space
    len(word)                       7, number of characters

Note: len() is a built in function, not a method.
You write len(word) not word.len().


CLASSES AND OBJECTS

A class is a blueprint. An object is the actual thing built from it.

    class Dog:
        def __init__(self, name):
            self.name = name

        def bark(self):
            print(self.name + " says woof!")

    dog1 = Dog("Rex")
    dog2 = Dog("Buddy")
    dog1.bark()     prints: Rex says woof!
    dog2.bark()     prints: Buddy says woof!

__init__ runs automatically when you create an object.
self refers to this specific object, keeping each one's data separate.

dog1 and dog2 are both Dogs but they have different names.
self is what keeps them from getting mixed up.

Properties are what the object is. Stored with self.something = value.
Methods are what the object can do. Defined with def inside the class.

    self.name = "Rex"       property, the dog's name
    def bark(self):         method, something the dog can do

The if __name__ == "__main__" block:
    this is where you actually run your code
    it always goes outside the class with no indentation
    everything inside it only runs when you run that specific file directly
"""


print("=== MATH ===")
print(10 / 2)
print(10 // 2)
print(10 % 3)

print("=== FOR LOOP ===")
for i in range(1, 6):
    print(i)

print("=== EVEN NUMBERS ===")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

print("=== WHILE LOOP ===")
x = 5
while x > 0:
    print(x)
    x = x - 1

print("=== LIST ===")
nums = [1, 2, 3, 4, 5]
total = 0
for num in nums:
    total = total + num
print(total)

print("=== FUNCTION ===")
def greet(name):
    return "hello " + name

print(greet("Sandesh"))

print("=== DICTIONARY ===")
person = {"name": "Sandesh", "age": 20}
for key in person:
    print(key, person[key])

print("=== ERROR HANDLING ===")
try:
    x = int("hello")
except ValueError:
    print("wrong value, hello is not a number")

print("=== CLASS ===")
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " says woof!")

dog1 = Dog("Rex")
dog2 = Dog("Buddy")
dog1.bark()
dog2.bark()