def removeCommonElements(t1, t2): 
	result = set(list(t1) + list(t2))
	common = []
	for i in t1:
		for j in t2:
			if i == j:
				common.append(i)
	for element in common:
		if element in result:
			result.remove(element)
		else: pass
	return tuple(sorted(result))
			