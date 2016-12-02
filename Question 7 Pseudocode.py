n <- int(input("Input a integer: "))
z <- n

PRIMENO(n):
    check <- z / n
    if z = n:
        n <- (n - 1)
        primeNo(n)
    elseif n = 1:
        print "Your number is a prime number"
    elseif check != int(check):
        n <- (n - 1)
        primeNo(n)
    elseif check = int(check) AND check != 1:
        print "Your number is not a prime number"
    else:
        print "Your number is a prime number"
    

primeNo(n)
