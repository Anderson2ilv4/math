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
            choice = str(input('Do you want to use meters, kilometers, miles or foot? ')).strip().upper()[0:2]
            if choice == 'ME':
                value = float(input('Value in meters: '))
                cm = value * 100
                km = value / 1000
                return f'{value}m is equal {cm}cm and {km}km'
            elif choice == 'KI':
                value = float(input('Value in kilometers: '))
                m = value * 1000
                cm = m * 100
                return f'{value}km is equal {cm}cm and {m}m'
            elif choice == 'MI':
                value = float(input('Value in miles: '))
                km = value * 1.60934
                m = km * 1000
                #fix cm
                cm = m * 100
                #fix foot
                ft = m * 0.3048
                return f'{value}mi is equal {cm} cm, {m}m, {km}km and {ft}ft'
            elif choice == 'FO':
                value = float(input('Value in foot: '))
                m = value * 0.3048 
                km = m / 1000
                cm = m * 100
                mi = km / 1.60934
                return f'{value}ft is equal {cm}cm, {m}m, {km}km and {mi}mi'