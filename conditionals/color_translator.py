#!/usr/bin/env python3

def color_translator(color):
	"""The color_translator function receives the name of a color, then prints
	its hexadecimal value.  Currently, it only supports the three additive
	primary colors (red, green, blue), so it returns "unknown" for all other
	colors."""
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(help(color_translator))
print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown
