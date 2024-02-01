#Mathematircs calculations
import math

formulas = ['SUM', 'SUBTRACTION', 'MULTIPLICATION', 'DIVISION', 'POWER', 'SQUARE ROOT', 'GEOMETRY']

def soma(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a, b):
    div = a / b
    int_div = a // b
    rest_div = a % b
    return div, int_div, rest_div

def power(a,b):
    return a ** b

def square_root(a):
    for i in range(1,a):
        if i * i == a:
            return i

def geometry(n, side=None, base = None, width=None, height=None, ray=None):
    if n == 1:
        return side * side
    if n == 2:
        return math.pi * (ray**2)
    if n == 3:
        return width * height
    if n == 4:
        return (1/2) * base * height

    return True