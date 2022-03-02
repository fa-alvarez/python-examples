# python-examples
This repository contains some basic python code examples. All examples are based on code from Google's Crash Course on Python available on Cousera's site as of today.


## Conditionals

### color_translator.py
The color_translator function receives the name of a color, then prints its hexadecimal value.  Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.

### exam_grade.py
Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass". For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score". This function receives the score and returns the proper grade.

### format_address.py
The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive".

### format_name.py
This function receives the first_name and last_name parameters and then returns a properly formatted string.

### fractional_part.py
The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1).

### longest_word.py
The longest_word function is used to compare 3 words. It returns the word with the most number of characters (and the first in the list when they have the same length).

### number_group.py
The number_group function returns "Positive" if the number received is positive, "Negative" if it's negative, and "Zero" if it's 0.


## Dictionaries

### add_prices.py
The add_prices function returns the total price of all of the groceries in the  dictionary.

### combine_guests.py
Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, but Rory's list has more current information about the number of guests. This function combines both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. Then it prints the resulting dictionary.

### count_letters.py
The count_letters function counts the frequency of letters in the input string.  Only letters are counted, not blank spaces, numbers, or punctuation.  Upper case are considered the same as lower case. For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

### email_list.py
The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. It returns a list that contains complete email addresses (e.g. diana.prince@gmail.com).

### groups_per_user.py
The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. It returns a dictionary with the users as keys and a list of their groups as values.


## Functions

### convert_distance.py
This function converts miles to kilometers (km).

### order_numbers.py
This function compares two numbers and returns them in increasing order.


## Lists

### combine_lists.py
A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order. The combine_lists function combines them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

### file_size.py
The file_size function receives a tuple to store information about a file: its name, its type and its size in bytes. It returns the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.

### filenames.py
Given a list of filenames, this code renames all the files with extension hpp
to the extension h.

### octal_to_string.py
The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others.  Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute.  Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.

For example:

640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"

The octal_to_string function converts a permission in octal format into a string format.

### odd_numbers.py
The odd_numbers function returns a list of odd numbers between 1 and n,
inclusively.

### pig_latin.py
The pig_latin function turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end  and appending "ay" to the end. For example, python ends up as ythonpay.

### squares.py
The squares function uses a list comprehension to create a list of squared numbers (n*n).  It receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively. For example, squares(2, 3) should return [4, 9].


## Loops

### counter.py
The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise.
