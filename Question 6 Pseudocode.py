sentence <- input("Input a sentence: ").split()

REVERSE(sentence):
    newSentence <- []
    s <- " "
    for word in sentence:
        newSentence.insert(0, word)
    print s.join(newSentence)



