"""
purpose of the program: Write a function longest_uniform_substring() that takes in a string s and returns the length of the longest uniform substring.
A uniform substring consists of a single repeated character.
step 1: handle the edge case of an empty string
step 2: declare and initialize a max_len variable to 1 and to hold the greatest uniform substring
step 3: declare and initialize a current_len variable to 1 for each new letter iteration
step 4: iterate over each character in string, check if same as prev char
step 5: if yes, increase current len by 1
step 6: if no, compare current len by max len, the higher one takes max len
step 7: reset curren len back to 1
step 8:The last uniform substring may be the longest, so check it at the end
step 9: return max len

"""


def longest_uniform_substring(s):
    if not s:
        return 0

    max_len = 1
    current_len = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 1
    max_len = max(max_len, current_len)

    return max_len


string = "AAAbbbcddddeeFFfffff"
print(longest_uniform_substring(string))
