"""
purpose of this program: write a function that takes an integer list as a parameter and moves
all the even integers to the beginning of the list followed by all the odd integers in
no particular order

quick idea:
declare 2 lists -- one for even numbers and one for odd numbers
create a for loop that iterates through our full list
if odd, append to odd number list
if even, append to even number list
then append the odd numbers to the end of the even list

intuitively, this feels inefficient, but we'll start with this solution for now! 😫
"""


def sort_array_by_parity(nums):
    odd = []
    even = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    even.extend(odd)
    return even


print(sort_array_by_parity([2, 4, 7, 9, 12, 51, 99, 110, 3, 7]))
