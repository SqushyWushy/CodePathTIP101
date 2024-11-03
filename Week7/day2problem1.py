# Problem 1: Neatly Nested
# Given a string, return True if it is a nesting of zero or more pairs of parentheses.
# Return False otherwise. A valid pair of parentheses is defined as (). The input string
# will only contain the characters ( or ). Your solution must be recursive.
#
# Evaluate the time and space complexity of your solution.

def is_nested(paren_s):
    if paren_s == "":
        return True
    if len(paren_s) % 2 != 0:
        return False
    if paren_s[0] == "(" and paren_s[-1] == ")":
        return is_nested(paren_s[1:-1])
    return False


string = "((()))"
string1 = "((()"
print(is_nested(string))
print(is_nested(string1))
