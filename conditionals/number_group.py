#!/usr/bin/env python3

def number_group(number):
    """The number_group function returns "Positive" if the number received
    is positive, "Negative" if it's negative, and "Zero" if it's 0."""
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative
