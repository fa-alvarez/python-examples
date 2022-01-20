#!/usr/bin/env python3

def count_letters(text):
    """The count_letters function counts the frequency of letters in the input
    string.  Only letters are counted, not blank spaces, numbers, or
    punctuation.  Upper case are considered the same as lower case.
    For example, count_letters("This is a sentence.") should return
    {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}."""

    result = {}
    text = text.lower()

    for letter in text:
        if letter.isalpha():
            if letter not in result:
                result[letter] = 1
            else:
                result[letter] += 1
    return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
