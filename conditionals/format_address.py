#!/usr/bin/env python3

def format_address(address_string):
    """The format_address function separates out parts of the address string into
    new strings: house_number and street_name, and returns: "house number X on
    street named Y". The format of the input string is: numeric house number,
    followed by the street name which may contain numbers, but never by
    themselves, and could be several words long. For example, "123 Main Street",
    "1001 1st Ave", or "55 North Center Drive"."""
    number = 0
    street = ""
    parts = address_string.split()

    for part in parts:
        if part.isnumeric():
            number = part
        elif street == "":
            street = part
        else:
            street = street + " " + part
    return "house number {} on street named {}".format(number, street)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

print (format_address("1600 Amphitheatre Parkway"))
# Should print "house number 1600 on street named Amphitheatre Parkway"
