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
    elif choice == 0:
        break
    else:
        print("\nTry again, the choice doesn't match any subject\n")
        time.sleep(1.5)
