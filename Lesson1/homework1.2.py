#Срезы
# exercise №1
str1 = '"aaaaaBccBddBeeBffBggB"'
print(str1[6::3])
str2 = ''

# exercise №2
str2_new = 'AAAABBBBCCCCDDDDFFFF'
n = len(str2)
for i in range((n//4) +1):
    str2_new+=str2[i*(n//4) :(i+1)*(n//4)]
if n%2 == 1 :
    str2_new += str2[(n//4) * 4]
print(str2_new)

# exercise №3
str3 = input()
str3_new = str3[::-1]
print(str3_new)