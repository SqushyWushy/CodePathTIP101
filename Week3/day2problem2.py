"""
purpose of the program: takes in a sorted list of integers and removes all duplicates in the list
"""


def remove_duplicates(nums):
    list_nums = list(set(sorted(nums)))
    return list_nums


numbers = [1, 1, 1, 2, 3, 4, 4, 5, 6, 6, 9]
result = remove_duplicates(numbers)
print(result)
