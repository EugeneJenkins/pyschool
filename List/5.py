def addOddNumbers(numList):
	oddSum = 0
	for num in numList:
		if num % 2 != 0:
			oddSum = oddSum + num
	return oddSum


import random
numList = random.sample(range(30),8)
print (numList)
print (addOddNumbers(numList))