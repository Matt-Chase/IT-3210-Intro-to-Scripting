#!/usr/bin/env python
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
Student Name: Matt Chase

Assignment 5

Things are starting to get a lot more complicated. You may feel overwhelmed! This will be
much worse if you are waiting to try to do all of the exercises and homework in one day.
It is imperative that you spend multiple days per week on course material or you will not 
retain it. Since every week is building on the previous week, you can't afford to have to 
relearn the material every week. It will quickly become unmanageable and you'll be tempted 
to cut corners which will become evident in the exams and final project. Stick with it! 
You can do it - but it will take TIME and DEDICATION!

This week, you've been introduced to Boolean logic, list objects, for and while loops.
You've also learned a little about the concept of recursion through the use of nested 
statements. Working with a bunch of simplistic scripts can get boring after awhile, so 
this week I though it would be fun to write something a little more practical: your very
first zip file dictionary attack password cracker.

With that said, a reminder from the syllabus on ethical behavior is in order: Ethical 
behavior is an absolute expectation in the execution of knowledge and tools gained through 
this class. In some cases students may be exposed to activities and/or knowledge that can 
be used illegally. Such activities will be grounds for failure of the course and potential 
administrative or legal action taken against the student.

Complete this code so that it successfully cracks the zip file entitled
crackmeifyoucan.zip. Use the file common_passwords.txt as your attack dictionary. Once
successful, put the password in the comments and explain what the file is so that I know 
you cracked it!
"""

# these are modules we will use to handle command line parameters and zip files
import sys
import zipfile

# The first command line parameter is the script name itself, which is sys.argv[0] 
# (remember that Python starts counting at 0). To determine if we have more arguments than
# just the script name itself, we can check the length of argv using the len() function
# which you have previously used in LPTHW exercises. The neat thing is that argv is 
# actually a list, so you can iterate over it like a list (with a for loop) and use index
# operators on it. We want the second command line parameter, sys.argv[1], which will be
# the name of the zip file we want to crack. This script gives a friendly error message
# if the user doesn't invoke the script correctly.
#
# Don't worry about understanding the zipfile module code just yet, especially if you're
# confused already. If you can handle an extra challenge, read the docs:
# https://docs.python.org/2/library/zipfile.html
if len(sys.argv) > 1:
    zip_file = sys.argv[1]
    zip = zipfile.ZipFile(zip_file, 'r')
else:
    print "You must start the script with the file name of the zip file you want to " \
          "crack as a command line parameter, e.g. 'python assn5.py crackmeifyoucan.zip'"
    sys.exit(1)  # this exits the program and tells the operating system it had an error

# we need to open the file with our 'dictionary' of common passwords in this case
password_file = open('common_passwords.txt', 'rb')

# this is how we can read one line in a file, but writing this same thing over and over
# 10,000 times would be extremely tedious! Use a loop to iterate through the file. You
# can actually treat the file like a list, like so: 'for line in password_file:'

for line in password_file:

	# I was getting an error: "Mixing iteration and read methods would lose data" for 
	# putting the line you gave inside the loop, so I found this solution online that
	# works without error. You don't need the readline() function since 'line' does this
	# automatically when you treat password_file as a list.
	
	next_password = line	

	def crack_it(next_password):
		try:
			current_password = next_password.strip()  # this removes extra whitespace: IMPORTANT!
			print 'Trying password %s' % current_password
			zip.setpassword(current_password)
			zip.extractall()
			print 'The password is %s' % current_password
			sys.exit(0)  # the program will exit successfully once the password is found
		except Exception:
			print '\tWRONG PASSWORD'

	crack_it(next_password)
	
# don't forget to close files after opening them!
zip.close()
password_file.close()

# wolfpack!