'''
PYTHON: FUNCTION DEFAULT PARAMETER

Python allows function arguments to have default values. If the function is called without the argument, the argument gets its default value. The default value is assigned by using assignment(=) operator.
'''

def my_function(name=""):
    print("Hello " + name)
my_function("James")