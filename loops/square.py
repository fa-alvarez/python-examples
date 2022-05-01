#!/usr/bin/env python3

def square(n):
    return n*n

def sum_squares(x):
    """The sum_squares function returns the sum of all the squares of numbers
    between 0 and x (not included)"""
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285
