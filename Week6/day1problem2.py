"""
Given the head of a linked list and a value val,
return the frequency of val in the list.
Evaluate the time and space complexity of your solution.
Define your variables and provide a rationale for why you
believe your solution has the stated time and space complexity.

#IOCE
	input:
		head and val, head is head of linked list, val represents a value we are looking
		for in linked list
	output:
		we are returning the frequency(amount of times) we find val inside the linked list
	constraints/things to consider/edge case:
		space/time complexity?
			O(n) for traversing through linked list
		edge cases?
			if the head is empty/ aka head = None
		constraints?
			val will be in Linked List
	example:
		#Example usage
		Input List: 3 -> 1 -> 2 -> 1
		Input: head = 3, val = 1

		#Example output
		2
"""


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def count_element(head, val):
	current = head
	freq = 0
	while current:
		if current.value == val:
			freq += 1
		current = current.next
	return freq

head = Node(3, Node(2, Node(1, Node(5, Node(5)))))

fatimahead = Node(3, Node(3))


result = count_element(head, 5)
print(result)

result = count_element(head, 0)
print(result)

result = count_element(fatimahead, 2)
print(result)