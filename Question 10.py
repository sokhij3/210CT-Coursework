#Q - Given a sequence of n integer numbers, extract the sub-sequence of maximum length
#    which is in ascending order.

l = input("Please input a list of integers: ")
lis = list(map(int, l)) #map() function makes each iterable in the list lis an int

def ascendingOrder(lis):
    temp = []
    maxSeq = [0]
    for x, y in zip(lis, lis[1:]):          #zip() function taken from stackoverflow as i needed 
        if x < y:                           #to find a way to compare an element of a list the with
            temp.append(x)                  #the next element.
        elif x >= y:
            temp.append(x)
            if len(temp) >= len(maxSeq):      
                maxSeq = temp                
                temp = []                     
            elif len(temp) < len(maxSeq):
                temp = []
    if len(temp) >= len(maxSeq):
        temp.append(y)
        maxSeq = temp
        temp = []
    print(maxSeq)

ascendingOrder(lis)
                
'''if x<y then it is put in a temp array. happens until x>=y. Then temp array length
compared with maxSeq array. If temp>maxSeq then it replaces maxSeq and temp is emptied.
repeats until the biggest sequence of ascending order is found'''

