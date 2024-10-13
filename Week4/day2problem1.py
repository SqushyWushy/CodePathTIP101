"""
purpose of this program: write a function is_long_pressed that in two strings as
parameters. the function should examine the characters of the strings and return true if it
is possible that they are the same name just potentially with duplicate characters because
of accidental long-pressed characters. we want to use the two pointer approach to solve the
problem.

my first idea:
declare 2 pointers, name pointer and typed pointer
initialize them to start at beginning of string at zero
start a while loop that goes on while the typed pointer < length of typed string:
inside the while loop, if the name pointer < length of name and the char at typed[ptr] and char at name[ptr] are equal:
then we are going to increment our name pointer by 1
else if typed pointer is greater than zero and typed[ptr] is equal to typed[ptr - 1]
then we are going to pass and continue into the rest of the loop
else neither are true, then we will return false
at the end of the loop in case any of the conditions pass we will increment out typed pointer by one
once it goes through the entirety of the loop without returning false, then we know that typed
is long pressed of name
return True
"""


def is_long_pressed(name, typed):
    nameptr = 0
    typedptr = 0
    while typedptr < len(typed):
        if nameptr < len(name) and typed[typedptr] == name[nameptr]:
            nameptr += 1
        elif typedptr > 0 and typed[typedptr] == typed[typedptr - 1]:
            pass
        else:
            return False
        typedptr += 1
    return True


myName = "Hector"
myTyped = "HHeeecttor"
result = is_long_pressed(myName, myTyped)
print(result)
