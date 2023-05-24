my_list = list(range(1,51))
sp_1 = [my_list[50-i] for i in my_list]
print(sp_1)
sp_2 = [my_list[-i] for i in my_list]
print(sp_2)