#!/usr/bin/env python3

def fractional_part(numerator, denominator):
	"""The fractional_part function divides the numerator by the denominator, and
	returns just the fractional part (a number between 0 and 1)."""
	if denominator != 0:
		return (numerator % denominator) / denominator
	return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
