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

class BinaryTree:
    def __init__(self):
        self.root = None   # empty tree, no root yet

    def insert(self, data):
        """Insert a new node into the tree."""
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)
    
    def _insert(self, node, data):
        """Helper function to insert recursively"""
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert(node.left, data)
        
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert(node.right, data)

    def inorder(self, node, result=[]):
        """left, root right --> gives sorted order"""
        if node:
            self.inorder(node.left, result)
            result.append(node.data)
            self.inorder(node.right, result)
        return result
    
if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(3)
    bt.insert(8)
    bt.insert(1)
    bt.insert(4)
    print(bt.inorder(bt.root, []))