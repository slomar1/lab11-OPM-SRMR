"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    pass

def add(a, b):

    return a + b

def sub(a, b):

    return a - b

def mul(a, b):

    return a * b

def div(a, b):

    try:
        return b / a

    except ZeroDivisionError:
        print("Error")

def log(a, b):

    try:
        return log(a, b)
    except ZeroDivisionError:
        print("Error")

def exp(a, b):

    return a ** b

