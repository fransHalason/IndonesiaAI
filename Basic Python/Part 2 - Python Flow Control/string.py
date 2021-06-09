# PYTHON: STRING

# STRING OPERATIONS
# Get the character at posiion 1 (the first character has the position)
a = "Hello, World!"
print(a[1])

# Get the character from position 2 to position 5(not included)
b = "Hello, World!"
print(b[2:5])

# The len() function returns the length of a string
a = "Hello, World!"
print(len(a))

# STRING OPERATIONS
# Merge variabel 'a' with variable 'b' into variable c
x = "Hello"
y = "World"
z = x + y
print(z)

# To add space between them, add" "
x = "Hello"
y = "World"
z = x + " "+ y
print(z)

# STRING FORMATTING
# The 'format()' method takes the passed arguments, formats them, and places them in the string where the placehodlers '{}' are
name = 'John'
age = 36
txt = "My name is {}, and I am {} years old".format(name, age)
print(txt)


