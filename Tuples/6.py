def commonElements(t1, t2): 
	result = []
	for i in t1:
		for j in t2:
			if i == j:
				result.append(i)
	return tuple(sorted(result))