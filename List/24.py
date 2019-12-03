def getSumOfFirstDigit(number_list):
	count = 0
	for i in number_list:
		num = str(i)
		count = count + int(num[0])

	return count 

number_list = [43, 45, 87]   

print (getSumOfFirstDigit(number_list))