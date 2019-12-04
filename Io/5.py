# Use seek() and read() methods to retrieve a hidden code from a list of indexes.
# A negative index implies searching from the end of document.
def getCode(filename, indexes): 
	t=""
	f=open(filename)
	f.tell()
	k=0
	
	while k<len(indexes):
		if indexes[k]>0:
			f.seek(indexes[k])
			t = t+f.read(1)
			k+=1
		else:
			f.seek(indexes[k],2)
			t+=f.read(1)
			k+=1
	return t