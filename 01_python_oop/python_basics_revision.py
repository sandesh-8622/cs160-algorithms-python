"""
Python Basics Revision
Everything I learned before starting DSA

PRINT AND VARIABLES

    print("hello")          shows something on screen
    name = "Sandesh"        stores a value in a variable
    x = 5                   numbers work too
    x = 10                  overwrites the old value, box only holds one thing

    the = sign means STORE not check
    the == sign means CHECK if equal


MATH OPERATORS

    +    addition
    -    subtraction
    *    multiplication
    /    division      always gives decimal    10 / 2 = 5.0
    //   floor division  whole number only     10 // 2 = 5
    %    remainder     leftover after dividing  10 % 3 = 1

    even numbers always have remainder 0 when divided by 2
    odd numbers always have remainder 1 when divided by 2

    10 % 2 = 0   even
    11 % 2 = 1   odd


IF ELIF ELSE

    if x > 10:
        print("big")
    elif x > 5:
        print("medium")
    else:
        print("small")

    Python checks top to bottom and stops at the first true one
    elif means else if, a second check
    else runs when nothing above was true


FOR LOOPS

    for i in range(5)       gives 0 1 2 3 4      starts from 0
    for i in range(1, 6)    gives 1 2 3 4 5      starts from 1
    for i in range(0, 5)    same as range(5)

    the last number is never included
    range(1, 11) gives 1 to 10, not 11

    i is just a variable name, you can use anything
    for banana in range(5) works the same way

    looping through a list
        for fruit in fruits:
            print(fruit)


WHILE LOOPS

    while keeps going as long as the condition is true
    for loops a fixed number of times
    while loops until something becomes false

    x = 5
    while x > 0:
        print(x)
        x = x - 1

    this prints 5 4 3 2 1
    when x hits 0, the condition x > 0 becomes false and it stops
    always update the variable inside or it loops forever


LISTS

    fruits = ["apple", "banana", "mango"]

    positions start from 0
        fruits[0]   apple
        fruits[1]   banana
        fruits[2]   mango

    len(fruits)         gives 3, how many items
    fruits.append("grape")  adds to the end

    looping through a list
        for fruit in fruits:
            print(fruit)


FUNCTIONS

    def creates a blueprint for reusable code
    it does not run until you call it

    def greet(name):
        return "hello " + name

    result = greet("Sandesh")
    print(result)

    parameters are variables that get their value when you call the function

    print inside the function  shows on screen but gives nothing back
    return  sends the value back out so you can store or use it

    def add(x, y):
        print(x + y)    shows 7 but function gives nothing back

    def add(x, y):
        return x + y    gives 7 back so you can store it


DICTIONARIES

    stores key value pairs, like a real dictionary
    word is the key, definition is the value

    person = {"name": "Sandesh", "age": 20}

    person["name"]          gives Sandesh
    person["age"] = 21      updates the value
    len(person)             gives 2

    looping gives you the keys not the values
        for key in person:
            print(key)          prints name, age

    to get values
        for key in person:
            print(person[key])  prints Sandesh, 20


COLON RULE

    every if, elif, else, for, while, def needs a colon at the end
    the code inside needs to be indented
    indented means it belongs to that block

    if x > 0:       colon here
        print(x)    indented, belongs to the if


QUOTES RULE

    'i'   prints the letter i
    i     prints the value stored in the variable i

    always remove quotes when you want the variable value
"""


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

print("=== LIST LOOP ===")
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

print("=== FUNCTION ===")
def greet(name):
    return "hello " + name

print(greet("Sandesh"))

print("=== DICTIONARY ===")
person = {"name": "Sandesh", "age": 20}
for key in person:
    print(key, person[key])