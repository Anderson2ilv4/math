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
                mi = value * 0.000621371
                ft = value * 3.28084
                return f'{value}m is equal {cm}cm, {km}km, {mi}mi and {ft}ft'
            elif choice == 'KI':
                value = float(input('Value in kilometers: '))
                m = value * 1000
                cm = m * 100
                mi = value * 0.621371
                ft = value * 3280.84
                return f'{value}km is equal {cm}cm, {m}m, {mi}mi and {ft}ft'
            elif choice == 'MI':
                value = float(input('Value in miles: '))
                km = value * 1.60934
                m = value * 1609.34
                cm = value * 160934
                ft = value * 5280
                return f'{value}mi is equal {cm} cm, {m}m, {km}km and {ft}ft'
            elif choice == 'FO':
                value = float(input('Value in foot: '))
                m = value * 0.3048 
                km = m / 1000
                cm = m * 100
                mi = km / 1.60934
                return f'{value}ft is equal {cm}cm, {m}m, {km}km and {mi:.7f}mi'
        elif type_choice == 2:
            choice = str(input('Do you want to use kilograms, tonnes or pounds? ')).strip().upper()[0]
            if choice == 'K':
                value = float(input('Value in kilograms: '))
                to = value / 1000
                lb = value * 2.20462
                return f'{value}Kg is equal to {to}t and {lb}lb'
            elif choice == 'T':
                value = float(input('Value in tonnes: '))
                kg = value * 1000
                lb = value * 2204.62
                return f'{value}t is equal to {kg}kg and {lb}lb'
            elif choice == 'P':
                value = float(input('Value in pounds: '))
                kg = value * 0.453592
                to = value * 0.000453592
                return f'{value}lb is equal to {kg:.4f}kg and {to:.4f}t'
        elif type_choice == 3:
            choice = str(input('Do you watn to use Celsius, Fahrenheit or Kelvin: ')).strip().upper()[0]
            if choice == 'C':
                value = float(input('Value in Celsius: '))
                return f'{value}°C is equal to {(value * 9/5 + 32)}°F and {value + 273.15}K'
            elif choice == 'F':
                value = float(input('Value in Fahrenheit: '))
                return f'{value}°F is equal to {(value - 32) * 5/9}°C and {(value - 32) * 5/9 + 273.15}K'
            elif choice == 'K':
                value = float(input('Value in Kelvin: '))
                return f'{value}K is equal {value - 273.15}°C and {(value - 273.15) * 9/5 +32}°F'
