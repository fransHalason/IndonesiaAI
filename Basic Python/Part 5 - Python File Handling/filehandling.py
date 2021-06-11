'''
PYTHON: FILE HANDLING

File handling is an important part of any web application. Python has several functions for creating, reading, updating, and deleting files. The key function for working with files in Python is the open() function. The open() function takes two parameters; filename, and mode. There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
'''

# To write to a file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
# Append to File
import os
f = open("file.txt", "a")
f.write("Added text")
f.close()

# Write to File
f = open("file.txt", "w")
f.write("Hello!")
f.close()

# A read() method for reading the content of the file:
# Read a File
f = open("file.txt", "r")
print(f.read())

# Read Only Parts of the File
f = open("file.txt", "r")
print(f.read(5))

# Read Line
f = open("file.txt", "r")
print(f.readLine())

# To delete a file, you must import the OS module, and run its os.remove() function:
# Remove the file "file.txt"
os.remove("demofile.txt")
