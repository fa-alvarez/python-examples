#!/usr/bin/env python3

def double_word(word):
    """The double_word function returns the same word repeated twice, followed
    by the length of the new doubled word.  For example, double_word("hello")
    returns hellohello10."""
    return word * 2 + str(len(word) * 2)

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0
