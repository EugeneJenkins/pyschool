def countOddNumbers(numList):
	odd_count = 0
	for num in numList:
		if num % 2 != 0:
			odd_count = odd_count + 1
	return odd_count


import random
numList = random.sample(range(30),8)
print (numList)
print (countOddNumbers(numList))