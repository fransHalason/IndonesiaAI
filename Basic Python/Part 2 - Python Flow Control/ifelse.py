'''
PYTHON: CONDITIONS (IF...ELSE)

Python uses boolean variables to evaluate conditions. The boolean values ... when an expression is compared or evaluated.
Conditions: ==, !=, >, <, >=, <=, and, or, not.
'''

a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")


x = 1
y = 2
z = 3

if y > x:
    print("x is greater than y")
elif x < z:
    print("x is greater than z")
else:
    print("x is greater than y")

# ==
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

# !=
if x != y:
    print("True, x is not equal to y")
else:
    print("False, x is equal to y")

# >=
if x >= y:
    print("True, x is greater than or equal to y")
else:
    print("False, x is not greater than or equal to y")

# <=
if x <= y:
    print("True, x is less than or equal to y")
else:
    print("False, x is not less than or equal to y")


# and
if z > x and x < y:
    print("True")
else:
    print("False")

# or
if z > x or x < y:
    print("True")
else:
    print("False")

# not
if not x == y:
    print("True")
else:
    print("False")

p = '123'
q = '456'

# if p == q:
    print("p is equal to q")
else:
    print("p is not equal to q")

# Nested If Statements
r = int(input("Input your number: "))

if r % 2 == 1:
    if r < 10:
        print("r adalah bilangan ganjil dibawah 10")
    else:
        print("r adalah bilangan ganjil diatas 10")
else:
    print("r adalah bilangan genap")
