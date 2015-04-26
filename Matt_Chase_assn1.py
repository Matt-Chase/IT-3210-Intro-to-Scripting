#!/usr/bin/env python
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
Student Name: Matt Chase

Assignment 1

Print the value of my_amount without changing it, but only display two decimal places.
The correct output should be 25.68

Then print the next three variables (my_first_number, my_second_number, and 
my_third_number) so that they also only show two decimal places and so that they are 
right-aligned in a column with a width of six characters. The output should look like:
124.54
 51.49
  6.28
"""

my_amount = 25.678437
print "%0.2f" % my_amount  # %0.2f prints a floating point variable with only 2 decimal places

my_first_number = 124.5392
my_second_number = 51.493333
my_third_number = 6.28345

# the 6 ensures there are 6 right-aligned characters, while the .2 limits it to 2 decimal places
print "%6.2f" % my_first_number
print "%6.2f" % my_second_number
print "%6.2f" % my_third_number