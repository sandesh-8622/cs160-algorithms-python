"""
Exam Prep 2
Heaps, BST, Tree Height, Algorithm Analysis Trick


HEAPS

MAX-heap   biggest number at the top, every parent is bigger than its kids
MIN-heap   smallest number at the top, every parent is smaller than its kids

In a MAX-heap the root is always the largest.
In a MIN-heap the root is always the smallest.
No number can be smaller than the root in a MIN-heap.

Heap stored as a list. Index formulas:
    parent of node at index i       (i - 1) // 2
    left child of node at index i   2i + 1
    right child of node at index i  2i + 2

Example:
    [10, 20, 15, 40, 30, 25, 50]

            10        index 0
           /  \
         20    15     index 1, 2
        / \   / \
       40 30 25 50    index 3, 4, 5, 6

    parent of index 4 (value 30)    (4-1) // 2 = 1 (value 20)
    left child of index 1           2*1+1 = 3 (value 40)
    right child of index 1          2*1+2 = 4 (value 30)


INSERT into a heap

    add the new number to the end
    compare with parent, if it breaks the heap rule swap
    keep swapping upward until valid

Example inserting 40 into MAX-heap:

    before:         50
                   /   \
                  30    20
                 / \   /
                15  10 40

    40 > 20 (parent), swap:
                    50
                   /   \
                  30    40
                 / \   /
                15  10 20

    40 < 50, stop. done.


DELETE from a heap

    you can only delete the root
    bring the last element to the top
    push it down by swapping with the right child until valid

    MAX-heap swap down with BIGGER child
    MIN-heap swap down with SMALLER child

Example deleting root 70 from MAX-heap:

    before:     70
               /   \
              50    40
             / \
            35  10

    remove 70, bring last (10) to top:
                10
               /   \
              50    40
             /
            35

    10 < 50 (bigger child), swap:
                50
               /   \
              10    40
             /
            35

    10 < 35 (bigger child), swap:
                50
               /   \
              35    40
             /
            10

    10 has no children, stop. valid MAX-heap.


HEAPIFY

Turning a random list into a heap all at once.

Steps:
    find last non-leaf index = n // 2 - 1
    work backwards from that index to 0
    at each node push down

Example heapifying [55, 73, 17, 41, 83, 89, 7, 28, 10, 69] into MIN-heap:

    n = 10, start at index 4 (value 83)

    index 4 (83), child is 69. 83 > 69, swap.
    list: [55, 73, 17, 41, 69, 89, 7, 28, 10, 83]

    index 3 (41), children are 28 and 10. smaller is 10. swap.
    list: [55, 73, 17, 10, 69, 89, 7, 28, 41, 83]

    index 2 (17), children are 89 and 7. smaller is 7. swap.
    17 goes to index 6, no children, stop.
    list: [55, 73, 7, 10, 69, 89, 17, 28, 41, 83]

    index 1 (73), children are 10 and 69. smaller is 10. swap.
    73 goes down. children are 28 and 41. smaller is 28. swap.
    list: [55, 10, 7, 28, 69, 89, 17, 73, 41, 83]

    index 0 (55), children are 10 and 7. smaller is 7. swap.
    55 goes down. children are 89 and 17. smaller is 17. swap.
    55 at bottom, no children, stop.
    final: [7, 10, 17, 28, 69, 89, 55, 73, 41, 83]

    7 is at top. valid MIN-heap.


ALGORITHM ANALYSIS TRICK

Two different questions with opposite answers.

If asked which is fastest by PROCESSING TIME:
    answer is LOGARITHMIC

If asked which GROWS the fastest:
    answer is EXPONENTIAL

Order from fastest TIME to slowest:
    Logarithmic, Linear, Log linear, Quadratic, Cubic, Exponential

Same order but read differently for growth questions.


BST INSERT AND DELETE

Rule: left is smaller, right is bigger

INSERT:
    start at root
    bigger, go right
    smaller, go left
    find empty spot, place it there

Example inserting 35:

        50
       /  \
      30   70
     / \
   20  40

    50, 35 < 50, go left
    30, 35 > 30, go right
    40, 35 < 40, go left
    empty, place 35 here

        50
       /  \
      30   70
     / \
   20  40
      /
     35

DELETE case 1, leaf node:
    just remove it

DELETE case 2, one child:
    remove the node
    connect parent directly to its child

    delete 20, it has one child 25:
        30              30
       /      becomes      \
      20                   25
       \
       25

DELETE case 3, two children:
    not on your exam, skip


TREE HEIGHT AND BALANCE

Height = number of edges from root to furthest leaf

    single node     height 0
    two levels      height 1
    three levels    height 2

Empty tree has height -1.

Example:
        A
       / \
      B   C
     / \
    D   E

    from A to D: 2 edges. height is 2.

BALANCED TREE:
    for every node, left and right sides differ by at most 1

    difference 0    balanced
    difference 1    balanced
    difference 2    NOT balanced

Example balanced:
        A
       / \
      B   C
     /   / \
    D   E   F

    left height 2, right height 2, difference 0, balanced

Example NOT balanced:
    A
   /
  B
 /
C

    left height 2, right height 0, difference 2, not balanced

Why it matters:
    balanced BST search is O(log n)
    unbalanced BST search is O(n) worst case
"""


print("=== HEAP DEMO ===")
import heapq

nums = [55, 73, 17, 41, 83, 89, 7, 28, 10, 69]
heapq.heapify(nums)
print("min heap:", nums)
print("smallest always at top:", nums[0])


print("=== BST DEMO ===")
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def inorder(self, node, result=[]):
        if node:
            self.inorder(node.left, result)
            result.append(node.data)
            self.inorder(node.right, result)
        return result

bst = BST()
for n in [50, 30, 70, 20, 40, 35]:
    bst.insert(n)
print("inorder should be sorted:", bst.inorder(bst.root, []))