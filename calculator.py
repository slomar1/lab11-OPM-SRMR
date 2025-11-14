import math


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
