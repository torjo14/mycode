#!/usr/bin/env python
# A program that prompts a user for two operators and and operation (plus or minus)
# the program then shows the result.
# The user may enter 'q' to exit the program.
calc1 = 0.0
calc2 = 0.0
calc3 = 0.0
operation = ''
while (calc1 != 'q'):
    print('\nWhat is the first operator? Or, enter q to quit: ')
    calc1 = raw_input()
    if calc1.lower () == 'q':
        break
    calc1 = float(calc1)
    print('\nWhat is the second operator? Or, enter q to quit: ')
    calc2 = raw_input()
    if calc2.lower () == 'q':
        break
    calc2 = float(calc2)
    print('\nWhat is the third operator? Or, enter q to quit: ')
    calc3 = raw_input()
    if calc3.lower () == 'q':
        break
    calc3 = float(calc3)
    print('Enter an operation to perform on the two operators (+ or -): ')
    operation = raw_input()
    if operation == '+':
        print('\n' + str(calc1) + ' + ' + str(calc2) + ' + ' + str(calc3) + ' = ' + str(calc1 + calc2 + calc3))
    elif operation == '-':
        print('\n' + str(calc1) + ' - ' + str(calc2) + ' - ' + str(calc3) + ' = ' + str(calc1 - calc2 - calc3))
    else:
        print('\n Not a valid entry. Restarting...')