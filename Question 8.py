#Q - Write a recursive function that removes all vowels from a given string

def removeVowels(word):
    vowels = "aeiouAEIOU"
    if len(word) == 0:
        return word
    else:
        newWord = word[1:len(word) + 1] #adds all letter apart from the first to the array
        letter = word[0]
        if letter in vowels:
            return removeVowels(newWord)   #if first letter of input word is a vowel it is skipped
        else:
            return letter + removeVowels(word[1:])  #if it isnt a vowel it is added back to the start




        
        
