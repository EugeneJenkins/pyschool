def reverseLookup(dictionary, value):
	result=[]
	for (k,v) in dictionary.items():
		if v == value:
			result.append(k)
	return sorted(result) 