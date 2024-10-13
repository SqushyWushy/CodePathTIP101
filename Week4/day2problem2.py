"""
purpose of program: Imagine you're an awesome babysitter and want to give the kids
you're looking after some cookies as a snack.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the
child will be content with.
Each cookie j has a cookie size s[j].
If s[j] >= g[i], we can assign the cookie j to the child i, and the child will be content.
If s[j] < g[i], the child will not be content.

Write a function find_content_children() that takes in the greed list g and the
cookie size list s as parameters and maximizes the number of content children you
are babysitting!

first idea to start:
at the very beginning, let's sort the 2 lists to iterate more easily
start with a content_counter for content kids who are satisfied
create a pointer for the kids greed factor and a pointer for the cookies size
we are going to make a while loop that goes as long as the kids pointer < number of kids
and as long as the cookie pointer is < number of cookies
if kid[pointer >= cookie[pointer]:
increment the content_counter by +1
then increment the kid pointer to move on to the next kid
whether or not we find a match we will move on to the next cookie
and increment the cookie pointer by 1
then return content children
"""


def find_content_children(g, s):
    g.sort()
    s.sort()

    content_children = 0
    i = 0
    j = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            content_children += 1
            i += 1
        j += 1
    return content_children


print(find_content_children([1, 2, 3], [1, 1, 3]))
print(find_content_children([1, 1], [2, 2, 2]))
print(find_content_children([1, 3, 4, 4, 5], [3, 1, 3, 7, 2]))
