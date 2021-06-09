'''
PYHTON: NESTED LOOP

A nested loop is a loop inside a loop.
The 'inner loop' will be executed one time for each iteration of the 'outer loop'
'''

for i in range(2):
    for j in range(3):
        print("i: {}, j: {}".format(i, j), end=" ")
    print()
