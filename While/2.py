def addNumbers(start, end):
    total = 0
    i=start
    while start <= i <= end:
        total = total + i
        i +=1
    return total

a= addNumbers(5,10)
print (a)