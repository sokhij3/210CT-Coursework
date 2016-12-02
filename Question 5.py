def matrixMultiplication(b, c): #to multiply, columns in b must = rows in c
    a = []
    for i in range(len(b)): #for each row of b
        row = b[i]
        newRow = []
        for j in range(len(c[0])): #for each column of c
            y = 0
            for x in range(len(row)):
                row1 = row[x]
                col2 = c[x][j]
                y += row1 * col2
            newRow.append(y)
        a.append(newRow)
    return a

b = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

c = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 1, 2, 1]]


def matrixSubtraction(d, e):
    for i in range(len(d)):
        for j in range(len(e)):
           f[i][j] = d[i][j] - e[i][j]
    return f
            
                
d = [[6, 7],
     [8, 9]]
e = [[1, 2],
     [3, 4]]
f = [[0, 0],
     [0, 0]]

def matrixAddition(g, h):
    for i in range(len(g)):
        for j in range(len(h)):
            k[i][j] = g[i][j] + h[i][j]
    return k

g = [[3, 4],
     [5, 6]]
h = [[9, 10],
     [11, 12]]
k = [[0, 0],
     [0, 0]]
            
