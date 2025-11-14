# https://github.com/slomar1/lab11-OPM-SRMR
# Partner 1: Omar Porven Miranda
# Partner 2: Santiago Mena

import math


def add(a, b):

    return a + b

def subtract(a, b):

    return a - b

def mul(a, b):

    return a * b

def div(a, b):
    
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b): 
    
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid Input for logarithm")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):

    if a < 0:
        raise ValueError("Invalid Input")
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    
    return math.hypot(a, b)