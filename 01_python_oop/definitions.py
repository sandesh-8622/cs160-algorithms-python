"""
CS160 Definitions/OOP definitions
Sandesh Bhandari


DATA STRUCTURES

A data structure is just a way to organize data.
Different problems need different structures.
Picking the right one makes your code faster and simpler.


Stack

The classic example is a pile of plates in a cafeteria.
You put plates on top. You take plates from the top.
The last plate you put down is the first one you pick up.
That is LIFO. Last In First Out.

Operations:
    push(item)      add to the top
    pop()           remove from the top
    peek()          look at the top without removing it
    is_empty()      returns True if nothing is in there
    size()          how many items are in it

All of these are O(1). Always fast, does not matter how big the stack is.

Real examples:
    Ctrl+Z in any software. Every action you take gets pushed.
    Pressing undo pops the last one off.
    Your browser back button works the same way.
    Python itself uses a stack to track which function called which.

Quick trace:
    s.push(10)      stack: [10]
    s.push(20)      stack: [10, 20]
    s.push(30)      stack: [10, 20, 30]
    s.pop()         returns 30, stack: [10, 20]
    s.peek()        returns 20, stack stays [10, 20]


Queue

Think of the line at a McDonald's.
First person in line gets served first.
New people join at the back.
That is FIFO. First In First Out.

Operations:
    enqueue(item)   add to the back
    dequeue()       remove from the front
    peek()          look at the front without removing
    is_empty()      returns True if empty
    size()          how many items

Real examples:
    Printer queue. First document you send gets printed first.
    Customer service calls. First caller gets helped first.
    Any waiting line in real life.

Quick trace:
    q.enqueue("alice")      line: [alice]
    q.enqueue("bob")        line: [alice, bob]
    q.enqueue("charlie")    line: [alice, bob, charlie]
    q.dequeue()             returns alice, line: [bob, charlie]
    q.peek()                returns bob, line stays [bob, charlie]


Deque

Short for Double Ended Queue. Pronounced like deck, as in deck of cards.
You can add and remove from both ends.
It is a Stack and Queue combined into one.

Operations:
    add_front(item)     add to the front
    add_rear(item)      add to the back
    remove_front()      remove from the front
    remove_rear()       remove from the back

Real example: a deck of cards. You can deal from the top or the bottom.

Quick trace:
    d.add_rear("bob")       deque: [bob]
    d.add_rear("charlie")   deque: [bob, charlie]
    d.add_front("alice")    deque: [alice, bob, charlie]
    d.remove_front()        removes alice
    d.remove_rear()         removes charlie
    deque is now just [bob]


Linked List

A chain of nodes. Each node holds a value and points to the next node.
Think of a treasure hunt. Each clue tells you where the next clue is.

    [data|next] -> [data|next] -> [data|None]

None at the end means the chain is over.

A Node has two things:
    data    the actual value
    next    a pointer to the next node, None if it is the last one

head is the first node. If head is None, the list is empty.

Operations and their Big O:
    append(data)    add to the end       O(n) you have to walk the whole chain
    prepend(data)   add to the front     O(1) just update the head
    search(data)    find a value         O(n) check each node one by one
    delete(data)    remove a node        O(n) find it first then remove

How delete works conceptually:
    you have 1 -> 5 -> 10 -> 15 -> None
    to delete 10, you make 5 point directly to 15
    1 -> 5 -> 15 -> None
    10 is now disconnected and gone

How it differs from a regular Python list:
    Python list stores items together in one block of memory
    Linked List items are scattered, connected only by pointers
    Linked List is better for frequent insertions and deletions
    Python list is better if you need to access items by index often


Binary Tree

A tree where each node has at most two children, a left and a right.

Vocabulary:
    root        the top node, no parent
    leaf        a node with no children
    parent      the node directly above
    child       a node directly below
    height      number of levels from root to deepest leaf

Example:
            5           root
           / \
          3   8
         / \   \
        1   4   9       1, 4, 9 are leaves

Traversal methods, three ways to visit every node:
    inorder     left, then root, then right   always gives sorted order on a BST
    preorder    root, then left, then right   root comes first
    postorder   left, then right, then root   root comes last

Inorder on the tree above gives: 1 3 4 5 8 9
That is sorted. That is the magic of inorder traversal on a BST.


Binary Search Tree (BST)

A binary tree with one rule:
    everything to the LEFT is smaller than the parent
    everything to the RIGHT is bigger than the parent

This rule makes searching fast because you always know which direction to go.

Example, searching for 7:
            10
           /  \
          5    15
         / \
        3   7

    start at 10, is 7 less than 10? yes, go left
    at 5, is 7 greater than 5? yes, go right
    found 7 in three steps

Without this rule you would have to check every single node.

Big O for BST operations:
    search      O(log n) average
    insert      O(log n) average
    delete      O(log n) average
    all become O(n) worst case if the tree is completely unbalanced


Hash Table

Stores key value pairs using a hash function.
Think of school lockers. Every student has a locker number.
You do not search for your locker, you calculate the number directly.

How it works:
    take a key like "alice"
    run it through a hash function to get a slot number
    store the value at that slot
    to look it up later, run the same hash and go straight to that slot

Example:
    hash("alice") = len("alice") % 10 = 5
    hash("bob") = len("bob") % 10 = 3
    hash("charlie") = len("charlie") % 10 = 7

    table: [None, None, None, 85, None, 90, None, 92, None, None]
                                bob        alice      charlie

Lookup is O(1). You go directly to the slot without searching.

Collision is when two keys map to the same slot.
It is solved by chaining (keeping a linked list at each slot)
or by open addressing (finding the next empty slot).


ALGORITHM ANALYSIS

Big O Notation

Measures how an algorithm's speed changes as the input grows.
We always look at the worst case.
Constants and smaller terms get dropped.

O(1)        constant time
            speed does not change no matter how big the input is
            examples: dict["key"], list[0], stack.push()
            like looking up a contact by name. Instant.

O(log n)    logarithmic time
            cuts the problem in half each step
            n = 1000 takes about 10 steps. That is how fast it is.
            examples: binary search, BST operations
            like opening a dictionary to the middle, then half again.

O(n)        linear time
            one operation per item
            double the input, double the time
            examples: looping through a list, linear search

O(n log n)  linearithmic time
            faster than O(n^2), slower than O(n)
            examples: merge sort, quick sort
            the realistic best you can do for general sorting

O(n^2)      quadratic time
            a loop inside a loop
            double the input, four times the work
            examples: bubble sort, selection sort, insertion sort
            fine for small inputs, gets slow fast as input grows

From fastest to slowest:
    O(1) < O(log n) < O(n) < O(n log n) < O(n^2)


SORTING ALGORITHMS

Bubble Sort

Compares two neighbors at a time. Swaps them if they are in the wrong order.
The largest value bubbles up to the end after each pass.
Simple to understand but slow.

Time complexity: O(n^2)

Trace on [5, 3, 8, 1]:
    compare 5 and 3, swap       [3, 5, 8, 1]
    compare 5 and 8, fine       [3, 5, 8, 1]
    compare 8 and 1, swap       [3, 5, 1, 8]
    8 is in place, repeat on rest


Selection Sort

Finds the smallest item in the unsorted portion and puts it at the front.
Repeats until everything is sorted.

Time complexity: O(n^2)

Trace on [5, 3, 8, 1]:
    find smallest = 1, swap with first      [1, 3, 8, 5]
    find smallest in rest = 3, in place     [1, 3, 8, 5]
    find smallest in rest = 5, swap with 8  [1, 3, 5, 8]


Insertion Sort

Picks each item and slides it into the correct position.
Like sorting cards in your hand one at a time.

Time complexity: O(n^2) worst case, O(n) if already sorted
Best choice for small or nearly sorted lists.

Trace on [5, 3, 8, 1]:
    take 3, 5 is bigger so shift 5 right       [3, 5, 8, 1]
    take 8, 5 is smaller so leave it           [3, 5, 8, 1]
    take 1, shift 8, 5, 3 all right            [1, 3, 5, 8]


Merge Sort

Divide and conquer. Split in half until you have single items.
Merge the halves back together in sorted order.
Uses recursion.

Time complexity: O(n log n) always
Space complexity: O(n), needs extra memory

Why O(n log n):
    you divide by 2 each time so there are log n levels
    at each level you touch every item once, so n work per level
    total is n times log n

How the merge step works, combining [1, 3, 5] and [2, 4, 6]:
    compare 1 and 2, take 1     [1]
    compare 3 and 2, take 2     [1, 2]
    compare 3 and 4, take 3     [1, 2, 3]
    compare 5 and 4, take 4     [1, 2, 3, 4]
    compare 5 and 6, take 5     [1, 2, 3, 4, 5]
    take 6                      [1, 2, 3, 4, 5, 6]


Quick Sort

Picks a pivot, usually the last item.
Puts everything smaller to the left, everything bigger to the right.
Pivot is now in its correct position.
Recursively sorts each side.

Time complexity: O(n log n) average, O(n^2) worst case

Trace on [5, 3, 8, 1, 4], pivot = 4:
    smaller: [3, 1]
    bigger: [5, 8]
    result: [3, 1] + [4] + [5, 8]
    sort each side recursively
    final: [1, 3, 4, 5, 8]


SEARCHING

Linear Search

Check every item from the start until you find the target.
Works on any list, sorted or not.
Time complexity: O(n)

Example, finding 7 in [3, 8, 1, 7, 5]:
    check 3, no
    check 8, no
    check 1, no
    check 7, found it


Binary Search

Only works on sorted lists.
Check the middle item. If target is smaller go left. If bigger go right.
Repeat until found.
Time complexity: O(log n)

For 1000 items, binary search takes at most 10 steps.
Linear search takes up to 1000.

Example, finding 3 in [1, 3, 5, 7, 9, 11, 13]:
    middle is 7, target 3 is smaller, look left [1, 3, 5]
    middle is 3, found it


GRAPHS

Graph

A collection of nodes connected by edges.
Like a map of cities connected by roads.
Facebook where people are nodes and friendships are edges.

Directed graph means edges have a direction, like a one way street.
Undirected graph means edges go both ways.
Weighted graph means edges have a cost like distance or time.

We represent graphs with an adjacency list.
Each node stores a list of its neighbors.


BFS - Breadth First Search

Visits all neighbors first, then their neighbors.
Spreads level by level, like ripples in water.
Uses a Queue internally.

Example graph: A connects to B and C. B connects to D and E. C connects to F.
BFS from A: A, B, C, D, E, F

Level 1: A
Level 2: B, C
Level 3: D, E, F

Use BFS when you need the shortest path in an unweighted graph.


DFS - Depth First Search

Goes as deep as possible before backtracking.
Like exploring a maze, keep going until you hit a dead end, then back up.
Uses a Stack internally, or recursion.

Same graph, DFS from A: A, B, D, E, C, F
Goes A to B to D, dead end, back to B, goes to E, dead end,
back to A, goes to C, goes to F, done.

Use DFS when finding connected components or detecting cycles.


RECURSION

Recursion

A function that calls itself.
Used when a problem can be broken into smaller versions of itself.

Every recursive function needs two things:
    base case       when to stop, no base case means infinite loop and crash
    recursive case  call yourself with a smaller problem each time

Countdown example:
    def countdown(n):
        if n == 0:          base case
            return
        print(n)
        countdown(n - 1)    recursive case

    countdown(3) prints 3, 2, 1 then stops

Factorial example:
    5! = 5 * 4 * 3 * 2 * 1 = 120

    def factorial(n):
        if n == 1:
            return 1
        return n * factorial(n - 1)

    factorial(5) works like this:
        5 * factorial(4)
        5 * 4 * factorial(3)
        5 * 4 * 3 * factorial(2)
        5 * 4 * 3 * 2 * factorial(1)
        5 * 4 * 3 * 2 * 1 = 120

Fibonacci example:
    0, 1, 1, 2, 3, 5, 8, 13...
    each number is the sum of the two before it

    def fib(n):
        if n == 0: return 0
        if n == 1: return 1
        return fib(n-1) + fib(n-2)

Iterative vs recursive:
    both solve the same problem, just written differently
    iterative uses a loop
    recursive uses a function calling itself
    some problems like trees and graphs are naturally recursive


Dynamic Programming

Solving a problem by breaking it into subproblems and storing results
so you do not recalculate things you have already figured out.
That storage technique is called memoization.

Why it matters:
    naive fibonacci is O(2^n), recalculates the same values over and over
    fibonacci with memoization is O(n), each value calculated once

Example:
    memo = {}
    def fib(n):
        if n in memo: return memo[n]
        if n <= 1: return n
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]


PYTHON TERMS

class           a blueprint for creating objects
object          an actual thing built from the class
self            refers to this specific object, keeps data separate
__init__        runs automatically when the object is created
method          a function that belongs to a class
property        data stored on an object using self.something
inheritance     a child class gets everything the parent class has

int()           converts to a number, int("123") gives 123
len()           counts items, len([1,2,3]) gives 3
append()        adds to the end of a list
pop()           removes and returns the last item, pop(0) removes first
range()         generates numbers, range(5) gives 0 1 2 3 4
f-string        puts variables in strings, f"{name} is learning Python"
"""

print("definitions loaded")
print("good luck Sandesh")