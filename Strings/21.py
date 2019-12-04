def isAllLettersUsed(word, required):
    for c in required:
        if c not in word:
            return False
    else:
        return True
    
a=isAllLettersUsed('apple', 'google')

print (a)