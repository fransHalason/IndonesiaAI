'''
PYTHON CASTING
There may be times when you want to specify a type on to a variable.
● int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous
whole number), or a string literal (providing the string represents a whole number)
● float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string
represents a float or an integer)
● str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
'''

x = int(2.8)        # x will be 2
y = float("4.2")    # y will be 4.2
z = str(3.0)        # z will be '3.0'
mylist = [x,y,z]

print(mylist)
