num = input('Enter a number of elements that your dictionary will make up: ')
while True:
    if num in '1234567890' and num !='0':
        num = int(num)
        break
    else:
        print('you entered the wrong number')
        num = input('Enter a number of elements that your dictionary will make up: ')


def rev_dictionary():
    dict_1 = {input(f'Enter {i+1} key: '): input(f'Enter appropriate value: ') for i in range(num)}
    print(f'original dictionary: {dict_1}')
    return {value: key for key, value in dict_1.items()}


print(f'reverse dictionary: {rev_dictionary()}')

