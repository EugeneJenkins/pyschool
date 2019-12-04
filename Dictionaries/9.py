def invertDictionary(d):
	initial={}
	AllValue = d.values() 
	output=initial.fromkeys(AllValue) 
	for value in AllValue:                   
		output[value]=[]              
		for (k,v) in d.items():         
			if v == value:           
				output[value].append(k)    
	return output