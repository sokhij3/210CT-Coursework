#Q - Write a function that randomly shuffles an array of integers        
        
from random import *                                                     #1          

numbers = input("Enter a list of numbers: ").split(",")                  #1       
length = len(numbers)                                                    #1    
n = int(length - 1)                                                      #1 

def shuffle(numbers):                                                    
    if length <= 1:                                                      #1 
        print("array is too short")                                      #1
    else:                                                                #1 
        for x in range(length):                                          #n
            z = randrange(n)                                             #n 
            z += z >= x                                                  #n
            numbers[x], numbers[z] = numbers[z], numbers[x]              #n 
        print(numbers)                                                   #1
    
shuffle(numbers)                                                         #1 

#Total = 4n + 9
#Big O = O(n)
