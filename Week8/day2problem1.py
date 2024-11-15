# Problem 1: Is Uni-valued
# A binary tree is uni-valued if every node in the tree has the same value.
# Given the root of a binary tree, return True if the given tree is uni-valued and False otherwise.
#
# Evaluate the time complexity of your solution.
# Example Input Tree #1
#
#       1
#      / \
#     /   \
#    1     1
#   / \     \
#  1   1     1
#
# Input: root = 1
# Expected Output: True
#
# Example Input Tree #2
#
#       1
#      / \
#     /   \
#    1     2
#   / \     \
#  1   1     1
#
# Input: root = 1
# Expected Output: False

'''
understand: [x]
plan:
traverse the tree
if statement that compares our current root with the left node and right node
'''
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def is_univalued(root):
    if root is None:
        return False

    root_value = root #this variable is a constant that points to the root of the tree
    current = root #this variable is a pointer to each root node as we traverse the tree
    while current: #while current is true
        current = current.left
        if current is None:
            current = current.right #if current.left

        if current is not root_value: #if the root node
            return False







