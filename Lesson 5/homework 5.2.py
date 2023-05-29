def fact(num: int):
    if num == 1 or num == 0:
        return 1
    else:
        return num*fact(num-1)


print(f'Result : {fact(int(input("Enter a number for which you want to calculate the factorial: ")))}')
