from itertools import combinations
matrix = [[1, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 0, 0, 0]]
l = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
            l.append((i,j))
I = []
J = []
for i in l:
    # I.append[i[0]]
    I.append(i[0])
for j in l:
    # J.append[j[1]]
    J.append(j[1])
for i in I:
    for j in range(len(matrix[0])):
        matrix[i][j] = 1
for j in J:
    for i in range(len(matrix)):
        matrix[i][j] = 1

for i in matrix:
    print(i)