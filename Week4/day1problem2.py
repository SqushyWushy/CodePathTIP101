"""
purpose of the program: write a function that takes in a list and returns the elements of that
list in reverse order using a two pointer approach

"""


def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

    return lst


result = reverse_list([1, 2, 3, 4, 5])
print(result)
