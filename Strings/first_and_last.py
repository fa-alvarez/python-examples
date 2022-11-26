#!/usr/bin/env python3

def first_and_last(message):
    if len(message) == 0:
        return True
    if message[0] == message[-1]:
        return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
