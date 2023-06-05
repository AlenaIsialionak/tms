def check_numb(num):
    if '-' in num:
        if num[0] != '-':
            return 'Incorrect number entered'
    if num.replace('.', '', 1).replace('-', '', 1).isdigit() and (num[0] not in '.') and num != '0':
        fl_num = float(num)
        int_num = int(fl_num)
        if fl_num - int_num == 0:
            if int_num < 0:
                return f'Вы ввели отрицательное целое число: {int_num}'
            else:
                return f'Вы ввели положительное целое число: {int_num}'
        else:
            if fl_num < 0:
                return f'Вы ввели отрицательное дробное число: {fl_num}'
            else:
                return f'Вы ввели положительное дробное число: {fl_num}'
    elif num == '0':
        return f'Вы ввели 0'

    return 'Incorrect number entered'


print(check_numb(input('Введите число: ')))

