# Problem 1: Is Symmetric Tree
# Given the root of a binary tree, return True if the tree’s left and right subtrees are mirrors of each other (i.e., tree is symmetric around its center). Return False otherwise.
#
# Evaluate the time complexity of your function.
"""
Understand: if the tree is symmetrical, then we will return True. Otherwise, return False
starting from the root, we need to ensure that the left and right side of the tree is of the same depth/number of levels
if not, then we can immediately know that they are not symmetrical

Example Tree #1:

       1
     /   \
    /     \
   2       2
  / \     / \
 3   4   4   3
           |


Input: root = 1
Expected Output: True


Example Tree #2:

        1
      /   \
     /     \
    2       2
     \       \
      3       3


Input: root = 1
Expected Output: False
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    def helper(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (left.val == right.val) and helper(left.left, right.right) and helper(left.right, right.left)

    if root is None:
        return True

    return helper(root.left, root.right)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(2)
root.right.right.right = TreeNode(2)

print(is_symmetric(root))