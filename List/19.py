def calCumulativeSum(numbers):
	cumulative_list =[ ]
	cumulative_list.append(numbers[0])
	sum = numbers[0]
		
	for i in range (0,len(numbers)-1):
		sum = sum + numbers[i+1]
		cumulative_list.append(sum) 
	
	return cumulative_list


numbers = [13, 15, 17]   
print (calCumulativeSum(numbers))