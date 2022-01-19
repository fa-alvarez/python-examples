#!/usr/bin/env python3

def combine_guests(guests1, guests2):
    """Taylor and Rory are hosting a party. They sent out invitations, and each one
    collected responses into dictionaries, with names of their friends and how
    many guests each friend is bringing. Each dictionary is a partial list, but
    Rory's list has more current information about the number of guests. This
    function combines both dictionaries into one, with each friend listed only
    once, and the number of guests from Rory's dictionary taking precedence, if a
    name is included in both dictionaries. Then it prints the resulting dictionary."""

    guests2.update(guests1)
    return guests2

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))
