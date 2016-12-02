#Q - Write a recursive function (pseudocode and code) to check if a number n is prime 

n = int(input("Input a integer: "))
z = n

def primeNo(n):
    check = z / n
    if z == n:         #makes sure input integer doesnt divide by itself
        n = (n - 1)
        primeNo(n)
    elif n == 1:       #if n reaches 1 then it must be a prime number
        print("Your number is a prime number")
    elif check != int(check):   
        n = (n - 1)
        primeNo(n)
    elif check == int(check) and check != 1:
        print("Your number is not a prime number")
    else:
        print("Your number is a prime number")
        
primeNo(n)

