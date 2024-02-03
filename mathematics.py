#Mathematircs calculations
import math

formulas = ['SUM', 'SUBTRACTION', 'MULTIPLICATION', 'DIVISION', 'POWER', 'SQUARE ROOT', 'GEOMETRY', 'RULE OF THREE', 'MEASUREMENT CONVERSION']

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

def rule_of_three(a, b):
    return (b*100) / a

def measurement_conversion(type_choice):
    if type_choice == 1:
        choice = str(input('Do you want to use meters, kilometers, miles or feets? ')).strip().upper()[0]
        if choice == 'M':
            value = float(input('Value in meters: '))
            cm = value * 100
            km = value / 1000
            return value, cm, km
