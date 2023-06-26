def calculations(x, y):
    action = input('Enter mathematical action: ')
    try:
        if action not in '+-**^//%':
            raise ValueError('Entered action incorrectly')
    except ValueError as err:
        print(err)
    else:
        if action == '+':
            return x+y
        elif action == '-':
            return x-y
        elif action == 'degree of number' or action == '**' or action == '^':
            return x**y
        elif action == '*':
            return x*y

        try:
            x/y
        except ZeroDivisionError:
            print("you can't divide by zero")
        else:
            if action == '%':
                return x%y
            elif action == '//':
                return x//y
            elif action == '/':
                return x/y


flag = True
while flag:
        try:
            x, y = float(input('Enter a value: x = ')),  float(input('Enter a value: y = '))

        except ValueError:
            print('Entered value incorrectly. Repeat the input with the correct values')
        else:
            flag = False
            print(f'Result: {calculations(x,y)}')
