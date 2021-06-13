'''
PYHTON: OBJECT METHODS

Objects can also contain methods. Methods in objects are functions that belong to the object.
'''

# Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Hello my name is {self.name}, I'm {self.age} years old")


object = Person("John", 36)
object.myfunc()
