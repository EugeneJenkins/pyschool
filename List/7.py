def getEvenNumbers(numList):
	even_list = []
	for num in numList:
		if num % 2 == 0:
			even_list.append(num)
	return even_list


import random
numList = random.sample(range(30),8)
print (numList)
print (getEvenNumbers(numList))