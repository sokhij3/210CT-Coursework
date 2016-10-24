#Q - Count the number of trailing 0s in a factorial number

n = int(input("Input an Integer: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def trailingZeros (n):
    zeros = 0
    d = 5
    for x in range(0, n+1):
        while x > 0:
            if x % d == 0:
                zeros += 1
                x = x / 5
            else:
                break
    print(zeros)

factorial(n)
trailingZeros(n)

#to find the trailing zeros, divide by powers of 5 and count the zeros.
#divide by powers of 5 whilst to result is > 1



  
