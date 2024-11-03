# Problem 5: Binary Search I
# Binary search is a searching algorithm that allows us to efficiently find the index of a given value
# within a sorted list. Given the pseudo code for binary search below, implement an iterative (non-recursive)
# implementation of binary search. There is also a recursive alternative that we’ll cover in the session 2 problem set!
#
# Evaluate the time and space complexity of your implementation.

def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle
        elif lst[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1

values = [1, 2, 3, 4, 5, 6, 8, 10, 14, 17, 21, 32, 37, 43]
print(binary_search(values, 17))
