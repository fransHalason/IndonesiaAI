'''
PYTHON: SCOPE

A variable is only available from inside the region it is created. This is called scope.

Local Scope

A variable created inside a function belongs to the local scope of that function, and can only be used inside that
function.

'''

def myfunc():
    x = 300
    print(x)

myfunc()

z = x + 20
print(z)

