"""
purpose of program: write a function that identifies whether
or not a number is prime or not.
what is a prime number?
a number with no factors other than 1 and itself
the only number it's divisible by is 1 and itself

example case:
'51'
is 51/1? yes because no remainder
is 51/2? nope there is a remainder so return false immediately
keep going if no remainders
"""


def is_prime(n):
    if n <= 1:
        return False
    for num in range(2, n):
        if n % num == 0:
            return False
    return True


print(is_prime(51))
print(is_prime(2))
print(is_prime(4))
print(is_prime(5))

