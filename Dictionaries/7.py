def countLetters(word):
	list0 = set(list(word))   # generate a list of non-repetitive characters
	dict={}
	output=dict.fromkeys(list0)   # generate dict with keywords filled but empty value
	for letter in list0:
		output[letter]=word.count(letter)   #match characters with # of letters appeared 
	return output