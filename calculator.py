import math


def square_root(a):
    
    if a < 0:
        raise ValueError("Invalid Input")
    else:
        return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):

    return a + b


def subtract(a, b):
    
    return a - b


def multiply(a, b):
    
    return a * b


def divide(a, b):
    
    if a == 0:
        raise ZeroDivisionError("Invalid Input")
    else:
        return b / a


def logarithm(a, b): 

    if b <= 0:
        raise ZeroDivisionError("Invalid Input")

    else:
        math.log(a, b)
