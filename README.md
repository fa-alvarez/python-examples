# python_examples
This repository is intended to contain some basic python code examples. All
examples are based on code from Google's Crash Course on Python available
on Cousera's site as of today.

## color_translator.py
The color_translator function receives the name of a color, then prints its
hexadecimal value.  Currently, it only supports the three additive primary
colors (red, green, blue), so it returns "unknown" for all other colors.

## exam_grade.py
Students in a class receive their grades as Pass/Fail. Scores of 60 or more
(out of 100) mean that the grade is "Pass". For lower scores, the grade is
"Fail". In addition, scores above 95 (not included) are graded as "Top Score".
This function receives the score and returns the proper grade.

## format_address.py
The format_address function separates out parts of the address string into
new strings: house_number and street_name, and returns: "house number X on
street named Y". The format of the input string is: numeric house number,
followed by the street name which may contain numbers, but never by
themselves, and could be several words long. For example, "123 Main Street",
"1001 1st Ave", or "55 North Center Drive".

## format_name.py
This function receives the first_name and last_name parameters and then returns
a properly formatted string.

## fractional_part.py
The fractional_part function divides the numerator by the denominator, and
returns just the fractional part (a number between 0 and 1).

## longest_word.py
The longest_word function is used to compare 3 words. It returns the
word with the most number of characters (and the first in the list when they
have the same length).

## number_group.py
The number_group function returns "Positive" if the number received is
positive, "Negative" if it's negative, and "Zero" if it's 0.
