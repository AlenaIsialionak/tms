num = int(input('Enter an integer: '))
sum1, sum2, i = 0, 0, 1
while i <= num:
    sum1 += i**3
    i += 1
for i in range(1, num+1):
    sum2 += i**3
print(f'Result1: {sum1}')
print(f'Result2: {sum2}')
