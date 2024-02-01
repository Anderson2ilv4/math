import mathematics as mt
import time

print('='*55)
print('UNICALC'.center(55))
print('='*55)

while True:
    print('CHOOSE SUBJECT'.center(55))
    print('-'*55)
    print('''1 - Math
          \r0 - Exit''')
    print('-'*55)

    choice = int(input('Wath subject? (use the index number) '))

    if choice == 1:
        print('-'*55)
        print('OPTIONS\n')
        for i in range(0, len(mt.formulas)):
            print(f'{i+1} - {mt.formulas[i]}')
        print('0 - Back')
        operation_choice = int(input('\nWhat do you want to calculate? (use the index number) '))
        if operation_choice == 1:
            print('SUM'.center(55, '-'))
            num1 = float(input('First number: '))
            num2 = float(input('Second number: '))
            result = mt.soma(num1, num2)
            print(f'\n{num1} + {num2} = {result}')
            time.sleep(1)
        elif operation_choice == 2:
            print('SUBTRACTION'.center(55, '-'))
            num1 = float(input('First number: '))
            num2 = float(input('Second number: '))
            result = mt.sub(num1, num2)
            print(f'\n{num1} - {num2} = {result}')
            time.sleep(1)
        elif operation_choice == 3:
            print('MULTIPLICATION'.center(55, '-'))
            num1 = float(input('First number: '))
            num2 = float(input('Second number: '))
            result = mt.mult(num1, num2)
            print(f'\n{num1} x {num2} = {result}')
            time.sleep(1)
        elif operation_choice == 4:
            print('MULTIPLICATION'.center(55, '-'))
            num1 = float(input('First number: '))
            num2 = float(input('Second number: '))
            div = mt.div(num1, num2)
            print(f'\n{num1} devided by {num2}')
            print(f'Reesult: {div[0]}')
            print(f'Integer division: {div[1]}')
            print(f'Rest of division: {div[2]}')
            time.sleep(1)
        elif operation_choice == 5:
            print('POWER'.center(55, '-'))
            num1 = float(input('Base number: '))
            num2 = float(input('Power: '))
            result = mt.power(num1, num2)
            print(f'\n{num1} powered to {num2} = {result}')
            time.sleep(1)
        elif operation_choice == 6:
            print('SQUARE ROOT'.center(55, '-'))
            num = int(input('Square root of: '))
            result = mt.square_root(num)
            print(f'\nThe square root of {num} = {result} ')
            time.sleep(1)
        elif operation_choice == 7:
            print('CALCULATE AREA'.center(55))
            print('-'*55)
            print('''1 - SQUARE
                \r2 - CIRCLE
                \r3 - RETANGLE
                \r4 - TRIANGLE
                    ''')
            figure = int(input('Figure choice: '))
            if figure == 1:
                side = float(input('Side lengh: '))
                result = mt.geometry(figure, side=side)
                print(f'The area is {result}')
            if figure == 2:
                ray = float(input('Ray: '))
                result = mt.geometry(figure, ray=ray)
                print(f'The circle area is {result:.2f}')
            if figure == 3:
                width = float(input('Width: '))
                height = float(input('Height: '))
                result = mt.geometry(figure, width=width, height=height)
                print(f'The retangle area is {result}')
            if figure == 4:
                print('OPTIONS')
                print('''1 - CALCULATE AREA
                      \r2 - TYPE OF''')
                option = int(input('What option? '))
                if option == 1:
                    base = float(input('Base lengh: '))
                    height = float(input('Height lengh: '))
                    result = mt.geometry(figure, base=base, height=height)
                    print(f'The area of the triangle is {result}')
                elif option == 2:
                    side1 = float(input('First side lengh: ')) 
                    side2 = float(input('Second side lengh: '))
                    side3 = float(input('Third side lengh: '))
                    if side1 == side2 and side2 == side3:
                        print('An equilateral triangle')
                    elif side1 != side2 and side1 != side3 and side2 != side3:
                        print('A scalene triangle')
                    else:
                        print('An isosceles triangle')
            time.sleep(1)
    elif choice == 0:
        break
    else:
        print("\nTry again, the choice doesn't match any subject\n")
        time.sleep(1.5)
