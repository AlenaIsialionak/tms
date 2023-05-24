x = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
y = [(3, 3, 3), (2, 2, 2), (1, 1, 1)]
z = [(2, 2, 2), (3, 3, 3), (4, 4, 4)]
sp_1 = [x[i][j] * y[i][j] * z[i][j] for i in range(len(x)) for j in range(len(x[i]))]
print(sp_1)
