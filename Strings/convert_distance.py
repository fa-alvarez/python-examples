#!/usr/bin/env python3

def convert_distance(miles):
	"""This function returns the phrase "X miles equals Y km", with Y having
	only 1 decimal place. For example, convert_distance(12) returns
	'12 miles equals 19.2 km'."""
	km = miles * 1.6
	result = "{} miles equals {:.1f} km".format(miles, km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
