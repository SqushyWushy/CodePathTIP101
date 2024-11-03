# Problem 2: How Many 1s
# Given a sorted list of integers containing only 0s and 1s, count the total
# number of 1’s in the array in O(log n) time.

# def count_ones(lst):
#     left = 0
#     right = len(lst) - 1
#
#     while left <= right:
#         middle = (left + right) // 2
#         if lst[middle] == 1 and (middle == 0 or lst[middle -1] == 0):
#             return len(lst) - middle
#         elif lst[middle] == 0:
#             left = middle + 1
#         else:
#             right = middle - 1
#
#     return 0

def count_ones(lst):
    left, right = 0, len(lst) - 1

    print("Initial List:", lst)
    print("Starting Binary Search...\n")

    # Perform binary search to find the first occurrence of 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Checking mid index {mid}, with left={left}, right={right}")
        print(f"Element at mid: {lst[mid]}")

        # Check if this mid element is the first 1
        if lst[mid] == 1 and (mid == 0 or lst[mid - 1] == 0):
            print(f"Found the first 1 at index {mid}")
            print(f"Total number of 1s: {len(lst) - mid}")
            return len(lst) - mid
        elif lst[mid] == 0:
            print(f"Moving right because lst[mid] is 0.")
            left = mid + 1
        else:
            print(f"Moving left because lst[mid] is 1 but not the first 1.")
            right = mid - 1

    print("No 1s found in the list.")
    return 0


values = [0, 0, 0, 0, 0, 0, 1, 1]
print(count_ones(values))

