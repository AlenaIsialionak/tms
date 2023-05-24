while True:
    name, age = input('Введите Ваше имя: '), input('Введите Ваш возраст: ')
    if not age.isdigit():
        print('Ошибка, повторите ввод')
    else:
        age = int(age)
        if age <= 0:
            print('Ошибка, повторите ввод')
        elif 10 > age >= 0:
            print(f'Привет, шкет {name}')
        elif 18 >= age >= 10:
            print(f'Как жизнь, {name}?')
        elif  100 > age > 18:
            print(f'Что желаете, {name}?')
        else:
            print(f'{name}, Вы лжёте - в наше время столько не живут ...')
