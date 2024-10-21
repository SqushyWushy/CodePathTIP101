# Problem 5: Replace Node
# Using the Node class, write a function ll_replace() that takes a head of a linked list and two values, original and replacement as parameters.
#
# The function updates any node with value original to have value replacement.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def ll_replace(head, original, replacement):
    current_node = head
    while current_node:
        if current_node.value == original:
            current_node.value = replacement
        current_node = current_node.next



num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

print(num1.value, "-->", num2.value, "-->", num3.value)


head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"

print(num1.value, "-->", num2.value, "-->", num3.value)