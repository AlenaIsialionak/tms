x = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
y = [(3, 3, 3), (2, 2, 2), (1, 1, 1)]
z = [(2, 2, 2), (3, 3, 3), (4, 4, 4)]
sp_1 = [x[i][0] * y[i][1] * z[i][2] for i in range(len(x))]
print(sp_1)
