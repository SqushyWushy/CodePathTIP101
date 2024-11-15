# Problem 4: Find Leftmost Node I
# Given the root of a binary tree, write a function that finds the value of the left most node in the tree.
#
# Evaluate the time complexity of your function.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.val



root = TreeNode(5, TreeNode(6), TreeNode(7))
print(left_most(root))