def add(x, y):
    return x + y


def subtract(x, y):
    return x-y


def divide(x, y):
    if y == 0 return ("Invalid value for denominator, can't divide by 0!")
    return x/y


def multiply(x, y):
    return x*y


def square(x):
    return x ** 2


def power(x, y):
    return x**y

import math
def sqrt(x):
    return math.sqrt(x)
# or  
# def sqrt(x):
#     return x**0.5
