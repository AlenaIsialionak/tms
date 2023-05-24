list_1 = [1, 2, 3]
list_2 = [1, 2, 3, 4, 5]
sp1 = [list_1[i] * list_2[j] for i in range(len(list_1)) for j in range(len(list_2))]
print(sp1)
