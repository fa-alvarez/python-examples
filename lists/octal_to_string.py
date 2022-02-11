#!/usr/bin/env python3

def octal_to_string(octal):
    """The octal_to_string function converts a permission in octal format into a
    string format."""
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    for digit in [int(n) for n in str(octal)]:
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += "-"
    return result

print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------
