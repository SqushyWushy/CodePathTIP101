# A variation of the two-pointer technique introduced in Unit 4 is to have a slow and a
# fast pointer that increment at different rates. Given the head of a linked list, use
# the slow-fast pointer technique to find the middle node of a linked list. If there
# are two middle nodes, return the second middle node.
#
# Evaluate the time and space complexity of your solution. Define your variables and
# provide a rationale for why you believe your solution has the stated time and
# space complexity.
"""
#IOCE
    #Inputs:
        what are our inputs?
            our input is the head of a linked list and that is it
    #Outputs
        what are our outputs?
            our output is the middle node of a linked list
            if even, then return second middle node
    #Constraints:
        what do we need to consider?
            we need to consider the length of linked list and if even, then return second middle node
            if odd, return the exact middle node
            if empty, then return None
            if 1 node, then that node is middle
            if 2 nodes, then second node is middle
        what constraints do we have?
            we have to use the slow-fast pointer method
        what is our space/time complexity?
         ^^^ not sure yet
    #Examples:
        # Input List:
            # 1 -> 2 -> 3
            # Input: head = 1
        Example Output:
            # Expected Return Value: 2
"""

class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
    if head is None:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

node = Node(1)
head = Node(1, Node(2, Node(3, Node(4))))

result = find_middle_element(head)
print(result.value)

