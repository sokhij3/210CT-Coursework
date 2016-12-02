#Q - Write the pseudocode for a function which returns the highest perfect square which is less
#    or equal to its parameter (a positive integer). Implement this in a programming language of
#    your choice.

x = int(input("input an integer: "))

def perfectSq(x):
    y = x**0.5      #Square rooting the given integer.
    p = int(y)**2   #squaring the integer of the sqrt will
    print(p)        #give you the highest perfect square

perfectSq(x)
