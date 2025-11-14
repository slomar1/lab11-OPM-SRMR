# https://github.com/slomar1/lab11-OPM-SRMR
# Partner 1: Omar Porven Miranda
# Partner 2: Santiago Mena

import math

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
    except ValueError:
        print("Error")

def exp(a, b):

    return a ** b

def add(a, b):

    return a + b


def subtract(a, b):

    return a - b


def multiply(a, b):

    return a * b


def logarithm(a, b):

    if b <= 0:
        raise ValueError("Invalid Input")

    else:
        math.log(a, b)



def square_root(a):
    
    if a < 0:
        raise ValueError("Invalid Input")
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    
    return math.hypot(a, b)