#!/usr/bin/env python
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
Student Name: Matt Chase

Assignment 3

This program should receive two filenames from the user from the command line arguments
used when launching the script, and copy the first file into the second. Use the file
provided (infile.txt) as the input_file.
"""

from sys import argv
from os.path import exists
from os.path import abspath

# we don't use the script variable, so there is no need to assign it a value:
# use the indexing operator / slice techniques learned for strings and apply them to the
# argv attribute to ONLY extract the filenames (as discussed in last week's discussion 
# board).
script, input_file, output_file = argv

# print the absolute path of each file using the relevant function from the os.path module
# imported abspath function from os.path at the top

print abspath(script)
print abspath(input_file)
print abspath(output_file)

# combine the next two lines into one. Bam.

indata = open(input_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(output_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(output_file, 'w')
out_file.write(indata)

# before closing the files, read the first 13 characters from the first file and print
# them to the console. Done.

first13 = indata[:13]
print first13

# why are the next two lines important?
# It basically saves what you did to the file(s)
out_file.close()

# append the footer string to the output_file (do not overwrite any existing text)
footer = '\n\nThe End' # made it look nicer with \n's

out_file = open(output_file, 'a')
out_file.write(footer)

out_file.close()
