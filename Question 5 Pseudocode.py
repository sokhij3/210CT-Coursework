MATRIXMULTIPLICATION(b, c): 
    a <- []
    for i in range(b.length):          //for each row of b
        row <- b[i]
        newRow <- []
        for j in range(c[0].length):  //for each column of c
            y <- 0
            for x in range(row.length):
                row1 <- row[x]
                col2 <- c[x][j]
                y += row1 * col2
            newRow.append(y)
        a.append(newRow)
    return a

MATRIXSUBTRACTION(b, c):
    for i in range(b.length):
        for j in range(c.length):
           a[i][j] <- b[i][j] - c[i][j]
    return a


MATRIXADDITION(b, c):
    for i in range(b.length):
        for j in range(c.length):
            a[i][j] <- b[i][j] + c[i][j]
    return a


