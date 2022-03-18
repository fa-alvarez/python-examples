#!/usr/bin/env python3

def longest_word(word1, word2, word3):
	"""The longest_word function is used to compare 3 words. It should return
	the	word with the most number of characters (and the first in the list when
	they have the same length)."""
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))
