"""
purpose of program: we are going to write a function that takes in a string as a parameter
and returns true if the string can be a palindrome after deleting at most one character from
it and false otherwise

here is my beginner idea so far:
use the two pointer technique to see if the original string is already a palindrome
if yes, return true
if no, then proceed to next step
if no, we will create a list ob substrings be removing one character at a time from the
original string
then for each of those substrings, check if it's a palindrome, if any are true we will
return true
if all are false, we will return false

pseudo code:
we first need a helper function that simply identifies whether or not any given string
is a palindrome or not.
helper function:
declare 2 pointers, one for left and initialize to zero and one for right which
we will initialize to length of the string - 1
run a loop while left is < right
if string[left] == string[right]:
increment left by +1 and right by -1
else return false
if it gets through the entire string successfully then it is palindrome and
return True

we are going to call our helper function using our original string and return true
if palindrome ano nothing else is necessary

if it does not return true then we will create a list of substrings by removing each letter
from the orignal string

we will do this by using a for loop that loops through each index of len(s)
declare and initialize a new string = s[:i] + s[i  + 1:]
then pass our new string into our helper function with an if statement
if true, return true
if not true then keep checking the next sub string
if none end up returning true
then once the for loop is over we will return False
"""


def valid_palindrome(s):
    def is_palindrome(sub_s):
        left, right = 0, len(sub_s) - 1
        while left < right:
            if sub_s[left] == sub_s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
    if is_palindrome(s):
        return True
    for i in range(len(s)):
        new_string = s[:i] + s[i + 1:]

        if is_palindrome(new_string):
            return True
    return False


print(valid_palindrome("racecar"))
