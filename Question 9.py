#Q - Adapt the binary search algorithm so that instead of outputting whether a specific value
#was found, it outputs whether a value within an interval (specified by you) was found.

l = input("Please input a list of integers in ascending order: ")       #1
lis = list(map(int, l))                                                 #1


minRange = int(input("Enter the minimum for your range: "))             #1
maxRange = int(input("Enter the maximum for your range: "))             #1

def binarySearch(lis, minRange, maxRange):
    first = 0                                                           #1
    last = lis[-1]                                                      #1
    midpoint = (first + last)//2                                        #1
    output = False                                                      #1

    while first <= last and not output:                                 #n
        if first == minRange or first == maxRange:                      #n
            output = True                                               #1
        elif last == minRange or last == maxRange:                      #n
            output = True                                               #1
        else:                                                           #n
            if minRange < lis[midpoint]:                                #n
                last = last - 1                                         #n
            else:                                                       #n
                first = first + 1                                       #n
    return output                                                       #1

print(binarySearch(lis, minRange, maxRange))

#Total = 8n + 11
#Big O = O(n)

#The binary search checks if the min/max range are in the list themselves.
#if they are then output = true as there is a value in the specified range.
#If not then if the minRange < midpoint, the last value will go down by 1
#else the first value will go up by 1, This will continue until a value is found
#within the range. If not false will be returned.

