#Q - Write the pseudocode and code for a function that reverses the words in a sentence. 

sentence = input("Input a sentence: ").split()    #1

def reverse(sentence):
    newSentence = []                              #1
    s = " "                                       #1
    for word in sentence:                         #n
        newSentence.insert(0, word)               #n
    print(s.join(newSentence))                    #1
    

reverse(sentence)                                 #1
    
#Total = 2n + 5
#Big O = O(n)

#Takes sentence and inserts each word to the start of an empty array 
