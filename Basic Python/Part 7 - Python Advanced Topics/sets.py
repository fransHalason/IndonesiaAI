'''
PYTHON: SETS

A set is a collection which is unordered and unindexed. In Python, sets are written with curly brackets.
'''

# Create a Set
this_set = {"apel", "banana", "cherry"}
print(this_set)

# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop.
for x in this_set:
    print(x)

# Add Items
this_set.add("orange")
print(this_set)

# Remove Item
this_set.remove("banana")
print(this_set)
