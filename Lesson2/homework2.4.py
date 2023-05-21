str1 = input('Entere a string: ')
str2 = str1[::2]
str3 = str1[1::2]
print(f'Введённая строка: {str1.strip()}')
print()
print()
print(str2, str3, sep=5 * ' ')