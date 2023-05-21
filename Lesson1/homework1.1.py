def modul(x, y):
    return (abs(x)-abs(y))/(1+abs(x*y))

def calculations(x,y,action):
    if action == '+':
        return x+y
    elif action == '-':
        return x-y
    elif action == 'degree of number' or action == '**' or action == '^' :
        return x**y
    elif action == '%':
        if y == 0:
            return "You can't divide by zero"
        else:
            return x%y
    elif action == '//' :
        if y == 0:
            return "You can't divide by zero"
        else:
            return x//y
    else:
        return 'Entered action incorrectly'

x,y, action = input('Entere a value: x = ',), input('Entere a value: y = '), input('Entere mathematical action: ')
flag = True
for i in x:
    if i not in '-1234567890':
        flag = False
    break
for i in y:
    if i not in '-1234567890':
        flag = False
    break
if flag == False:
    print('Entered value incorrectly')
else:
    x, y = float(x), float(y)
    print(f'Result:{modul(x, y)}')
    print(f'Result:{calculations(x, y, action)}')
