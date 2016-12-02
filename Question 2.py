#Q - Count the number of trailing 0s in a factorial number

n = int(input("Input an Integer: "))                                      

def factorial(n):                                                         
    if n == 0:                                                            
        return 1                                                          
    else:                                                                 
        return n * factorial(n - 1)                                       
    
def trailingZeros(n):                                                    
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

#factorial(n) find the factorial of a given integer.
#trailgZeros(n) cycles through every number up to (n - 1) from 0 (x)
#if x%d == 0 then the zero counter goes up by one as on zero is trailing.
# x=x/5, this happens so every power of 5 is cycled through to check for all
#trailing zeroes



  
