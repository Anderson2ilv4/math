#Mathematircs calculations

formulas = ['SUM', 'SUBTRACTION', 'MULTIPLICATION', 'DIVISION']

def soma(a,b):
    return a + b

def sub(a,b):
    sub = a - b
    return sub

def mult(a,b):
    mult = a * b
    return mult

def div(a, b):
    div = a / b
    int_div = a // b
    rest_div = a % b
    return div, int_div, rest_div