# Print using `print` function.
print('Hello, World!')

# Assign variables; No need to declare beforehand, and no need to declare types.
x = 42
y = 'hello world'

# Basic operations
## Addition
print(1 + 3) # -> 4
## Subtraction
print(4 - 2) # -> 2
## Multiplication
print(4 * 5) # -> 20
## Division
print(3 / 2) # -> 1.5
## Truncated Division
print(3 // 2) # -> 1
## Modulus
print(5 % 3) # -> 2

# Functions
## Define a function using the `def` keyword, followed
## by the parameters. Return using `return`. Note that there
## is no need to declare a return type, nor is there a need to
## declare the types of your parameters.
def foo(a):
    return a + 1

print(foo(3)) # -> 4


# BONUS TOPICS
## Can you return multiple values in a function?
def bar():
    return 2, 4

q, w = bar()
print(q) # -> 2
print(w) # -> 4
## Sure can! We'll look further into this later.

## What happens if you don't type the parentheses after a function name?
print(foo) # -> ?????
## We'll come back to this later
