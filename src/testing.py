x = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 2], [0, 0, 0, 0, 1, 2, 4], [0, 0, 0, 1, 2, 4, 0], [0, 0, 1, 2, 4, 0, 0]]

y = [j for i in x for j in i ]
print(set(y))