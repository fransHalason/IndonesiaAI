'''
PYTHON: __INIT__() FUNCTION

The examples before are classes and objects in their simplest form, and are not really useful in real life applications.
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

object = Person("John", 36)

print(object.name)
print(object.age)
