# Homework from last time
def foo(a, b):
    return a + b


def f1(a, b):
    c = a + b
    return c


# Major data types in python
## integer
type(4) # -> int
## integers are always whole numbers just like every other language

## float
type(3.14) # -> float
## floats have decimal points just like every other language

## list
type([0, 1, 1, 2, 3, 5, 8]) # -> list
## lists are:
##  - ordered
##  - mutable (can be modified)
##  - expandable

## tuple
type((1, 2, 3, 4))
## tuples are:
##  - ordered
##  - immutable (cannot be modified once created)

## set
type({2, 4, 6 ,8}) # -> set
## sets are:
##  - unordered: there is no notion of 'the first element in a set', only that an element is in the set
##  - have unique elements: attempting to add an element to a set that already has that element will be a NOP

## dictionary
type({'hello': 2, 'world': 32}) # -> dict
## dicts are:
##  - unordered: there is no notion of 'the first element in a dict' only that an element is in the dict
##  - fast lookup: keys can be looked up extremely fast (approaching O(1))

# for loops in python
iterable = [2, 4, 6, 8]
for variable in iterable:
    print(variable)

## `for` loops in python are NOT like traditional `C` for loops
## in python, there is no 'counting' variable. Instead, the thing to be iterated over
## is handled by python. For each iteration, the current element will be called
## whatever name was written (in this case, `variable`). That name is free to be used
## in the body of the loop
