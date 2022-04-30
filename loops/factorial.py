#!/usr/bin/env python3

def factorial(n):
    """The factorial function returns the product of an integer and all the
    integers below it.  For example, the factorial of four (4!) is
    equal to 1*2*3*4=24."""
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120
