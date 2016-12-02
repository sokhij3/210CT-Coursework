MATRIXMULTIPLICATION(b, c): 
    a <- []
    for i in range(len(b)):          //for each row of b
        row <- b[i]
        newRow <- []
        for j in range(len(c[0])):  //for each column of c
            y <- 0
            for x in range(len(row)):
                row1 <- row[x]
                col2 <- c[x][j]
                y += row1 * col2
            newRow.append(y)
        a.append(newRow)
    RETURN a

MATRIXSUBTRACTION(b, c):
    for i in range(len(b)):
        for j in range(len(c)):
           a[i][j] <- b[i][j] - c[i][j]
    RETURN a


MATRIXADDITION(b, c):
    for i in range(len(b)):
        for j in range(len(c)):
            a[i][j] <- b[i][j] + c[i][j]
    RETURN a


