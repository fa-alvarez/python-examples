#!/usr/bin/env python3

def pig_latin(text):
    """The pig_latin function turns text into pig latin: a simple text
    transformation that modifies each word moving the first character to the end
    and appending "ay" to the end. For example, python ends up as ythonpay."""
    say = ""
    pig_latin_word = []
    words = text.split()
    for word in words:
            pig_latin_word.append(word[1:len(word)+1] + word[0] + "ay")
        say = " ".join(pig_latin_word)
    return say

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
