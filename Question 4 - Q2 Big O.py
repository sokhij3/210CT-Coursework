#Q - Count the number of trailing 0s in a factorial number

n = int(input("Input an Integer: "))                                      #1

def factorial(n):                                                         
    if n == 0:                                                            #1
        return 1                                                          #1
    else:                                                                 #1
        return n * factorial(n - 1)                                       #1
    
def trailingZeros (n):                                                    
    zeros = 0                                                             #1
    d = 5                                                                 #1
    for x in range(0, n+1):                                               #n
        while x > 0:                                                      #n*n
            if x % d == 0:                                                #n*n
                zeros += 1                                                #n*n
                x = x / 5                                                 #n*n
            else:                                                         #1
                break                                                     #1
    print(zeros)                                                          #1

factorial(n)                                                              #1
trailingZeros(n)                                                          #1

#Total = 4n^2 + n + 12
#Big O = O(n^2)
