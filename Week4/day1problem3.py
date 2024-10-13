"""
The reverse_list() problem can also be solved
without using the two pointer technique (as you may
have seen it in previous units)! Evaluate the time
and space complexity of your two-pointer solution.

Then, evaluate the time and space of the following
solution:

Which has better time complexity?
- both solutions have the same time complexity: O(n),
because both need to traverse the entire list once

Which has better space complexity?
- the two pointer solution has better space complexity:
O(1) or constant space, while the slicing solution uses
O(n) because it creates a new list of size n


"""


def reverse_list(lst):
    # Create a new reversed list
    reversed_lst = lst[::-1]
    # Copy the elements back into the original list
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]
    return lst


print(reverse_list([1, 2, 3, 4, 5]))
