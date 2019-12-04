def getVowels(word):
	vow = []
	for letter in list(word):
		if letter in 'aeiouAEIOU':
			vow.append(letter)
	return vow