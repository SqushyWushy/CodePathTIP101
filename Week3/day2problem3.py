"""
purpose of the program: Write a function reverse_only_letters() that takes in a string s as a parameter.
The function reverses the order of the letters in the string and returns the new string.
Non-letter characters should remain in their original positions.
"""


def reverse_only_letters(s):
    letters = [char for char in s if char.isalpha()]
    letters.reverse()

    result = []
    letter_index = 0
    for char in s:
        if char.isalpha():
            result.append(letters[letter_index])
            letter_index += 1
        else:
            result.append(char)
    return "".join(result)


string = "skib-idi*rizz24"
print(reverse_only_letters(string))
