from random import randrange
low, high = 0, 100
num = randrange(0, 100)
print(' You need to guess a number in the range from 0 to 100. ')
while True:
    guess_num = int(input(" Enter an integer: "))
    if guess_num > num:
        print('The hidden number is less')
    elif guess_num < num:
        print('The hidden number is more')
    else:
        print(f'success, the hidden number is {num}')
        break