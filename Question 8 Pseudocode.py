REMOVEVOWELS(word):
    vowels <- "aeiouAEIOU"
    if word.length = 0:
        return word
    else:
        newWord <- word[1: word.length + 1]
        letter <- word[0]
        if letter in vowels:
            return removeVowels(newWord)
        else:
            return letter + removeVowels(word[1:])
