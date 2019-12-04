def hasSameContent(t1, t2): 
    x=sorted(t1)
    y=sorted(t2)
    
    print(x)
    print(y)
    if x==y:
    		return True
    else:
    		return False

a=hasSameContent((1, 2), (1, 2))
print (a)