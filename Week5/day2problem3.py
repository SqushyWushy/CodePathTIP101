# Problem 3: Add First
# Write a function add_first() that takes in a head of a linked list and a new_node from the Node class as parameters.
#
# It should insert new_node as the new head of the linked_list. The function returns new_node.
#
# Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.

# Problem 4: Get Tail
# Write a function get_tail() that takes in the head of a linked list as a parameter.
#
# It should print out the value of the tail of the list.
#
# If the list is empty (head is None), return None.
# Note: The "tail" of a list is the last element in the linked list. Equivalent to lst[-1] in a normal list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def add_first(head, new_node):
    new_node.next = head
    return new_node
def get_tail(head):
    current_node = head
    while current_node:
        if current_node.next == None:
            return current_node.value
        current_node = current_node.next


node_1 = Node("Jigglypuff", None)
node_2 = Node("Wigglytuff", None)

node_1.next = node_2

print(node_1.value, "->", node_1.next.value)

node_3 = Node("Ditto")
node_1 = add_first(node_1, node_3)

print(node_1.value, "->", node_1.next.value)

tail = get_tail(node_3)
print(tail)
