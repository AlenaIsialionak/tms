# version №1
str1 = input().split(' ')
str1[0], str1[1] = str1[0].strip(), str1[1].strip()
str1 = " ! ".join(str1)
print(f"!{str1}!")

# version №2
str2 = input().split(' ')
str2 = str2[::-1]
str2. insert(1, ' ! ')
print(f"!{''.join(str2)}!")

# version №3
str3 = input().split(' ')
elem = str3.pop(-1)
str3.insert(0, elem)
str3. insert(1, ' ! ')
str_new = '!'+''.join(str3)+'!'
print(str_new)

