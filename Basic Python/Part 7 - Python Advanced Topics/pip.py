'''
PYTHON: PIP

PIP is a package manager for Python packages, or modules if you like.
A package contains all the files you need for a module.
Modules are Python code libraries you can include in your project.

Check if PIP is Installed
pip --version

Check if PIP is Installed
Find more packages at https://pypi.org/

Download a Package, ex: “camelcase” package
pip install camelcase

Using a Package
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

List Packages
pip list

Remove a Package
pip uninstall camelcase

'''
