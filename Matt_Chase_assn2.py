#!/usr/bin/env python
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
Student Name: Matt Chase

Assignment 2

This program should receive input from the user from both the command line arguments
used when launching the script and by use of prompts while the script is running. The
comments in this assignment give further guidance on what specific input is expected
and how it is to be handled.

Feel free to be creative and go beyond the minimum requirements. The primary learning
objective of this assignment is receiving user input, both from command line arguments
and within the program's execution. Can you incorporate any previously learned knowledge
about Python into this exercise?
"""

from sys import argv

script_name, user_name, age = argv

print "Hello, %s! You are %s years old. That's not very young at all..." % (user_name, age)

print "\n""""The next two questions ask your height in feet and inches. If you are 5'11",
answer 5 to the first question and 11 to the second.""" "\n"
height_feet = raw_input("How many feet tall are you (excluding inches)? ")
height_inches = raw_input("How many inches tall are you (excluding feet)? ")

print "Looks like you stand tall at %s'%s\"" % (height_feet, height_inches)

inches = int(height_feet) * 12 + int(height_inches) # need to convert height_feet and height_inches
													# to integers to do math with them
print "You are %d inches tall." % inches