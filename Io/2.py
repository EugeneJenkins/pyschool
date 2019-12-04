def addEmail(filename, name, email):    
    mode = 'a'
    f = open(filename, mode) # replace the mode
    f.write("%s %s\n" % (name, email))
    f.close()
    return f # do not remove this line