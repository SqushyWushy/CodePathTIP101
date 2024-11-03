# Problem 3: Binary Search IV
# Thus far, we’ve mostly been using an iterative implementation of the
# binary search algorithm. Recursive implementations of binary search
# are also very common. Implement binary_search() recursively.
'''
example list: [1, 2, 3, 5, 7, 9, 11], target = 9
left = 0
right = 6
middle = 3
lst[middle] = 5
'''

def binary_search(nums, target, left = 0, right = None):
    if right is None:
        right = len(nums) - 1

    if left > right:
        return - 1

    middle = (left + right) // 2

    if nums[middle] == target:
        return middle
    elif nums[middle] < target:
        return binary_search(nums, target, middle + 1, right)
    else:
        return binary_search(nums, target, left, middle - 1)

nums = [1, 2, 3, 5, 7, 9, 11]
print(binary_search(nums, 11))