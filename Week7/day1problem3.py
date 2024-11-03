# Problem 3: Recursive Sum
# Without using the built-in sum() function, write a function sum_list() that calculates the sum of all values
# in a list recursively.
#
# What is the time complexity of this function? What is the space complexity?


def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        print(lst)
        return lst[0] + sum_list(lst[1:])

list1 = [1, 2, 3, 4, 5]
print(sum_list(list1))