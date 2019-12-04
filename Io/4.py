def readFile(filename):
    f = open(filename)
    count = 0
    lines = 0
    while 1:
        char = f.read(1)
        if not char: break
        count+=1
        if(char == '\n'):
            lines+=1
    f.close()                  # close file
    return (count, lines)