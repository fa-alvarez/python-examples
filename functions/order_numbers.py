#!/usr/bin/env python3

def order_numbers(number1, number2):
	"""This function compares two numbers and returns them
	in increasing order."""
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)
