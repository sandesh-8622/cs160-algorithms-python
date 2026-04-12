"""
Binary Tree --> each node has at most 2 children (left and right)

Vocabulary
- Root --> top node, no parent
- Parent --> node above
- Child --> Node below
- Leaf --> node with no children

Example:

        5
       / \
      3   8
     / \   \
    1   4   9

"""
class TreeNode:
    def __init__(self, data):
        self.data = data   # the value
        self.left = None   # left child
        self.right = None  # right child