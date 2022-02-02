# python-examples
This repository is intended to contain some basic python code examples. All
examples are based on code from Google's Crash Course on Python available
on Cousera's site as of today.


## Conditionals

### color_translator.py
The color_translator function receives the name of a color, then prints its
hexadecimal value.  Currently, it only supports the three additive primary
colors (red, green, blue), so it returns "unknown" for all other colors.

### exam_grade.py
Students in a class receive their grades as Pass/Fail. Scores of 60 or more
(out of 100) mean that the grade is "Pass". For lower scores, the grade is
"Fail". In addition, scores above 95 (not included) are graded as "Top Score".
This function receives the score and returns the proper grade.

### format_address.py
The format_address function separates out parts of the address string into
new strings: house_number and street_name, and returns: "house number X on
street named Y". The format of the input string is: numeric house number,
followed by the street name which may contain numbers, but never by
themselves, and could be several words long. For example, "123 Main Street",
"1001 1st Ave", or "55 North Center Drive".

### format_name.py
This function receives the first_name and last_name parameters and then returns
a properly formatted string.

### fractional_part.py
The fractional_part function divides the numerator by the denominator, and
returns just the fractional part (a number between 0 and 1).

### longest_word.py
The longest_word function is used to compare 3 words. It returns the
word with the most number of characters (and the first in the list when they
have the same length).

### number_group.py
The number_group function returns "Positive" if the number received is
positive, "Negative" if it's negative, and "Zero" if it's 0.


## Dictionaries

### add_prices.py
The add_prices function returns the total price of all of the groceries in
the  dictionary.

### combine_guests.py
Taylor and Rory are hosting a party. They sent out invitations, and each one
collected responses into dictionaries, with names of their friends and how
many guests each friend is bringing. Each dictionary is a partial list, but
Rory's list has more current information about the number of guests. This
function combines both dictionaries into one, with each friend listed only
once, and the number of guests from Rory's dictionary taking precedence, if a
name is included in both dictionaries. Then it prints the resulting dictionary.

### count_letters.py
The count_letters function counts the frequency of letters in the input
string.  Only letters are counted, not blank spaces, numbers, or
punctuation.  Upper case are considered the same as lower case.
For example, count_letters("This is a sentence.") should return
{'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

### email_list.py
The email_list function receives a dictionary, which contains domain names as
keys, and a list of users as values. It returns a list
that contains complete email addresses (e.g. diana.prince@gmail.com).

### groups_per_user.py
The groups_per_user function receives a dictionary, which contains group names
with the list of users. Users can belong to multiple groups. It returns a
dictionary with the users as keys and a list of their groups as values.


## Functions

### convert_distance.py
This function converts miles to kilometers (km).

### order_numbers.py
This function compares two numbers and returns them in increasing order.


## Lists

### combine_lists.py
A professor with two assistants, Jamie and Drew, wants an attendance list of
the students, in the order that they arrived in the classroom. Drew was the
first one to note which students arrived, and then Jamie took over. After the
class, they each entered their lists into the computer and emailed them to
the professor, who needs to combine them into one, in the order of each
student's arrival. Jamie emailed a follow-up, saying that her list is in
reverse order. The combine_lists function combines them into one list as follows:
the contents of Drew's list, followed by Jamie's list in reverse order, to
get an accurate list of the students as they arrived.
