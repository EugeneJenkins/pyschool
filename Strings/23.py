def splitWord(word, numOfChar):
    newlist=[]
    length=len(word)
    i=0
    while i<=length:
        if length-i<=numOfChar:
            newlist.append(word[i:length])
            break
        if length-i>numOfChar:
            newlist.append(word[i:i+numOfChar])
            i=i+numOfChar

    return newlist

a=splitWord('google', 2)
print (a)