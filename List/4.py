import random

def addNumbersInList(num_list):
	sum_of_numbers = 0
	for num in num_list:
		sum_of_numbers = sum_of_numbers + num
	return sum_of_numbers

num_list = random.sample(range(30), 3)
print (num_list)

print (addNumbersInList(num_list))