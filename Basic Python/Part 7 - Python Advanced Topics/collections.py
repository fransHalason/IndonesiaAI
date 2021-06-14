# PYTHON: COLLECTIONS

from prettytable import PrettyTable

x = PrettyTable()

x.field_names = ["Data Types", "Ordered", "Changeable", "Duplication"]
x.add_rows([
    ["Lists", "Yes", "Yes", "Yes"],
    ["Tuples", "Yes", "No", "Yes"],
    ["Sets", "No", "Yes", "No"],
    ["Dictionaries", "No", "Yes", "No"],
])

print(x)
