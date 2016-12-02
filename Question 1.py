#Q - Write a function that randomly shuffles an array of integers        
        
from random import *                                                               

numbers = input("Enter a list of numbers: ").split(",")                         
length = len(numbers)                                                        
n = int(length - 1)                                                       

def shuffle(numbers):                                                    
    if length <= 1:                                                       
        print("array is too short")                                      
    else:                                                                 
        for x in range(length):                                          
            z = randrange(n)                                              
            z += z >= x                                                  
            numbers[x], numbers[z] = numbers[z], numbers[x]               
        print(numbers)                                                   
    
shuffle(numbers)                                                         

'''z takes a random number from the array and places it in a new array.
this repeats until the new array is the same length as the old one (x)'''

