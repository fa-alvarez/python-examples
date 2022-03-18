#!/usr/bin/env python3

def file_size(file_info):
	"""This function receives a tuple to store information about a file:
	its name, its type and its size in bytes. It returns the size in
	kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places."""

	file_name, file_type, file_size = file_info
	return("{:.2f}".format(file_size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21
