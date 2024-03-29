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

### car_listing.py
In this code car_prices dictionary is iterated through its keys and values, printing out some information about each one.

### combine_guests.py
Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, but Rory's list has more current information about the number of guests. This function combines both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. Then it prints the resulting dictionary.

### count_letters.py
The count_letters function counts the frequency of letters in the input string.  Only letters are counted, not blank spaces, numbers, or punctuation.  Upper case are considered the same as lower case. For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

### email_list.py
The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. It returns a list that contains complete email addresses (e.g. diana.prince@gmail.com).

### groups_per_user.py
The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. It returns a dictionary with the users as keys and a list of their groups as values.

### wardrobe.py
In Python, a dictionary can only hold a single value for a given key. To workaround this, the single value can be a list containing multiple values. This code has a dictionary called "wardrobe" with items of clothing and their colors.


## Functions

### convert_distance.py
This function converts miles to kilometers (km).

### get_seconds.py
The get_seconds function converts hours and minutes to seconds.  This example works out the amount of seconds in 2 hours and 30  minutes, then adds this number to the amount of seconds in 45 minutes and 15 seconds, then prints the result.

### lucky_number.py
The lucky_number function returns a message with a lucky number determined by 9 times the length of the given name.

### order_numbers.py
This function compares two numbers and returns them in increasing order.


## Lists

### combine_lists.py
A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order. The combine_lists function combines them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

### file_size.py
The file_size function receives a tuple to store information about a file: its name, its type and its size in bytes. It returns the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.

### filenames.py
Given a list of filenames, this code renames all the files with extension hpp to the extension h.

### octal_to_string.py
The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others.  Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute.  Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.

For example:

640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"

The octal_to_string function converts a permission in octal format into a string format.

### odd_numbers.py
The odd_numbers function returns a list of odd numbers between 1 and n, inclusively.

### pig_latin.py
The pig_latin function turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end  and appending "ay" to the end. For example, python ends up as ythonpay.

### squares.py
The squares function uses a list comprehension to create a list of squared numbers (n*n).  It receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively. For example, squares(2, 3) should return [4, 9].


## Loops

### counter.py
The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise.

### digits.py
The digits functThe sum_squares function returns the sum of all the squares of numbers
    between 0 and x (not included)ion returns how many digits a number has.  For example: 25 has 2 digits and 144 has 3 digits.

### even_numbers.py
The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2, up to and including the maximum that's passed into the function. For example, even_numbers(6) returns “2 4 6”.

### factorial.py
The factorial function returns the product of an integer and all the integers below it.  For example, the factorial of four (4!) is equal to 1\*2\*3\*4=24.

### multiplication_table.py
This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column).

### show_letters.py
The show_letters function prints out each letter of a word on a separate line.

### square.py
The sum_squares function returns the sum of all the squares of numbers between 0 and x (not included).


## OOP (Object-Oriented Programming)

### animal.py
An example of inheritance making animals speak.

### city.py
The City class has the following attributes: name, country (where the city is located), elevation (measured in meters), and population (approximate, according to recent statistics). The max_elevation_city function returns the name of the city and its country (separated by a comma), when comparing the 3 defined instances for a specified minimal population. For example, calling the function for a minimum population of 1 million: max_elevation_city(1000000) should return "Sofia, Bulgaria".

### clothing1.py
In this example we have a base class called Clothing.  A second class, called Shirt, inherits methods from the Clothing class.

### clothing2.py
This script shows the current clothing stock by material.  First, it adds up 6 cotton shirts followed by 4 cotton sweatpants. Finally, it prints out the result.

### dog.py
The Dog class contains a method that returns seven times the entered year (one human year is about 7 dog years).

### elevator.py
This code defines an Elevator class. The elevator has a current floor, it also has a top and a bottom floor that are the maximum and minimum floors it can go to. The elevator go through the floors requested.

### flower.py
This script prints a poem.

### fruit.py
This is a very basic inheritance example.

### furniture.py
We have two pieces of furniture: a brown wood table and a red leather couch. The describe_furniture function can format a sentence that describes these pieces as follows: "This piece of furniture is made of {color} {material}".

### zoo.py
This script shows how many types of animals are in a certain category in a zoo.


## Recursion

### is_power_of.py
This function returns whether the number is a power of the given base. Note: base is assumed to be a positive number.

### sum_positive_numbers.py
The function sum_positive_numbers returns the sum of all positive numbers between the number n received and 1. For example, when n is 3 it returns 1+2+3=6, and when n is 5 it returns 1+2+3+4+5=15.


## String

### convert_distance.py
The convert_distance function returns the phrase "X miles equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) returns "12 miles equals 19.2 km".

### double_word.py
The double_word function returns the same word repeated twice, followed by the length of the new doubled word.  For example, double_word("hello") returns "hellohello10".

### ex_format_method1.py
This is an example of using the format() method on a string.

### ex_format_method2.py
This is another example of using the format() method on a string.

### ex_index.py
This example shows how to find out the position of "x" in "supercalifragilisticexpialidocious" using the index method.

### first_and_last.py
This function returns True if the first letter of the string is the same as the last letter of the string, and False if they're different.  An empty string returns True.

### highlight_word.py
The highlight_word function changes the given word in a sentence to its upper-case version. For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". 

### initials.py
The initials function returns the initials of the words contained in the phrase received, in upper case. For example: "Universal Serial Bus" returns "USB"; "local area network" returns "LAN”.
